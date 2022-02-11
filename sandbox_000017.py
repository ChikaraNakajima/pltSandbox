from pathlib import Path
import shutil


import numpy as np
from mpl_toolkits.mplot3d import Axes3D


from template_plt import *



def main():
    frame = 10
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    t = 1
    r = [-np.pi, np.pi]
    x = np.linspace(*r, 3601, endpoint=True)
    y = np.linspace(*r, 3601, endpoint=True)
    X, Y = np.meshgrid(x, y)
    Z = np.cos(X + Y)
    surface = ax.plot_surface(X, Y, Z, cmap="summer")
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_zlabel("")
    ax.set_xlim(*r)
    ax.set_ylim(*r)
    #ax.set_ylim(-1, 1)
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
    for i in range(frame):
        t = i / 1800 * 4 * np.pi
        Z = np.cos(X + Y + t)
        print(X.shape)
        print(Y.shape)
        print(Z.shape)
        surface.set_verts([X, Y, Z])
    """
    fig.savefig(Path(__file__).resolve().with_suffix(".png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
