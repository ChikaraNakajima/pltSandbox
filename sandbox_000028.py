from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    home = Path(__file__).resolve().parent
    frame = 600
    fig, ax = plt.subplots()
    l = np.linspace(-1, 1, 1001, endpoint=True)
    xx, yy = np.meshgrid(l, l)
    r = np.sqrt(xx**2 + yy**2)
    im = ax.imshow(r, vmin=-1, vmax=1, cmap="plasma")
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    #ax.set_xlim(-2*np.pi, 2*np.pi)
    #ax.set_ylim(-2.1, 2.1)
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
    output = home.joinpath("heatmap")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i / frame
        h = np.cos(12*np.pi * (t + r))
        im.set_data(h)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
