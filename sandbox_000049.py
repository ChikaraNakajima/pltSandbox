from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    frame = 1800
    fig, ax = plt.subplots()
    w = 20
    h = 10
    lines = [
        {
            "line"  : ax.plot([], [], linewidth=3)[0],
            "ix"    : 0.5+x,
            "iy"    : 0.5+y,
            "vx"    : 0,
            "vy"    : 0.1 * np.sin((0.5 + x)/w * np.pi),
            "r"     : (2.5+i) * 0.1,
        }
        for i in range(3)
        for x in range(w)
        for y in range(h)
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(0, w)
    ax.set_ylim(0.5, h-0.5)
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
    v = np.linspace(0, 2*np.pi, 1+4, endpoint=True)
    bx = np.cos(v)
    by = np.sin(v)
    for i in range(frame):
        for data in lines:
            cx = data["ix"] + i * data["vx"]
            cy = (data["iy"] + i * data["vy"])%h
            x = cx + data["r"] * bx
            y = cy + data["r"] * by
            data["line"].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
