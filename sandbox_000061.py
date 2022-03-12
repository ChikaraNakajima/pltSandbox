from pathlib import Path
import shutil
from multiprocessing import Pool
import os

import numpy as np

from template_plt import *


num = 600

def make_graph(params, *args, **kwargs):
    t = np.linspace(0, 20*np.pi, 1+3600, endpoint=True)
    fig, ax = plt.subplots()
    tmp = [
        0.3,
        0.7,
        1.1,
        1.3,
        1.7,
        1.9,
        2.3,
        2.9,
        3.1,
        3.7,
        0.3,
        0.7,
        1.1,
        1.3,
        1.7,
        1.9,
        2.3,
        2.9,
        3.1,
        3.7,
    ]
    for j, i in enumerate(tmp):
        x = np.cos(t + params["delta"] * (-1)**(j)) + np.cos(i*t) + 2*j
        y = np.sin(t + params["delta"] * (-1)**(j)) + np.sin(i*t)
        ax.plot(x, y, linewidth=6)
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    tmp = 20 * params["i"] / params["num"]
    ax.set_xlim(tmp, tmp+8)
    ax.set_ylim(-2.25, 2.25)
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
    output = home.joinpath("circle")
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
    with Pool(processes=os.cpu_count()) as p:
        for i in p.imap_unordered(make_graph, params):
            print(i["fp"])
    return None


if __name__ == "__main__":
    main()
