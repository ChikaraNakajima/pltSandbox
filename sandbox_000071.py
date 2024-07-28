from pathlib import Path
import shutil
from multiprocessing import Pool, cpu_count

import numpy as np

from template_plt import *


def make_graph(params: dict, *args, **kwargs) -> dict:
    fig, ax = plt.subplots()
    t = -2*np.pi * params["i"] / params["n"]
    r = np.array([
        [np.cos(t), -np.sin(t)],
        [np.sin(t),  np.cos(t)],
    ])
    t = np.linspace(0, 6*np.pi, 1+3*3600, endpoint=True)
    x, y = r@np.array([t*np.cos(t), t*np.sin(t)])
    ax.plot(x, y, linewidth=6)
    ax.plot(-x, -y, linewidth=6)
    t = np.linspace(0, 2*np.pi, 1+3600, endpoint=True)
    bx = np.cos(t)
    by = np.sin(t)
    for i in range(2):
        for j in range(40):
            t = 6*np.pi * ((j/40 - params["i"]/params["n"]) % 1)
            cx, cy = r@np.array([t*np.cos(t), t*np.sin(t)]) * (-1)**i
            x = cx + bx
            y = cy + by
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
    num = 1800
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
