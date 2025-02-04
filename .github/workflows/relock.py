import json
import sys
from subprocess import check_call


def git(*args):
    return check_call(["git"] + list(args))


prs = json.loads(sys.argv[1])

for pr in prs:
    print(f"Processing PR: {pr}")
    branch_name = pr["headBranchName"]
    git("switch", branch_name)

    check_call(["uv", "sync"])

    git("add", ".")
    git("commit", "-m", "chore: update uv.lock")
    git("push")
