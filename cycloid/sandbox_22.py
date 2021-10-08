from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def cycloid_epi(a, b, t, *args, **kwargs):
    x = (1+a) * np.cos(t) - b*a*np.cos((1+1/a)*t)
    y = (1+a) * np.sin(t) - b*a*np.sin((1+1/a)*t)
    return x, y


def cycloid_hypo(a, b, t, *args, **kwargs):
    x = (1-a) * np.cos(t) + b*a*np.cos((1-1/a)*t)
    y = (1-a) * np.sin(t) + b*a*np.sin((1-1/a)*t)
    return x, y


def circle_epi(a, t, v, *args, **kwargs):
    x = (1+a) * np.cos(t) - a * np.cos(v)
    y = (1+a) * np.sin(t) - a * np.sin(v)
    return x, y


def circle_hypo(a, t, v, *args, **kwargs):
    x = (1-a) * np.cos(t) + a * np.cos(v)
    y = (1-a) * np.sin(t) + a * np.sin(v)
    return x, y


def main():
    # 設定
    frame = 1800
    num = 11
    pe = 11
    ph = pe//2
    fig, ax = plt.subplots()
    lines_e = [[] for i in range(pe)]
    lines_h = [[] for i in range(ph)]
    # 転がる円
    for i in range(pe):
        lines_e[i].append(ax.plot([], [], color="red", linewidth=3)[0])
    for i in range(ph):
        lines_h[i].append(ax.plot([], [], color="red", linewidth=3)[0])
    # 外枠
    v = np.linspace(-np.pi, np.pi, 361, endpoint=True)
    x = np.cos(v)
    y = np.sin(v)
    ax.plot(x, y, linewidth=3)
    # 軌跡
    for i in range(pe):
        lines_e[i].append(ax.plot([], [], linewidth=3)[0])
    for i in range(ph):
        lines_h[i].append(ax.plot([], [], linewidth=3)[0])
    # 定点
    for i in range(pe):
        lines_e[i].append(ax.plot([], [], color="black", linestyle="None", marker="o")[0])
    for i in range(ph):
        lines_h[i].append(ax.plot([], [], color="black", linestyle="None", marker="o")[0])
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-3.05, 3.05)
    ax.set_ylim(-3.05, 3.05)
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
    output = Path(__file__).resolve().parent.joinpath(f"cycloid_{num:02d}")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    v = np.linspace(-np.pi, np.pi, 361, endpoint=True)
    for i in range(frame):
        angle = i / frame * 2 * np.pi * 12
        t = np.linspace(0, angle, 1+12*i, endpoint=True)
        for j in range(pe):
            a = (1 + j) / num
            x, y = circle_epi(a, angle, v)
            lines_e[j][0].set_data(x, y)
            x, y = cycloid_epi(a, 1, t)
            lines_e[j][1].set_data(x, y)
            x, y = x[-1], y[-1]
            lines_e[j][2].set_data(x, y)
        for j in range(ph):
            a = (1 + j) / num
            x, y = circle_hypo(a, angle, v)
            lines_h[j][0].set_data(x, y)
            x, y = cycloid_hypo(a, 1, t)
            lines_h[j][1].set_data(x, y)
            x, y = x[-1], y[-1]
            lines_h[j][2].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
