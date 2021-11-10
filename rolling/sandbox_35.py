from pathlib import Path
import shutil
from matplotlib.pyplot import plot


import numpy as np


from template_plt import *


def gen_lines(t, r, n=20):
    x = np.cos(t)
    y = np.sin(t)
    yield x, y
    for i in range(n-1):
        x = r*x + (1-r)*np.roll(x, shift=1)
        y = r*y + (1-r)*np.roll(y, shift=1)
        yield x, y


def main():
    frame = 600
    n = 40
    fig, ax = plt.subplots()
    lines = [ax.plot([], [], linewidth=3)[0] for i in range(n)]
    theta = np.linspace(-np.pi, np.pi, 8, endpoint=False)
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
    # 画像出力
    home = Path(__file__).resolve().parent
    output = home.joinpath("rolling")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i / frame * 2*np.pi
        r = 2*i/frame
        r = min(r, 2-r)
        for j, (x, y) in enumerate(gen_lines(t=theta+t, r=r, n=n)):
            x = np.append(x, x[0])
            y = np.append(y, y[0])
            lines[j].set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
