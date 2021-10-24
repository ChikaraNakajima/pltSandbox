from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    home = Path(__file__).resolve().parent
    frame = 600
    fig, ax = plt.subplots()
    lines = [
        ax.plot([], [], linewidth=6)[0],
        ax.plot([], [], linewidth=6)[0],
    ]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-2*np.pi, 2*np.pi)
    ax.set_ylim(-2.1, 2.1)
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
    output = home.joinpath("wave")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    x = np.linspace(-2*np.pi, 2*np.pi, 1+360*4, endpoint=True)
    for i in range(frame):
        t = i / frame * 2*np.pi
        lines[0].set_data(x, 2*np.cos(x+t))
        lines[1].set_data(x, 2*np.sin(x-t))
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
