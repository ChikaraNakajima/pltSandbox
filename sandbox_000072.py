import shutil
from multiprocessing import Pool, cpu_count
from pathlib import Path

import numpy as np

from template_plt import plt


def make_graph(params: dict, *args, **kwargs) -> dict:
    fig, ax = plt.subplots()
    rt = -2*np.pi * params["i"] / params["n"]
    r = np.array([
        [np.cos(rt), -np.sin(rt)],
        [np.sin(rt),  np.cos(rt)],
    ])
    t = np.linspace(0, 6*np.pi, 1+3*3600, endpoint=True)
    x, y = r@np.array([t*np.cos(t), t*np.sin(t)])
    ax.plot(x, y, linewidth=6)
    ax.plot(-x, -y, linewidth=6)
    t = np.linspace(0, 2*np.pi, 1+3600, endpoint=True)
    bx = np.cos(t)
    by = np.sin(t)
    data = []
    for i in range(2):
        for j in range(40):
            tmp = 6*np.pi * ((j/40 - params["i"]/params["n"]) % 1)
            cx, cy = r@np.array([tmp*np.cos(tmp), tmp*np.sin(tmp)]) * (-1)**i
            vec = r@np.array([np.cos(tmp) - tmp*np.sin(tmp), np.sin(tmp) + tmp*np.cos(tmp)])
            vec = 1.2 * vec / np.linalg.norm(vec)
            data.append([cx, cy, tmp, *vec])
    for cx, cy, t, v0, v1 in data:
        x = cx + bx
        y = cy + by
        ax.plot(x, y, linewidth=6)
    for cx, cy, t, v0, v1 in data:
        ax.plot([cx+v0, cx-v0], [cy+v1, cy-v1], linewidth=6)
    for cx, cy, t, v0, v1 in data:
        ax.plot([cx+v1, cx-v1], [cy-v0, cy+v0], linewidth=6)
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
    output = home.joinpath("output")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    num = 1800
    params = [
        {
            "fp": output.joinpath(f"{i:06d}.png"),
            "i" : i,
            "n" : num,
        }
        for i in range(num)
    ]
    cc = cpu_count()
    params = [params[i*5*cc:(1+i)*5*cc] for i in range(num//(5*cc))]
    for param in params:
        with Pool(cc) as p:
            for rv in p.imap_unordered(make_graph, param):
                print(rv["fp"])
    return None


if __name__ == "__main__":
    main()
