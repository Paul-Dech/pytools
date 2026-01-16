import numpy as np

def load_datfile(filename, **kwargs):
    return np.loadtxt(filename, **kwargs)