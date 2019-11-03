import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import scipy as sp
import scipy.interpolate

cps = pd.read_csv("spline_cps.txt")
x = cps['x'].values
y = cps['y'].values
z = cps['z'].values/5
print(x,y,z)
fig = plt.figure(figsize=(10,6))
ax = axes3d.Axes3D(fig)
ax.scatter3D(x,y,z, c='r')
x_grid = np.linspace(min(x), max(y), 10*len(x))
y_grid = np.linspace(min(y), max(y), 10*len(y))
B1, B2 = np.meshgrid(x_grid, y_grid, indexing='xy')
Z = np.zeros((x.size, z.size))

spline = sp.interpolate.Rbf(x,y,z,function='thin_plate',smooth=5, episilon=5)
f = sp.interpolate.interp2d(x, y, z, kind='cubic')

Z = spline(B1,B2)
Z = f(x_grid, y_grid)
ax.plot_wireframe(B1, B2, Z)
ax.plot_surface(B1, B2, Z,alpha=0.2)
ax.scatter3D(x,y,z, c='r')
fig.savefig("spline.png")