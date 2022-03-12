from pathlib import Path
import shutil
from multiprocessing import Pool
import os

import numpy as np

from template_plt import *


def make_graph(params, *args, **kwargs):
    fig, ax = plt.subplots()
    x = np.linspace(-16, 16, 1+3600, endpoint=True)
    yc = np.cos(x/16 * 2*np.pi + params["delta"]) ** 2
    ys = np.sin(x/16 * 2*np.pi + params["delta"]) ** 2
    for i in range(1, 18):
        ax.plot(x, i*yc, linewidth=6)
        ax.plot(x, 18-i*ys, linewidth=6)
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-16, 16)
    ax.set_ylim(0, 18)
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
    output = home.joinpath("wave")
    num = 600
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    params = [
        {
            "delta" : 2 * np.pi / num * i,
            "i"     : i,
            "num"   : num,
            "fp"    : output.joinpath(f"{i:06d}.png"),
        }
        for i in range(num)
    ]
    cc = os.cpu_count()
    params = [
        params[i*5*cc:(1+i)*5*cc]
        for i in range(len(params) // (5*cc))
    ]
    for i in params:
        with Pool(processes=cc) as p:
            for j in p.imap_unordered(make_graph, i):
                print(j["fp"])
    return None


if __name__ == "__main__":
    main()
