from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    home = Path(__file__).resolve().parent
    frame = 300
    num = 19
    fig, ax = plt.subplots()
    tmp = np.linspace(-np.pi, np.pi, 1+360, endpoint=True)
    x = np.cos(tmp)
    y = np.sin(tmp)
    ax.plot(x, y, linewidth=3)
    lines = [
        {
            "line"  : ax.plot([], [], linewidth=3)[0],
            "data"  : np.linspace(0, i*2*np.pi, 1+num, endpoint=True),
        }
        for i in list(range(1, 1+num//2))[::-1]
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
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
    output = home.joinpath("magiccircle")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    x = np.linspace(-2*np.pi, 2*np.pi, 1+360*4, endpoint=True)
    for i in range(frame):
        for data in lines:
            t = i / frame * 2*np.pi
            x = np.cos(data["data"] + t)
            y = np.sin(data["data"] + t)
            data["line"].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
