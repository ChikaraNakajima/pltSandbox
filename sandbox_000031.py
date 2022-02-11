from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    frame = 300
    home = Path(__file__).resolve().parent
    fig, ax = plt.subplots()
    r = 0.8
    v1 = np.linspace(-np.pi, np.pi, 1+3, endpoint=True)
    v2 = np.linspace(-np.pi, np.pi, 1+24, endpoint=True)
    lines1 = [
        ax.plot([], [], linewidth=3)[0],
        ax.plot([], [], linewidth=3)[0],
        ax.plot([], [], linewidth=3)[0],
        ax.plot([], [], linewidth=3)[0],
    ]
    lines2 = [
        ax.plot([], [], linewidth=3)[0],
        ax.plot([], [], linewidth=3)[0],
    ]
    v3 = np.linspace(-np.pi, np.pi, 1+360, endpoint=True)
    ax.plot(np.cos(v3), np.sin(v3), linewidth=3)
    ax.plot(r*np.cos(v3), r*np.sin(v3), linewidth=3)
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
    output = home.joinpath("circle")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    r1 = np.array([1 if i%2 else r for i in range(len(v2))])
    r2 = np.array([r if i%2 else 1 for i in range(len(v2))])
    for i in range(frame):
        t = i / frame * 2 * np.pi
        for u, v in enumerate(lines1):
            x = r*np.cos(v1+t+np.pi/6*u)
            y = r*np.sin(v1+t+np.pi/6*u)
            v.set_data(x, y)
        x = np.cos(v2-2*t) * r1
        y = np.sin(v2-2*t) * r1
        lines2[0].set_data(x, y)
        x = np.cos(v2-2*t) * r2
        y = np.sin(v2-2*t) * r2
        lines2[1].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    return None


if __name__ == "__main__":
    main()
