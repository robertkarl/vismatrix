import json
import numpy as np
import matplotlib.pyplot as plt

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

