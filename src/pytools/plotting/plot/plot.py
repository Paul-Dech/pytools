from matplotlib import pyplot as plt
from pytools.io.dat_files.load import load_datfile

def plot(fname, **kwargs):

    plot_type = kwargs.get('type', 'article')

    xy = load_datfile(fname, **kwargs)
    plt.figure()
    plt.plot(xy[:,0], xy[:,1])
    plt.show()