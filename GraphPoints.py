import sys
import matplotlib.pyplot as plt
import numpy as np

def exportPlot (filepath):
    x, y = np.loadtxt(filepath, delimiter=",", unpack=True)
    plt.plot(x, y)
    plt.savefig("testscatter.png")

if __name__ == "__main__":
    exportPlot(sys.argv[1])