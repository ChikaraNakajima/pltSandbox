from pathlib import Path
import shutil
from multiprocessing import Pool, cpu_count

import numpy as np

from template_plt import *


def make_graph(params: dict, *args, **kwargs) -> dict:
    fig, ax = plt.subplots()
    t = np.linspace(0, 2*np.pi, 1+360, endpoint=True)
    calcry = lambda t : np.array([
        [np.cos(t), 0, -np.sin(t)],
        [0, 1, 0],
        [np.sin(t), 0,  np.cos(t)],
    ])
    ryt = [
        np.pi * ((params["i"]/params["n"] + i/20)%1 - 0.5)
        for i in range(20)
    ]
    ry = [calcry(-i) for i in ryt]
    for i in range(20):
        for iry in ry:
            init = np.array([
                0 * t,
                (i + 18*params["i"]/params["n"]) % 20 - 10 + np.cos(t),
                8 + np.sin(t)
            ])
            x, y, z = iry @ init
            ax.plot(x, y, linewidth=6)
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


def main() -> None:
    home = Path(__file__).resolve().parent
    output = home.joinpath("circle")
    num = 600
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    params = [
        {
            "i"     : i,
            "n"     : num,
            "fp"    : output.joinpath(f"{i:06d}.png"),
        }
        for i in range(num)
    ]
    cc = cpu_count()
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
