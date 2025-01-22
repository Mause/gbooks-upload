import re
from collections import defaultdict
from operator import attrgetter
from subprocess import check_call
from typing import NamedTuple

import yaml
from jinja2 import Environment


class Method(NamedTuple):
    hostname: str
    service: str
    method: str
    body: str


def get_methods():
    with open("upload/endpoints.md") as f:
        lines = {line for line in f.read().splitlines() if line}

    PREFIX = "https://"
    methods = []
    for line in lines:
        body = None
        hostname = "playbooks-pa.clients6.google.com"
        if " " in line:
            line, body = line.split(" ", 1)
        line = line[1:-1]
        if line.startswith(PREFIX):
            hostname, line = line.split("/$rpc")
            hostname = hostname[len(PREFIX) :]
        _, service, method = line.split("/")
        methods.append(Method(hostname, service, method, body))
    return methods


def key(x):
    return x.hostname, x.service


template = """
class {{classname}}Rpc(RpcService):
    hostname = "{{hostname}}"
    service = "{{service}}"

    {% for hostname, _, method, body in methods %}
    async def {{method | lower}}(self{% if body %}, data={{body | repr}}{% endif %}):
        return await self._call_rpc({{method | repr}}{% if body %},
                                    data=data{% endif %})
    {% endfor %}


"""


def lower(s):
    return re.sub("([a-z])([A-Z])", r"\1_\2", s).lower()


env = Environment()
env.filters["lower"] = lower
env.filters["repr"] = repr
t = env.from_string(template)


def groupby(iterable, key):
    result = defaultdict(list)
    for item in sorted(iterable, key=key):
        result[key(item)].append(item)
    return result.items()


def dump_methods(orig_methods):
    with open("upload/endpoints.yaml", "w") as fh:
        result = {
            hostname: {
                service: {
                    "methods": [
                        {
                            "method": method.method,
                            "body": method.body,
                        }
                        for method in sorted(methods, key=attrgetter("method"))
                    ]
                }
                for service, methods in groupby(services, key=attrgetter("service"))
            }
            for hostname, services in groupby(orig_methods, key=attrgetter("hostname"))
        }
        yaml.dump(
            result,
            fh,
            sort_keys=False,
        )


def main():
    methods = get_methods()

    dump_methods(methods)

    OUT = "upload/endpoints_rpc.py"

    with open(OUT, "w") as f:
        f.write("from .ghunter import RpcService\n\n")

        for (hostname, service), methods in groupby(sorted(methods, key=key), key=key):
            f.write(
                t.render(
                    classname=service.split(".")[-1],
                    hostname=hostname,
                    service=service,
                    methods=sorted(methods),
                )
            )
    check_call(["ruff", "format", OUT])


if __name__ == "__main__":
    main()
