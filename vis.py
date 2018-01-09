import json
import numpy as np
import matplotlib.pyplot as plt
import torch

import axes3d as a3d

def readstuff():
    bts = None
    with open("floats.float32", 'rb') as fp:
        bts = fp.read()

    with open("floats.json") as fp:
        info = fp.read()
        dims = json.loads(info)
        dims = dims["dims"]
    bts = np.fromstring(bts, 'float')
    stuff = bts.reshape(dims)
    plt.matshow(stuff)
    return stuff


def show_tensor(tensor):

def main(argv):
    a = torch.rand([3, 4, 4])
    show_tensor(a)
    return 0

if __name__ == '__main__':
    import sys;
    return sys.exit(main(sys.argv[1:]))
