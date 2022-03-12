from pathlib import Path
import shutil
from multiprocessing import Pool
import os

import numpy as np

from template_plt import *


num = 600


def make_graph(params, *args, **kwargs):
    fig, ax = plt.subplots()
    for i in range(11, 3, -2):
        t = np.linspace(0, i*2*np.pi, 1+i*3600, endpoint=True)
        x = np.cos(t) + 0.1*i*np.cos(1/i*t + (i//4)*params["delta"]*(-1)**(i//2%2))
        y = np.sin(t) + 0.1*i*np.sin(1/i*t + (i//4)*params["delta"]*(-1)**(i//2%2))
        ax.plot(x, y, linewidth=6)
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
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
    output = home.joinpath("orbital")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    params = [
        {
            "delta" : 2 * np.pi / num * i,
            "i"     : i,
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
