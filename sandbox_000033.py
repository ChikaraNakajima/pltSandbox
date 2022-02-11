from pathlib import Path
import shutil
from matplotlib.pyplot import plot


import numpy as np


from template_plt import *


ct = np.linspace(-np.pi, np.pi, 1+360, endpoint=True)
def star(t1, t2, r1, r2, r3, n):
    tmp = np.linspace(0, 2*np.pi*(n//2), 1+n, endpoint=True) + (t1 + t2)
    sx = r1*np.cos(t1) + r2*np.cos(t1+t2) + r3*np.cos(tmp)
    sy = r1*np.sin(t1) + r2*np.sin(t1+t2) + r3*np.sin(tmp)
    cx = r1*np.cos(t1) + r2*np.cos(t1+t2) + r3*np.cos(ct)
    cy = r1*np.sin(t1) + r2*np.sin(t1+t2) + r3*np.sin(ct)
    return sx, sy, cx, cy


def main():
    frame = 300
    fig, ax = plt.subplots()
    n1 = 5
    n2 = 5
    lines = [
        [
            {
                "star"  : ax.plot([], [], linewidth=3)[0],
                "circ"  : ax.plot([], [], linewidth=3)[0],
                "bt1"   : i/n1*2*np.pi,
                "bt2"   : (1+j)/(1+n2)*np.pi,
                "n"     : 5
            }
            for j in range(n2)
        ]
        for i in range(n1)
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
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
    r1 = 0.5
    r2 = 0.5
    r3 = 0.5 * np.sin(np.pi/2/(1+n2))
    for i in range(frame):
        t = i / frame * 2*np.pi
        for j1, v in enumerate(lines):
            for j2, data in enumerate(v):
                t1 = data["bt1"] + t
                t2 = data["bt2"]
                sx, sy, cx, cy = star(t1, t2, r1, r2, r3, data["n"])
                data["star"].set_data(sx, sy)
                data["circ"].set_data(cx, cy)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
