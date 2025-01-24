import re
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
    with open("endpoints.yaml") as f:
        return yaml.load(f, yaml.SafeLoader)


def key(x):
    return x.hostname, x.service


template = """
class {{classname}}Rpc(RpcService):
    hostname = "{{hostname}}"
    service = "{{service}}"

    {% for method in methods %}
    async def {{method.method | lower}}(self, data={% if method.body %}
        {{method.body | repr}}
        {% else %}
        None
        {% endif %}):
        return await self._call_rpc({{method.method | repr}}, data=data)
    {% endfor %}


"""


def lower(s):
    return re.sub("([a-z])([A-Z])", r"\1_\2", s).lower()


env = Environment()
env.filters["lower"] = lower
env.filters["repr"] = repr
t = env.from_string(template)


def main():
    methods = get_methods()

    OUT = "google_internal_apis/__init__.py"

    with open(OUT, "w") as f:
        f.write("from .ghunter import RpcService\n\n")

        for hostname, services in methods.items():
            for service, methods in services.items():
                f.write(
                    t.render(
                        classname=service.split(".")[-1],
                        hostname=hostname,
                        service=service,
                        methods=methods["methods"],
                    )
                )
    check_call(["ruff", "format", OUT])


if __name__ == "__main__":
    main()
