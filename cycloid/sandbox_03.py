from pathlib import Path


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


def main():
    # 設定
    frame = 1800
    num = 60
    time = range(frame)
    v = np.linspace(-num*np.pi, num*np.pi, 360*num+1, endpoint=True)
    fig, ax = plt.subplots()
    p1 = 25
    p2 = 25
    # サイクロイド
    a = 1 - 1/p1
    for i in range(1, 1 + p2):
        b = i/p2
        x, y = cycloid_hypo(a, b, v)
        ax.plot(x, y)
    # 外枠
    ax.plot(np.cos(v), np.sin(v))
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.02, 1.02)
    ax.set_ylim(-1.02, 1.02)
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
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
