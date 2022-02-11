import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


plt.rcParams["axes.facecolor"] = "#eeeeee"
plt.rcParams["axes.grid"] = False
plt.rcParams["figure.dpi"] = 100
plt.rcParams["figure.figsize"] = [19.2, 10.8]
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 20
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["savefig.edgecolor"] = "#eeeeee"
plt.rcParams["savefig.facecolor"] = "#eeeeee"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["xtick.minor.visible"] = False
plt.rcParams["xtick.top"] = False
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["ytick.minor.visible"] = False
plt.rcParams["ytick.right"] = False


def ExpFormatter(digit=None):
    if isinstance(digit, int) and 1 <= digit:
        pass
    else:
        digit = 1
    return StrMethodFormatter(r"$\mathrm{{{x:." + str(digit) + "e}}}$")
