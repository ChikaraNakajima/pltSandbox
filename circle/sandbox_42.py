from pathlib import Path
import shutil


import numpy as np


from template_plt import *

n = 1
tmp = np.linspace(0, n*2*np.pi, 1+360*n, endpoint=True)
def gen_lines(r, t):
    x = sum([i * np.cos(j*tmp) for i, j in zip(r, t)])
    y = sum([i * np.sin(j*tmp) for i, j in zip(r, t)])
    return x, y


def main():
    frame = 1
    fig, ax = plt.subplots()
    r = [1.0, 2]
    t = [1.0, -2]
    n = 4
    for i in range(n):
        y, x = gen_lines(r, t)
        a = i/n * 2*np.pi
        rot = np.array([
            [np.cos(a), -np.sin(a)],
            [np.sin(a),  np.cos(a)]
        ])
        x, y = rot@np.array([x, y])
        ax.plot(x, y, linewidth=3)
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    #ax.set_xlim(-1.3, 1.3)
    #ax.set_ylim(-1.3, 1.3)
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
    home = Path(__file__).resolve().parent
    output = home.joinpath("circle")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i / frame * 2*np.pi
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
