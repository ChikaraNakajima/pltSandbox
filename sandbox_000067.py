import bisect
import random
import shutil
from pathlib import Path
from multiprocessing import Pool, cpu_count

from template_plt import plt


def make_graph(params: dict, *args, **kwargs) -> dict:
    fig, ax = plt.subplots()
    ax.plot(params["x"], params["y"], linestyle="", marker=".", markersize=6, color="green")
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-11, 11)
    ax.set_ylim(0, 12)
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
    output = home.joinpath("barnsley")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    x, y = [0.0], [0.0]
    function = [
        lambda x, y : ( 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6),
        lambda x, y : ( 0.2 *x - 0.26*y,  0.23*x + 0.22*y + 1.6),
        lambda x, y : (-0.15*x + 0.28*y,  0.26*x + 0.24*y + 0.44),
        lambda x, y : ( 0.0, 0.16*y),
    ]
    probability = [0.85, 0.92, 0.99, 1.0]
    for i in range(7200):
        for j in range(10):
            xn, yn = function[bisect.bisect_left(probability, random.random())](x[-1], y[-1])
            x.append(xn)
            y.append(yn)
    params = [
        {
            "fp"    : output.joinpath(f"{i:06d}.png"),
            "x"     : x[:1+10*i],
            "y"     : y[:1+10*i],
        }
        for i in range(7200)
    ]
    cc = cpu_count()
    params = [params[i*5*cc:(1+i)*5*cc] for i in range(7200//(5*cc))]
    for param in params:
        with Pool(cc) as p:
            for rv in p.imap_unordered(make_graph, param):
                print(rv["fp"])
    return None


if __name__ == "__main__":
    main()
