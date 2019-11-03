import math

from geomdl import BSpline
from geomdl.visualization import VisMPL, VisVTK, VisPlotly

# Control points
ctrlpts = [
    [[-25.0, -25.0, -10.0], [-25.0, -15.0, -5.0], [-25.0, -5.0, 0.0], [-25.0, 5.0, 0.0], [-25.0, 15.0, -5.0], [-25.0, 25.0, -10.0]],
    [[-15.0, -25.0, -8.0], [-15.0, -15.0, -4.0], [-15.0, -5.0, -4.0], [-15.0, 5.0, -4.0], [-15.0, 15.0, -4.0], [-15.0, 25.0, -8.0]],
    [[-5.0, -25.0, -5.0], [-5.0, -15.0, -3.0], [-5.0, -5.0, -8.0], [-5.0, 5.0, -8.0], [-5.0, 15.0, -3.0], [-5.0, 25.0, -5.0]],
    [[5.0, -25.0, -3.0], [5.0, -15.0, -2.0], [5.0, -5.0, -8.0], [5.0, 5.0, -8.0], [5.0, 15.0, -2.0], [5.0, 25.0, -3.0]],
    [[15.0, -25.0, -8.0], [15.0, -15.0, -4.0], [15.0, -5.0, -4.0], [15.0, 5.0, -4.0], [15.0, 15.0, -4.0], [15.0, 25.0, -8.0]],
    [[25.0, -25.0, -10.0], [25.0, -15.0, -5.0], [25.0, -5.0, 2.0], [25.0, 5.0, 2.0], [25.0, 15.0, -5.0], [25.0, 25.0, -10.0]]
]

# for i in ctrlpts:
#     for j in i:
#         j[2] *= math.sqrt(abs(j[2]))


# Create a BSpline surface
surf = BSpline.Surface()

# Set degrees
surf.degree_u = 3
surf.degree_v = 3

# Set control points
surf.ctrlpts2d = ctrlpts

# Set knot vectors
surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Set evaluation delta
surf.delta = 0.025
# Evaluate surface points
a = surf.evaluate()

# Import and use Matplotlib's colormaps
from matplotlib import cm

# Plot the control points grid and the evaluated surface
surf.vis = VisVTK.VisSurface()
surf.vis.ctrlpts_offset = 6
# surf.render(filename="spline.png", plot=False, cpcolor="red", evalcolor="white")
surf.render(filename="spline.png", cpcolor="red", evalcolor="blue", line_width=5)
