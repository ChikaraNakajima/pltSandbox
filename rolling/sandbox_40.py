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
    frame = 300
    fig, ax = plt.subplots()
    t_base = np.linspace(0, np.pi, 1+360, endpoint=True)
    n1 = 3
    n2 = 12
    lines = [
        {
            "line"  : ax.plot([], [], linewidth=3)[0],
            "cx"    : np.cos(2*np.pi / n1 * i),
            "cy"    : np.sin(2*np.pi / n1 * i),
            "r"     : 0.1 * (2+j%3),
            #"rt1"   : np.pi / 3 if j%3 else 0,
            "rt2"   : 1/3*np.pi * (j//3+1)/3,
            "rt3"   : np.pi / 3 * i,
            "pt1"   : np.pi / 6 * (j//3),
        }
        for j in range(n2)
        for i in range(n1)
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
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
    angle = np.linspace(-np.pi, np.pi, 1+3, endpoint=True)
    for i in range(frame):
        t = i / frame * 2*np.pi
        for l in lines:
            cx = l["cx"] * np.cos(l["pt1"]+t)
            cy = l["cy"] * np.cos(l["pt1"]+t)
            #px = l["r"] * np.cos(angle + l["rt1"] + l["rt2"])
            #py = l["r"] * np.sin(angle + l["rt1"] + l["rt2"])
            px = l["r"] * np.cos(angle + l["rt2"] + l["rt3"] + t)
            py = l["r"] * np.sin(angle + l["rt2"] + l["rt3"] + t)
            l["line"].set_data(cx+px, cy+py)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
