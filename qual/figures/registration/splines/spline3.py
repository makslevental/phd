# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.interpolate as si
#
# points = [
#     [-2, 2],
#     [0, 1],
#     [-2, 0],
#     [0, -1],
#     [-2, -2],
#     [-4, -4],
#     [2, -4],
#     [4, 0],
#     [2, 4],
#     [-4, 4],
# ]
#
# degree = 3
#
# points = points + points[0 : degree + 1]
# points = np.array(points)
# n_points = len(points)
# x = points[:, 0]
#
# t = range(len(x))
# ipl_t = np.linspace(1.0, len(points) - degree, 1000)
#
# x_tup = si.splrep(t, x, k=degree, per=1)
# x_list = list(x_tup)
# xl = x.tolist()
# x_list[1] = [0.0] + xl + [0.0, 0.0, 0.0, 0.0]
#
#
# x_i = si.splev(ipl_t, x_list)
#
#
# fig = plt.figure()
#
# ax = fig.add_subplot(211)
# plt.plot(t, x, "-og")
# plt.plot(ipl_t, x_i, "r")
# plt.xlim([0.0, max(t)])
# plt.title("Splined x(t)")
#
# ax = fig.add_subplot(212)
# for i in range(n_points - degree - 1):
#     vec = np.zeros(11)
#     vec[i] = 1.0
#     x_list = list(x_tup)
#     x_list[1] = vec.tolist()
#     x_i = si.splev(ipl_t, x_list)
#     plt.plot(ipl_t, x_i)
# plt.xlim([0.0, 9.0])
# plt.title("Periodic basis splines")
#
# plt.show()
from scipy.interpolate import BSpline
import numpy
from matplotlib import pyplot

b = BSpline.basis_element([1,2,5,6,8,12])
x = numpy.linspace(1,12,100)
pyplot.plot(x, b(x))
pyplot.show()
