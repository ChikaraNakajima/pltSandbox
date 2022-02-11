from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def satellite(t):
    x = t * np.cos(t)
    y = t * np.son(t)
    return x, y


def main():
    frame = 1800
    fig, ax = plt.subplots()
    lines = [
        [ax.plot([], [], linewidth=3)[0]]
        for i in range(5)
    ]
    for i in range(len(lines)):
        lines[i].append(ax.plot([], [], linewidth=3)[0])
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
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
    output = Path(__file__).resolve().parent.joinpath("spiral")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = (1+i) / 1800 * 12 * np.pi
        v = np.linspace(0, t, 12*i+1, endpoint=True)
        r = np.sqrt(t)
        rl = np.sqrt(v)
        for j, (l1, l2) in enumerate(lines):
            d = j / len(lines) * 2 * np.pi
            x = r * np.cos(t + d)
            y = r * np.sin(t + d)
            l1.set_data([0, x], [0, y])
            x = rl * np.cos(v + d)
            y = rl * np.sin(v + d)
            l2.set_data(x, y)
        ax.set_xlim(-1.05*r, 1.05*r)
        ax.set_ylim(-1.05*r, 1.05*r)
        fig.tight_layout()
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
