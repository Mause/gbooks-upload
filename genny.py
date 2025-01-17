"""
"https://waa-pa.clients6.google.com"
"""

import re
from itertools import groupby
from operator import itemgetter
from subprocess import check_call

from jinja2 import Template
from ruff.__main__ import find_ruff_bin

with open("upload/endpoints.md") as f:
    lines = {line[1:-1] for line in f.read().splitlines() if line}


methods = []
for line in lines:
    _, service, method = line.split("/")
    methods.append((service, method))


key = itemgetter(0)


template = """
class {{classname}}(RpcService):
    service = "{{service}}"

    {% for _, method in methods %}
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

    for service, methods in groupby(sorted(methods, key=key), key=key):
        f.write(
            t.render(
                classname=service.split(".")[-1],
                service=service,
                methods=sorted(methods),
                lower=lower,
            )
        )
check_call([find_ruff_bin(), "format", OUT])
