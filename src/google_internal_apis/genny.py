import logging
import re
from pathlib import Path
from subprocess import check_call
from textwrap import dedent
from typing import NamedTuple

import yaml
from jinja2 import Environment
from rich.logging import RichHandler

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])

HERE = Path(__file__).parent


class Method(NamedTuple):
    hostname: str
    service: str
    method: str
    body: str


def get_methods():
    with open(HERE / "endpoints.yaml") as f:
        return yaml.load(f, yaml.SafeLoader)


def key(x):
    return x.hostname, x.service


template = """
class {{classname}}Rpc(RpcService):
    service = "{{service}}"

    def __init__(self, creds, client):
        super().__init__(creds, client)
        self.hostname = "{{hostname}}"

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

    OUT = HERE / "google_internal_apis/endpoints.py"

    with open(OUT, "w") as f:
        f.write(
            dedent("""
        from .ghunter import RpcService

        """)
        )

        for hostname, services in methods.items():
            for service, methods in services.items():
                if isinstance(methods, str):
                    logging.warning(f"Skipping {hostname}.{service}")
                    continue
                f.write(
                    t.render(
                        classname=service.split(".")[-1],
                        hostname=hostname,
                        service=service,
                        methods=methods["methods"],
                    )
                )
    check_call(["ruff", "format", OUT])
    check_call(["ruff", "check", OUT, "--fix"])


if __name__ == "__main__":
    main()
