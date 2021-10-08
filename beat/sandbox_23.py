from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def beat(x, t):
    y0 = np.cos(46*x + 1*t) + np.cos(44*x + 11*t)
    y1 = 2 * np.cos(x - 5*t)
    return y0, y1


def main():
    # 設定
    frame = 1800
    x = np.linspace(-np.pi, np.pi, 360 * 10 +  1, endpoint=True)
    fig, ax = plt.subplots()
    lines = [
        ax.plot([], [], linewidth=6, color="#cd659f")[0],
        ax.plot([], [], linewidth=6, color="#829ac8")[0],
        ax.plot([], [], linewidth=6, color="#77c2b9")[0],
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-2.02, 2.02)
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
    output = Path(__file__).resolve().parent.joinpath(f"beat")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i * 1.0e-3
        y0, y1 = beat(x, t)
        lines[0].set_data(x, y0)
        lines[1].set_data(x, y1)
        lines[2].set_data(x, -y1)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
