from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def henon(x, y):
    x1 = y + 1 - 1.4 * x**2
    y1 = 0.3 * x
    return x1, y1


def main():
    frame = 1800
    home = Path(__file__).resolve().parent
    fig, ax = plt.subplots()
    lines = [
        ax.plot([], [], linewidth=3)[0],
        ax.plot([], [], linewidth=3)[0],
        ax.plot([], [], linewidth=3)[0],
        ax.plot([], [], linewidth=3)[0],
        ax.plot([], [], linewidth=3)[0],
    ]
    ax.plot([0, 0], [-np.pi, np.pi], linewidth=3)
    ax.plot([-np.pi, np.pi], [0, 0], linewidth=3)
    v = np.linspace(-np.pi, np.pi, 3601, endpoint=True)
    x = np.cos(v)
    y = np.sin(v)
    ax.plot(x, y, linewidth=3)
    lines.append(ax.plot([], [], linestyle="", marker="o", color="black")[0])
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-np.pi, np.pi)
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
    output = home.joinpath("circle")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    x = [1]
    y = [1]
    for i in range(frame):
        t = i / frame * 2 * np.pi * 12
        x = np.cos(v - t)
        y = - np.sin(v - t)
        lines[0].set_data(x, v)
        lines[1].set_data(v, y)
        x = np.cos(t)
        y = np.sin(t)
        lines[2].set_data([x, x], [-np.pi, np.pi])
        lines[3].set_data([-np.pi, np.pi], [y, y])
        lines[4].set_data([0, x], [0, y])
        lines[5].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    return None


if __name__ == "__main__":
    main()
