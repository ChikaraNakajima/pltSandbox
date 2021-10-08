from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def main():
    # 設定
    num = 25
    fps = 30
    sec = 60
    # 描画領域
    fig, ax = plt.subplots()
    # 動く円 [alpha, circle, point]
    ims = [
        [i/num, ax.plot([], [], color="red")[0]]
        for i in range(1, 1 + num//2)
    ]
    for i in range(len(ims)):
        ims[i].append(ax.plot([], [], color="black", linestyle="None", marker="o")[0])
    # サイクロイド
    v = np.linspace(-num*np.pi, num*np.pi, 360*num+1, True)
    for i in range(len(ims)):
        u = (1 + i) / num
        x = -(1-u)*np.sin(v) - u*np.sin((1-1/u)*v)
        y =  (1-u)*np.cos(v) + u*np.cos((1-1/u)*v)
        ax.plot(x, y)
    # 外枠
    ax.plot(np.cos(v), np.sin(v))
    # 動く円
    def update(t, *args, **kwargs):
        t *= np.pi/180
        for a, c, p in ims:
            cx = a*np.sin(v) - (1-a)*np.sin(t)
            cy = a*np.cos(v) + (1-a)*np.cos(t)
            px = -(1-a)*np.sin(t) - a*np.sin((1-1/a)*t)
            py =  (1-a)*np.cos(t) + a*np.cos((1-1/a)*t)
            c.set_data(cx, cy)
            p.set_data(px, py)
        return None
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("\n".join([
        r"$x = (1-\alpha)\cos(\theta) + \alpha\cos((1-\frac{1}{\alpha})\theta)$",
        r"$y = (1-\alpha)\sin(\theta) + \alpha\sin((1-\frac{1}{\alpha})\theta)$",
    ]))
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
    output = Path(__file__).resolve().parent.joinpath(f"hypocycloid_{num:02d}")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(fps * sec):
        update(i)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
