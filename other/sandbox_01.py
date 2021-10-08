from pathlib import Path

import numpy as np

from template_plt import *


def main():
    fig, ax = plt.subplots()
    r = 0.08
    width = 10
    theta = np.linspace(0, np.pi*5/r, 1+360*10, True)
    x = r*(np.cos(theta) + theta*np.cos(theta))
    y = r*(np.sin(theta) + theta*np.sin(theta))
    ax.plot( x,  y, linewidth=width, dash_capstyle="round", dash_joinstyle="round", label=r"$\alpha$")
    ax.plot(-y,  x, linewidth=width, dash_capstyle="round", dash_joinstyle="round", label=r"$\beta$")
    ax.plot(-x, -y, linewidth=width, dash_capstyle="round", dash_joinstyle="round", label=r"$\gamma$")
    ax.plot( y, -x, linewidth=width, dash_capstyle="round", dash_joinstyle="round", label=r"$\delta$")
    ax.plot(
        r*np.cos(np.linspace(-np.pi, np.pi, 61, True)),
        r*np.sin(np.linspace(-np.pi, np.pi, 61, True)),
        linewidth=width,
        label=r"$\epsilon$",
        dash_capstyle="round",
        dash_joinstyle="round",
    )
    ax.set_xlabel("")
    ax.set_ylabel(
        r"$x = a(\theta + \theta \cos(\theta))$" +
        "\n" +
        r"$y = a(\theta + \theta \sin(\theta))$"
    )
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect("equal")
    ax.tick_params(
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labeltop=False,
        labelleft=False,
        labelright=False,
    )
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
    fig.tight_layout()
    #plt.show()
    fig.savefig(Path(__file__).resolve().with_suffix(".png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
