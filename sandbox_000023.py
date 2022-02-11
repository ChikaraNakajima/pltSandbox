from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def henon(x, y):
    x1 = y + 1 - 1.4 * x**2
    y1 = 0.3 * x
    return x1, y1


def main():
    frame = 1800
    home = Path(__file__).resolve().parent
    fig, ax = plt.subplots()
    line    = ax.plot([], [], linestyle="", marker="o", color="#649f44")[0]
    point   = ax.plot([], [], linestyle="", marker="o", color="#295782")[0]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.4, 0.4)
    ax.set_aspect("equal")
    ax.tick_params(
        axis="both",
        which="both",
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labeltop=False,
        labelleft=False,
        labelright=False,
    )
    fig.tight_layout()
    output = home.joinpath("Henon")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    x = [1]
    y = [1]
    for i in range(frame):
        for j in range(100):
            x1, y1 = henon(x[-1], y[-1])
            x.append(x1)
            y.append(y1)
        line.set_data(x, y)
        point.set_data(x[-1], y[-1])
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    return None


if __name__ == "__main__":
    main()
