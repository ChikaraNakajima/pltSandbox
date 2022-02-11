from pathlib import Path
import shutil

import numpy as np
from numpy.core import shape_base
from scipy.integrate import solve_ivp

from template_plt import *


def lorenz(t, Y, p=10, r=28, b=8/3):
    x, y, z = Y
    rv = np.array([
        -p*x + p*y,
        -x*z + r*x - y,
        x*y - b*z,
    ])
    return rv


def solve(y0=None):
    t_span = [0, 108]
    if y0:
        y0 = y0[:3]
    else:
        y0 = [1, 0, 0]
    t_eval = np.linspace(*t_span, 1+100000, endpoint=True)
    sol = solve_ivp(lorenz, t_span=t_span, y0=y0, t_eval=t_eval)
    return sol





def main():
    home = Path(__file__).resolve().parent
    frame = 1800
    fig, ax = plt.subplots()
    sol = solve()
    t = sol.t
    #x, y, z = sol.y
    #y, z, x = sol.y
    z, x, y = sol.y
    ax.plot(x, y, color="red")
    point = ax.plot([], [], color="black", linestyle="", marker="o")[0]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    #ax.set_xlim(-2*np.pi, 2*np.pi)
    #ax.set_ylim(-2.1, 2.1)
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
    output = home.joinpath("lorentz")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        index = (1+i) * (len(t)//frame)
        point.set_data(x[index], y[index])
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
