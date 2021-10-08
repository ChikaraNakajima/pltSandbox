from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def main():
    fig, ax = plt.subplots()
    frame = 1800
    v = np.linspace(-np.pi, np.pi, 10*360+1, endpoint=True)
    line = ax.plot([], [], linewidth=3, color="red")[0]
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
    output = Path(__file__).resolve().parent.joinpath("lissajous")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i / frame * 2 * np.pi
        x = np.cos(3 * v + t)
        y = np.sin(5 * v + t)
        line.set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
