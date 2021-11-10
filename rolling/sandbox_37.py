from pathlib import Path
import shutil
from matplotlib.pyplot import plot


import numpy as np


from template_plt import *


def gen_lines(t, r, offset=0):
    x = np.cos(t) + r*np.cos(-2*t+offset)
    y = np.sin(t) + r*np.sin(-2*t+offset)
    return x, y

def gen_pol(cx, cy, n, r, offset):
    tmp = np.linspace(-np.pi, np.pi, 1+n, endpoint=True) + offset
    x = r*np.cos(tmp) + cx
    y = r*np.sin(tmp) + cy
    return x, y


def main():
    frame = 150
    n = 4
    fig, ax = plt.subplots()
    t_base = np.linspace(0, np.pi, 1+360, endpoint=True)
    lines = [
        {
            "line"  : ax.plot([], [], linewidth=3)[0],
            "offset": i*2*np.pi/n,
        }
        for i in range(n)
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.0, 2.0)
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
    for i in range(frame):
        t = i / frame * 2*np.pi
        for data in lines:
            x, y = gen_lines(t+t_base, 0.8, data["offset"])
            data["line"].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
