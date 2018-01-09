import json
import numpy as np
import matplotlib.pyplot as plt
import random


def save_arraylike_to_numpy(array_to_vis, fname):
    arraystuff = np.array(array_to_vis) 
    np.save(fname, arraystuff)
    return arraystuff

def read_and_visualize(fname):
    stuff = np.load(fname)
    plt.matshow(stuff)
    return stuff


if __name__ == "__main__":
    read_and_visualize("floats.npy")

