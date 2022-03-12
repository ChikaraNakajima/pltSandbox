from pathlib import Path
import shutil
from multiprocessing import Pool
import os

import numpy as np

from template_plt import *


def make_graph(params, *args, **kwargs):
    fig, ax = plt.subplots()
    # 基準線
    ax.plot([-2*np.pi, 4*np.pi], [0, 0], linewidth=6)
    # 円
    t = np.linspace(0, 2*np.pi, 1+3600, endpoint=True)
    x = np.cos(t) + params["delta"]
    y = np.sin(t) + 1
    ax.plot(x, y, linewidth=6)
    # サイクロイド
    t = np.linspace(-2*np.pi, 4*np.pi, 1+3*3600, endpoint=True)
    for i in range(10):
        a = (1+i) / 10
        x = t - a * np.sin(t)
        y = 1 - a * np.cos(t)
        ax.plot(x, y, linewidth=6)
    # 点・線
    x = np.linspace(params["delta"], params["delta"] - np.sin(params["delta"]), 11, endpoint=True)
    y = np.linspace(1, 1 - np.cos(params["delta"]), 11, endpoint=True)
    ax.plot(x, y, linewidth=6)
    ax.plot(x, y, markersize=12, marker="o", linestyle="", color="black")
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(params["delta"] - np.pi, params["delta"] + np.pi)
    ax.set_ylim(-0.7, 2.7)
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
    output = home.joinpath("cycloid")
    num = 300
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
