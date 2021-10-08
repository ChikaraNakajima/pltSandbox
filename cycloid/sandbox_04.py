from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def cycloid_epi(a, b, t, *args, **kwargs):
    x = (1+a) * np.sin(t) - b*a*np.sin((1+1/a)*t)
    y = (1+a) * np.cos(t) - b*a*np.cos((1+1/a)*t)
    return x, y


def cycloid_hypo(a, b, t, *args, **kwargs):
    x = (1-a) * np.sin(t) + b*a*np.sin((1-1/a)*t)
    y = (1-a) * np.cos(t) + b*a*np.cos((1-1/a)*t)
    return x, y


def circle_epi(a, t, v, *args, **kwargs):
    x = (1+a) * np.sin(t) - a * np.sin(v)
    y = (1+a) * np.cos(t) - a * np.cos(v)
    return x, y


def circle_hypo(a, t, v, *args, **kwargs):
    x = (1-a) * np.sin(t) + a * np.sin(v)
    y = (1-a) * np.cos(t) + a * np.cos(v)
    return x, y


def main():
    # 設定
    frame = 1800
    num = 60
    time = range(frame)
    v = np.linspace(-num*np.pi, num*np.pi, 360*num+1, endpoint=True)
    fig, ax = plt.subplots()
    p = 11
    # 動く円
    mc_epi = [[(1 + i) / p] for i in range(p)]
    mc_hypo = [[(1 + i) / p] for i in range(p//2)]
    for i in range(len(mc_epi)):
        l2d = ax.plot([], [], color="red")[0]
        mc_epi[i].append(l2d)
    for i in range(len(mc_epi)):
        l2d = ax.plot([], [], color="black", linestyle="None", marker="o")[0]
        mc_epi[i].append(l2d)
    for i in range(len(mc_hypo)):
        l2d = ax.plot([], [], color="red")[0]
        mc_hypo[i].append(l2d)
    for i in range(len(mc_hypo)):
        l2d = ax.plot([], [], color="black", linestyle="None", marker="o")[0]
        mc_hypo[i].append(l2d)
    # サイクロイド
    for i in range(p):
        a = (1+i) / p
        x, y = cycloid_epi(a, 1, v)
        ax.plot(x, y)
    for i in range(1+p//2):
        a = (1+i) / p
        x, y = cycloid_hypo(a, 1, v)
        ax.plot(x, y)
    # 外枠
    ax.plot(np.cos(v), np.sin(v))
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-3.02, 3.02)
    ax.set_ylim(-3.02, 3.02)
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
    fig.savefig(Path(__file__).resolve().with_suffix(".png"))
    output = Path(__file__).resolve().parent.joinpath(f"cycloid_{p:02d}")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i * np.pi / 180
        for a, *cl in mc_epi:
            x, y = circle_epi(a, t, v)
            cl[0].set_data(x, y)
            x, y = cycloid_epi(a, 1, t)
            cl[1].set_data(x, y)
        for a, *cl in mc_hypo:
            x, y = circle_hypo(a, -t, v)
            cl[0].set_data(x, y)
            x, y = cycloid_hypo(a, 1, -t)
            cl[1].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
