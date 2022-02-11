from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    frame = 1800
    home = Path(__file__).resolve().parent
    fig, ax = plt.subplots()
    lines = [
        ax.plot([], [], linewidth=3)[0]
        for i in range(20)
    ]
    v = np.linspace(-np.pi, np.pi, 1 + 360, endpoint=True)
    x = (np.cos(v) + 1) * np.cos(v)
    y = (np.cos(v) + 1) * np.sin(v)
    ax.plot(x, y, linewidth=3, color="red")
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.0, 2.5)
    ax.set_ylim(-1.5, 1.5)
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
    output = home.joinpath("pascal")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    v = np.linspace(-2*np.pi, 2*np.pi, 1 + 360*4, endpoint=True)
    for i in range(frame):
        for j, line in enumerate(lines):
            t = (i + j) * 18  / frame % 1
            x = (np.cos(v) + t) * np.cos(v)
            y = (np.cos(v) + t) * np.sin(v)
            line.set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
