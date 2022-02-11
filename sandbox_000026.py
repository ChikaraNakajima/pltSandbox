from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    frame = 1800
    fig, ax = plt.subplots()
    line = ax.plot([], [], linewidth=3)[0]
    x = np.linspace(-3*np.pi, 3*np.pi, 1 + 360*6, endpoint=True)
    n = 180
    waves = [
        4 / np.pi /(2*i-1) * np.sin((2*i-1)*x)
        for i in range(n)
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(-3, 3)
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
    output = Path(__file__).resolve().parent.joinpath("fourier")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = min(i%(2*n), 2*n - i%(2*n)) + 1
        y = sum(waves[:t])
        line.set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
