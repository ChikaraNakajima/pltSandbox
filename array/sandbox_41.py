from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    frame = 150
    fig, ax = plt.subplots()
    lines = [
        {
            "l1"    : ax.plot([], [], linewidth=3)[0],
            "l2"    : ax.plot([], [], linewidth=3)[0],
            "x"     : x,
            "y"     : y,
        }
        for x in range(21)
        for y in range(11)
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 10)
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
    a1 = np.linspace(-np.pi, np.pi, 1+5, endpoint=True)
    a2 = np.linspace(-2*np.pi, 2*np.pi, 1+5, endpoint=True)
    for i in range(frame):
        t = i / frame * 2*np.pi
        for l in lines:
            x = 0.2*np.cos(a1+t) + l["x"]
            y = 0.2*np.sin(a1+t) + l["y"]
            l["l1"].set_data(x, y)
            x = 0.2*np.cos(a2+t) + l["x"] + 0.5
            y = 0.2*np.sin(a2+t) + l["y"] + 0.5
            l["l2"].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
