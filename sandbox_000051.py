from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def clock(t, r1, r2):
    x = np.array([r1*np.sin(t),  r2*np.cos(t), -r1*np.sin(t), -r2*np.cos(t), r1*np.sin(t)])
    y = np.array([r1*np.cos(t), -r2*np.sin(t), -r1*np.cos(t),  r2*np.sin(t), r1*np.cos(t)])
    return x, y


def main():
    fig, ax = plt.subplots()
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
    # 基本設定
    frame = 300
    num = 2*3
    # 外枠
    outer = [
        {
            "line"  : ax.plot([], [], linewidth=5, color="#666666")[0],
            "bt"    : 2*np.pi / num * i,
            "vt"    : 2*np.pi / frame,
            "r"     : 1 * np.sin(np.pi/num),
        }
        for i in range(num)
    ]
    # 時計の針
    hands = [
        {
            "line"  : ax.plot([], [], linewidth=5)[0],
            "bti"   : 2*np.pi / num * i,
            "dti"   : 2*np.pi/30 * j * (-1)**i,
            "vti"   : 2*np.pi / frame * (-1)**i,
            "bto"   : 2*np.pi / num * i,
            "vto"   : 2*np.pi / frame,
            "r"     : 1 * np.sin(np.pi/num),
        }
        for i in range(num)
        for j in range(30)
    ]
    # 点
    point = [
        {
            "line"  : ax.plot([], [], linestyle="", color="black", marker="o")[0],
            "bt"    : 2*np.pi / num * i,
            "vt"    : 2*np.pi / frame,
            "r"     : 1 * np.sin(np.pi/num),
        }
        for i in range(num)
    ]
    # 画像出力
    output = Path(__file__).resolve().parent.joinpath("clock")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    v   = np.linspace(0, 2*np.pi, 1+360, endpoint=True)
    bx  = np.cos(v)
    by  = np.sin(v)
    for i in range(frame):
        for data in outer:
            t   = data["bt"] + i * data["vt"]
            x   = np.cos(t) + data["r"] * bx
            y   = np.sin(t) + data["r"] * by
            data["line"].set_data(x, y)
        for data in hands:
            t   = data["bto"] + i * data["vto"]
            cx  = np.cos(t)
            cy  = np.sin(t)
            t   = 2*np.pi/frame*i + data["bti"] + data["dti"] + i * data["vti"]
            hx  = cx + data["r"] * np.cos(t)
            hy  = cy + data["r"] * np.sin(t)
            data["line"].set_data([cx, hx], [cy, hy])
        for data in point:
            t   = data["bt"] + i * data["vt"]
            x   = np.cos(t)
            y   = np.sin(t)
            data["line"].set_data([x], [y])
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
