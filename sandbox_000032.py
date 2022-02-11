from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    frame = 600
    num = 19
    r = 0.8
    fig, ax = plt.subplots()
    lines1 = [
        {
            "line"  : ax.plot([], [], linewidth=3)[0],
            "data"  : np.linspace(0, i*2*np.pi, 1+num, endpoint=True),
        }
        for i in list(range(1, 1+num//2))[::-1]
    ]
    lines2 = [
        {
            "line"  : ax.plot([], [], linewidth=3)[0],
            "r" : np.array([1 if j%2 else r for j in range(1+2*num)]),
            "t" : np.linspace(-np.pi, np.pi, 1+2*num, endpoint=True) + i/4*2*np.pi/num,
        }
        for i in range(4)
    ]
    tmp = np.linspace(-np.pi, np.pi, 1+360, endpoint=True)
    x = np.cos(tmp)
    y = np.sin(tmp)
    ax.plot(r*x, r*y, linewidth=3)
    ax.plot((1+r)/2*x, (1+r)/2*y, linewidth=3)
    ax.plot(x, y, linewidth=3)
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
    home = Path(__file__).resolve().parent
    output = home.joinpath("magiccircle")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i / frame * 2*np.pi
        for data in lines1:
            x = r*np.cos(data["data"] + t)
            y = r*np.sin(data["data"] + t)
            data["line"].set_data(x, y)
        for data in lines2:
            x = data["r"] * np.cos(data["t"] - 2*t)
            y = data["r"] * np.sin(data["t"] - 2*t)
            data["line"].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
