import json
import numpy as np
import matplotlib.pyplot as plt
import random


def save_stuff(array_to_vis):
    arraystuff = np.array(array_to_vis) 
    arraystuff.tofile("floats.float32")
    dims = arraystuff.shape
    with open("floats.json", 'w') as outfile:
        json.dump({"dims":dims}, outfile)
    return arraystuff

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


if __name__ == "__main__":
    readstuff()

