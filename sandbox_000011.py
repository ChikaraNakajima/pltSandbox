from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def satellite(r1, a1, r2, a2, v):
    y = r1 * np.cos(a1* v) + r2 * np.cos(a2*v)
    x = r1 * np.sin(a1* v) + r2 * np.sin(a2*v)
    return x, y


def main():
    frame = 1800
    r = 0.2
    num = 20
    fig, ax = plt.subplots()
    v = np.linspace(-np.pi, np.pi, 10*360+1, endpoint=True)
    # 自転
    center = ax.plot([], [], color="black", linestyle="None", marker="o")[0]
    circle = ax.plot([], [], color="red")[0]
    # 公転
    sate = [
        [1+i, ax.plot([], [], color="black", linestyle="None", marker="o")[0]]
        for i in range(num)
    ]
    # 自転
    ax.plot(np.cos(v), np.sin(v), color="red")
    # 公転
    for i in range(num):
        x, y = satellite(1, 1, r, 1+i, v)
        ax.plot(x, y)
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
    fig.savefig(Path(__file__).resolve().with_suffix(".png"))
    output = Path(__file__).resolve().parent.joinpath("satellite")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i * np.pi / 180
        y = np.cos(t)
        x = np.sin(t)
        center.set_data(x, y)
        y = np.cos(t) + r * np.cos(v)
        x = np.sin(t) + r * np.sin(v)
        circle.set_data(x, y)
        for p, q in sate:
            x, y = satellite(1, 1, r, p, t)
            q.set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
