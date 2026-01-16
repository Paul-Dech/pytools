from pytools.plotting.plot.plot import plot
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

file = f'{THIS_DIR}/naca0012.dat'

plot(file, skiprows=1)
