from pathlib import Path
import re


template = """\
from pathlib import Path

import numpy as np

from template_plt import *


def main():
    home = Path(__file__).resolve().parent
    return None


if __name__ == "__main__":
    main()
"""


def main():
    home = Path(__file__).resolve().parent
    re_pattern = re.compile(".+?_(\d+).*?\.py")
    num = 1 +  max(
        int(mo.group(1))
        for fp in home.glob("**/*.py")
        if (mo := re_pattern.search(fp.name))
    )
    home.joinpath(f"sandbox_{num}.py").write_text(template, encoding="utf-8")
    return None


if __name__ == "__main__":
    main()
