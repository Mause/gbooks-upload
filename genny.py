import re
from itertools import groupby
from operator import itemgetter
from subprocess import check_call

from jinja2 import Template
from ruff.__main__ import find_ruff_bin

with open("upload/endpoints.md") as f:
    lines = {line for line in f.read().splitlines() if line}


PREFIX = "https://"
methods = []
for line in lines:
    hostname = "playbooks-pa.clients6.google.com"
    line = line[1:-1]
    if line.startswith(PREFIX):
        hostname, line = line.split("/$rpc")
        hostname = hostname[len(PREFIX) :]
    _, service, method = line.split("/")
    methods.append((hostname, service, method))


key = itemgetter(slice(0, 2))


template = """
class {{classname}}(RpcService):
    hostname = "{{hostname}}"
    service = "{{service}}"

    {% for hostname, _, method in methods %}
    async def {{lower(method)}}(self):
        return await self.call_rpc("{{method}}")
    {% endfor %}


"""

t = Template(template)


def lower(s):
    return re.sub("([a-z])([A-Z])", r"\1_\2", s).lower()


OUT = "upload/endpoints.py"

with open(OUT, "w") as f:
    f.write("from .ghunter import RpcService\n\n")

    for (hostname, service), methods in groupby(sorted(methods, key=key), key=key):
        f.write(
            t.render(
                classname=service.split(".")[-1],
                hostname=hostname,
                service=service,
                methods=sorted(methods),
                lower=lower,
            )
        )
check_call([find_ruff_bin(), "format", OUT])
