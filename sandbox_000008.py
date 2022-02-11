from pathlib import Path
import shutil
import random


import numpy as np
from numpy.core.numeric import outer


from template_plt import *


class Star:
    def __init__(self, r = 0.05, num=7, *args, **kwargs):
        # 半径
        self.r = r
        # 初期位置
        self.cx = random.random()
        self.cy = random.random()
        # 初期回転角度
        self.theta = np.array([i * (num//2)/num * 2*np.pi for i in range(1+num)])
        # 移動速度最大値
        self.vmax = 0.01
        # 回転速度最大値
        self.rmax = np.pi * 0.05
        # 初期速度
        self.v = self.vmax * random.random()
        # 初期向き
        self.d = random.uniform(-np.pi, np.pi)
        # 初期回転速度
        self.vr = self.rmax * random.uniform(-1, 1)
        # 速度更新量最大値
        self.vtup = self.vmax * 0.05
        # 向き更新量最大値
        self.dup = np.pi / 10
        # 回転速度更新量最大値
        self.vrup = self.rmax * 0.1
        return None

    def update(self, *args, **kwargs):
        # 現在位置計算
        x = self.cx + self.r * np.cos(self.theta)
        y = self.cy + self.r * np.sin(self.theta)
        if self.cx <= 0.0:
            if self.d < -0.5 * np.pi or 0.5 * np.pi < self.d:
                self.d = np.pi - self.d
        elif 1.0 <= self.cx:
            if -0.5 * np.pi < self.d < 0.5 * np.pi:
                self.d = np.pi - self.d
        if self.cy <= 0.0:
            if self.d < 0:
                self.d *= -1
        elif 1.0 <= self.cy:
            if 0 < self.d:
                self.d *= -1
        # 向き
        self.d += random.uniform(-self.dup, self.dup)
        while True:
            if self.d < -np.pi:
                self.d += 2*np.pi
            elif np.pi < self.d:
                self.d -= 2*np.pi
            else:
                break
        # 座標更新
        self.cx += self.v * np.cos(self.d)
        self.cy += self.v * np.sin(self.d)
        # 回転角更新
        self. theta += self.vr
        # 速度更新
        while True:
            dv = random.uniform(-self.vtup, self.vtup)
            if 0 <= self.v + dv <= self.vmax:
                self.v += dv
                break
            else:
                continue
        # 回転速度更新
        while True:
            dr = random.uniform(-self.vrup, self.vrup)
            if abs(self.vr + dr) <= self.rmax:
                self.vr += dr
                break
            else:
                continue
        return x, y


def main():
    frame = 1800
    fig, ax = plt.subplots()
    lines = [
        [
            Star(r=random.choice([0.03, 0.04, 0.05, 0.06]), num=1+2*random.randint(2, 6)),
            ax.plot([], [], linewidth=3)[0],
        ]
        for i in range(180)
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
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
    output = Path(__file__).resolve().parent.joinpath("star")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        for j in range(len(lines)):
            x, y = lines[j][0].update()
            lines[j][1].set_data(x, y)
        fig.tight_layout()
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()

