from pathlib import Path
import shutil


import numpy as np
from numpy.lib.index_tricks import nd_grid


from template_plt import *


def gen_lines(t, r, offset=0):
    x = np.cos(t) + r*np.cos(-2*t+offset)
    y = np.sin(t) + r*np.sin(-2*t+offset)
    return x, y


def main():
    frame = 600
    n = 3
    fig, ax = plt.subplots()
    t_base = np.linspace(0, np.pi, 1+360, endpoint=True)
    lines = [
        {
            "line"  : ax.plot([], [], linewidth=3)[0],
            "rot"   : 2*np.pi * i / n + np.pi* j/10,
            "phase" : np.pi* j/10,
        }
        for i in range(n)
        for j in range(10)
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
    # 画像出力
    home = Path(__file__).resolve().parent
    output = home.joinpath("rolling")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    t = np.linspace(-np.pi, np.pi, 1+360, endpoint=True)
    bx = np.cos(t)
    by = np.sin(t)
    for i in range(frame):
        t = i / frame * 2*np.pi
        for data in lines:
            x = np.cos(data["rot"]+t)*bx - np.sin(data["rot"]+t)*by*np.cos(data["phase"]+t)
            y = np.sin(data["rot"]+t)*bx + np.cos(data["rot"]+t)*by*np.cos(data["phase"]+t)
            data["line"].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
