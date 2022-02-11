from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def main():
    frame = 1
    fig, ax = plt.subplots()
    v = np.linspace(0, 4*np.pi, 1+5, endpoint=True)
    x = np.sin(v)
    y = np.cos(v)
    ax.plot(x, y, linewidth=10,color="red")
    v = np.linspace(0, 2*np.pi, 1+5, endpoint=True)
    x = np.sin(v)
    y = np.cos(v)
    ax.plot(x, y, linewidth=10, color="green")
    v = np.linspace(0, 2*np.pi, 1+360, endpoint=True)
    x = np.sin(v)
    y = np.cos(v)
    ax.plot(x, y, linewidth=15, color="black")
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
    output = Path(__file__).resolve().parent.joinpath("satellite")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
