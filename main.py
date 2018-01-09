import json
import numpy as np
import matplotlib.pyplot as plt
import torch

import axes3d as a3d

def show_tensor(tensor):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(torch.ones(4, 4, 3).numpy(), facecolors="blue", edgecolor='black')
    plt.show()

def main(argv):
    a = torch.rand([3, 4, 4])
    show_tensor(a)
    return 0

if __name__ == '__main__':
    import sys;
    sys.exit(main(sys.argv[1:]))
