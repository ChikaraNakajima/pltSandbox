from pathlib import Path
import shutil


import numpy as np


from template_plt import *


def function(v, t):
    x = (1 + np.cos(1.9*v + t)) * np.cos(v)
    y = (1 + np.cos(1.9*v + t)) * np.sin(v)
    return x, y



def main():
    # 設定
    frame = 1800
    v = np.linspace(-10*np.pi, 10*np.pi, 360 * 10 +  1, endpoint=True)
    fig, ax = plt.subplots()
    wave = ax.plot([], [], color="red", linewidth=3)[0]
    # 見た目調整
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-2.02, 2.02)
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
    # 画像出力
    output = Path(__file__).resolve().parent.joinpath(f"flower")
    if output.is_dir():
        shutil.rmtree(output)
    output.mkdir()
    for i in range(frame):
        t = i * np.pi/120
        x, y = function(v, t)
        wave.set_data(x, y)
        fig.savefig(output.joinpath(f"{i:06d}.png"))
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
