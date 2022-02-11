from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    frame = 100
    fig, ax = plt.subplots()
    num = 16
    lines = [
        {
            "line"  : ax.plot([], [], linewidth=3)[0],
            "t"     : 2*np.pi * (j + k/10) / num,
            "r"     : k + 10*i,
            "v"     : -1/10,
        }
        for i in range(3)
        for j in range(num)
        for k in range(10)
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-16, 16)
    ax.set_ylim(-9, 9)
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
    home = Path(__file__).resolve().parent
    output = home.joinpath("array")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    v = np.linspace(0, 2*np.pi, 1+360, endpoint=True)
    bx = np.cos(v)
    by = np.sin(v)
    ax.plot(bx, by, linewidth=3, color="black")
    for i in range(frame):
        for line in lines:
            r = (line["r"] + i * line["v"])%30
            x = r*np.cos(line["t"]) + bx
            y = r*np.sin(line["t"]) + by
            line["line"].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
