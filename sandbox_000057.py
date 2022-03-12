from pathlib import Path
import shutil
from multiprocessing import Pool
import os

import numpy as np

from template_plt import *


colors = [
    "#D0DEEA",
    "#003682",
    "#005EAC",
]

def make_graph(params, *args, **kwargs):
    fig, ax = plt.subplots()
    for i, c in enumerate(colors):
        x = np.linspace(-16, 16, 1+36, endpoint=True) - 32 / 36 * i / (len(colors))
        y = 7 * np.cos(x/16*np.pi - params["delta"])
        ml, sl, bl = ax.stem(x, y-1, bottom=-10)
        ml.set_color(c)
        sl.set_color(c)
        ml, sl, bl = ax.stem(x, y+1, bottom=10)
        ml.set_color(c)
        sl.set_color(c)
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-16, 16)
    ax.set_ylim(-9, 9)
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
    fig.savefig(params["fp"])
    plt.close(fig)
    return params



def main():
    home = Path(__file__).resolve().parent
    output = home.joinpath("stem")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    num = 600
    params = [
        {
            "delta" : 2 * np.pi / num * i,
            "fp"    : output.joinpath(f"{i:06d}.png"),
        }
        for i in range(num)
    ]
    with Pool(processes=os.cpu_count()) as p:
        for i in p.imap_unordered(make_graph, params):
            print(i["fp"])
    return None


if __name__ == "__main__":
    main()
