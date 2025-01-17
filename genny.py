"""
"https://waa-pa.clients6.google.com"
"""

import re
from itertools import groupby
from operator import itemgetter

from jinja2 import Template

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
    def {{lower(method)}}(self):
        return self.call_rpc("{{method}}")
    {% endfor %}


"""

t = Template(template)


def lower(s):
    return re.sub("([a-z])([A-Z])", r"\1_\2", s).lower()


with open("upload/endpoints.py", "w") as f:
    f.write("from .playbooks import RpcService\n\n")

    for service, methods in groupby(sorted(methods, key=key), key=key):
        f.write(
            t.render(
                classname=service.split(".")[-1],
                service=service,
                methods=methods,
                lower=lower,
            )
        )
