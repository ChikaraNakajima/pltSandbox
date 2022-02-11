from pathlib import Path
import shutil

import numpy as np

from template_plt import *


def main():
    frame = 1800
    fig, ax = plt.subplots()
    data = [1 for i in range(10)]
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.05, 1.05)
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
    home = Path(__file__).resolve().parent
    output = home.joinpath("ring")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = 360 * i / frame
        for j in range(10):
            if j%2:
                cc = True
                sa = 1
            else:
                cc = False
                sa = -1
            ax.pie(
                data,
                #counterclock=cc,
                startangle=t * (2 - 0.1*j),
                radius=1 - 0.1*j,
                wedgeprops={"linewidth": 3, "edgecolor": "#eeeeee"}
            )
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        ax.set_aspect("equal")
        fig.savefig(output.joinpath(f"{i:06d}.png"))
        plt.cla()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
