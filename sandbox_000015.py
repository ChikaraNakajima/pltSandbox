from pathlib import Path
import shutil


import numpy as np
from mpl_toolkits.mplot3d import Axes3D


from template_plt import *


def satellite(t):
    x = t * np.cos(t)
    y = t * np.son(t)
    return x, y


def main():
    frame = 1800
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    r = [-100, 100]
    #fig, ax = plt.subplots()
    x = np.linspace(*r, 2001, endpoint=True)
    y = np.linspace(*r, 2001, endpoint=True)
    X, Y = np.meshgrid(x, y)
    Z = X**2 - Y**2
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_zlabel("")
    ax.set_xlim(*r)
    ax.set_ylim(*r)
    #ax.set_aspect("equal")
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
    """
    output = Path(__file__).resolve().parent.joinpath("spiral")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    fig.savefig(output.joinpath(f"{i:06d}.png"))
    """
    ax.plot_surface(X, Y, Z, cmap="summer")
    #ax.contour(X, Y, Z)
    fig.savefig(Path(__file__).resolve().with_suffix(".png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
