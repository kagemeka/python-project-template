import argparse
import os

CFD = os.path.dirname(os.path.abspath(__file__))
ROOT = f"{CFD}/../.."
SPHINX_DOCS_PATH = f"{ROOT}/docs/sphinx"

CONTENT = """\
import os
import sys

sys.path.append(f"{os.path.dirname(os.path.abspath(__file__))}/../../src")
from _sphinx_conf import *
from _rtd_conf import *
"""


def _generate(sphinx_docs_path: str) -> None:
    with open(f"{sphinx_docs_path}/conf.py", mode="w") as f:
        f.write(CONTENT)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sphinx-docs-path",
        type=str,
        default=SPHINX_DOCS_PATH,
        required=False,
    )
    args = parser.parse_args()
    _generate(args.sphinx_docs_path)
