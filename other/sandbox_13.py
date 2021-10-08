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
    k = 1
    num = 100
    fig, ax = plt.subplots()
    v = np.linspace(-np.pi, np.pi, 10*360+1, endpoint=True)
    for i in range(num+1):
        k = i/num
        x = np.cos(v) + k
        y = (1-k**2)**0.5 * np.sin(v)
        ax.plot(x, y)
        #ax.plot(y, x)
        #ax.plot(-x, y)
        #ax.plot(y, -x)
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.05, 2.05)
    ax.set_ylim(-1.05, 1.05)
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
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
