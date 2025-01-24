import re
from pathlib import Path
from subprocess import check_call
from textwrap import dedent
from typing import NamedTuple

import yaml
from jinja2 import Environment

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

    OUT = HERE / "google_internal_apis/__init__.py"

    with open(OUT, "w") as f:
        f.write(
            dedent("""
        from typing import TypeVar

        import httpx
        from ghunt.helpers import auth

        from .ghunter import RpcService

        T = TypeVar("T", bound="RpcService")


        async def get_client(t: type[T]) -> T:
            client = httpx.AsyncClient()
            creds = await auth.load_and_auth(client)
            return t(creds, client)

        """)
        )

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
    check_call(["ruff", "check", OUT, "--fix"])


if __name__ == "__main__":
    main()
