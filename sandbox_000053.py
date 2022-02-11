from pathlib import Path
import shutil
from multiprocessing import Pool
import os

import numpy as np

from template_plt import *


def make_graph(params, *args, **kwargs):
    fig, ax = plt.subplots()
    t = np.linspace(0, 2*np.pi, 1+3600, endpoint=True)
    ax.plot(np.cos(t), np.sin(t), linewidth=3)
    #ax.plot(0.6*np.cos(t), 0.6*np.sin(t), linewidth=3)
    #ax.plot(1.4*np.cos(t), 1.4*np.sin(t), linewidth=3)
    for i in range(4):
        r = 1.0 + 0.4*np.cos(6*t + i*0.5*np.pi + params["delta"] * (-1)**i)
        x = r * np.cos(t)
        y = r * np.sin(t)
        ax.plot(x, y, linewidth=3)
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
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
    output = home.joinpath("array")
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
