from pathlib import Path
import shutil


import numpy as np


from template_plt import *



def main():
    fig, ax = plt.subplots()
    v = np.linspace(-np.pi, np.pi, 10*360+1, endpoint=True)
    for i in np.linspace(1, 3, 31, endpoint=True):
        a = 1 / i
        b = 1 / a
        x = np.cos(v) / a
        y = np.sin(v) / b
        ax.plot(x, y)
        x = np.cos(v) / b
        y = np.sin(v) / a
        ax.plot(x, y)
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-3.05, 3.05)
    ax.set_ylim(-3.05, 3.05)
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
