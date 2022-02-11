from pathlib import Path
import shutil


from scipy.spatial import Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
import numpy as np


from template_plt import *


def main():
    frame = 1800
    fig, ax = plt.subplots()
    points = np.random.rand(10000, 2)
    tri = Delaunay(points)
    delaunay_plot_2d(tri, ax)
    vor = Voronoi(points)
    voronoi_plot_2d(vor, ax)
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
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
    output = Path(__file__).resolve().parent.joinpath("Voronoi")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i / frame * 0.8
        ax.set_xlim(0.05+t, 0.15+t)
        ax.set_ylim(0.05+t, 0.11+t)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
