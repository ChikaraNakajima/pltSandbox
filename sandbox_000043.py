from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def clock(t, r1, r2):
    x = np.array([r1*np.sin(t),  r2*np.cos(t), -r1*np.sin(t), -r2*np.cos(t), r1*np.sin(t)])
    y = np.array([r1*np.cos(t), -r2*np.sin(t), -r1*np.cos(t),  r2*np.sin(t), r1*np.cos(t)])
    return x, y


def main():
    frame = 1800
    fig, ax = plt.subplots()
    # 飾り
    v = np.linspace(0, 2*np.pi, 1+24, endpoint=True)
    x = np.sin(v)
    y = np.cos(v)
    r = np.array([1.1 if i%2 else 0.9 for i in range(25)])
    ax.plot(r*x, r*y, linewidth=3)
    r = np.array([0.9 if i%2 else 1.1 for i in range(25)])
    ax.plot(r*x, r*y, linewidth=3)
    r = np.array([0.7 if i%2 else 0.5 for i in range(25)])
    ax.plot(r*x, r*y, linewidth=3)
    r = np.array([0.5 if i%2 else 0.7 for i in range(25)])
    ax.plot(r*x, r*y, linewidth=3)
    r = np.array([0.3 if i%2 else 0.1 for i in range(25)])
    ax.plot(r*x, r*y, linewidth=3)
    r = np.array([0.1 if i%2 else 0.3 for i in range(25)])
    ax.plot(r*x, r*y, linewidth=3)
    # 外枠
    v = np.linspace(0, 2*np.pi, 1+360, endpoint=True)
    x = np.sin(v)
    y = np.cos(v)
    ax.plot(1.1*x, 1.1*y, linewidth=3)
    ax.plot(0.9*x, 0.9*y, linewidth=3)
    ax.plot(0.7*x, 0.7*y, linewidth=3)
    ax.plot(0.5*x, 0.5*y, linewidth=3)
    ax.plot(0.3*x, 0.3*y, linewidth=3)
    ax.plot(0.1*x, 0.1*y, linewidth=3)
    # 時計の針
    hands = {
        "short" : [
            {
                "line"  : ax.plot([], [], linewidth=3)[0],
                "r1"    : 0.3 - 0.1*i   ,
                "r2"    : (0.3 - 0.1*i) * 0.4,
            }
            for i in range(3)
        ],
        "long"  : [
            {
                "line"  : ax.plot([], [], linewidth=3)[0],
                "r1"    : 0.5 - 0.1*i   ,
                "r2"    : (0.5 - 0.1*i) * 0.2,
            }
            for i in range(3)
        ],
    }
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
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
    output = Path(__file__).resolve().parent.joinpath("clock")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i / frame * 2*np.pi
        for h in hands["long"]:
            x, y = clock(12*t, h["r1"], h["r2"])
            x += 0.5 * np.sin(12*t)
            y += 0.5 * np.cos(12*t)
            h["line"].set_data(x, y)
        for h in hands["short"]:
            x, y = clock(t, h["r1"], h["r2"])
            x += 0.3 * np.sin(t)
            y += 0.3 * np.cos(t)
            h["line"].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
