from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def main():
    fig, ax = plt.subplots()
    v = np.linspace(-np.pi, np.pi, 10*360+1, endpoint=True)
    for i in range(20):
        delta = i * np.pi / 10
        x = np.cos(2*v + delta)
        y = np.sin(3*v)
        ax.plot(x, y)
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.05, 1.05)
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
