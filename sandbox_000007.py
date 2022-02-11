from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def function(r, a, v, t):
    x = 0.5 * r * (1 + np.cos(a*v + t)) * np.cos(v)
    y = 0.5 * r * (1 + np.cos(a*v + t)) * np.sin(v)
    return x, y


def circle(r, t):
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y



def main():
    # 設定
    frame = 1800
    fig, ax = plt.subplots()
    v = np.linspace(-10*np.pi, 10*np.pi, 10*360+1, endpoint=True)
    waves = [
        [0.7, ax.plot([], [], linewidth=3)[0]],
        [0.9, ax.plot([], [], linewidth=3)[0]],
        [1.1, ax.plot([], [], linewidth=3)[0]],
        [1.3, ax.plot([], [], linewidth=3)[0]],
        [1.7, ax.plot([], [], linewidth=3)[0]],
        [1.9, ax.plot([], [], linewidth=3)[0]],
    ]
    center = ax.plot([], [], linewidth=3)[0]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
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
    output = Path(__file__).resolve().parent.joinpath("flower")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i * np.pi / 120
        for j, (a, line) in enumerate(waves):
            delta = j / len(waves) * 2 * np.pi
            x, y = function(0.5, a, v, (j+1)*t*(-1)**j)
            cx, cy = circle(1, t+delta)
            line.set_data(cx+x, cy+y)
        x, y = function(0.5, 2.1, v, t)
        center.set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
