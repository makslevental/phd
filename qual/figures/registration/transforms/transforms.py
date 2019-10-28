import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from skimage.io import imread
from skimage.transform import ProjectiveTransform
from skimage import transform


def get_image():
    delta = 0.25
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X ** 2 - Y ** 2)
    Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
    Z = Z1 - Z2
    return Z


def do_plot(ax, Z, transform):
    im = ax.imshow(
        Z, interpolation="none", origin="lower", extent=[-2, 4, -3, 2], clip_on=True
    )

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--", transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
    ax.axis("off")


# prepare image and figure
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
Z = imread("cat.jpg")

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))

# # image skew
# do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))

# # scale and reflection
# do_plot(ax3, Z, mtransforms.Affine2D().scale(-1, 0.5))

# t = mtransforms.Affine2D()
# t = mtransforms.Transform
# print(t.get_matrix())
# do_plot(
#     ax4,
#     Z,
#     t
# )
# src = np.array([[0, 0], [0, 50], [300, 50], [300, 0]])
# dst = np.array([[155, 15], [65, 40], [260, 130], [360, 95]])
#
# tform3 = tf.ProjectiveTransform(np.asarray([[1, 0, 0.002], [1, 1, 0.0002], [0, 0, 1]]))
#
# warped = tf.warp(Z, tform3, output_shape=(4000,4000))
#
# fig, ax = plt.subplots(nrows=2, figsize=(8, 3))
#
# ax[0].imshow(Z, cmap=plt.cm.gray)
# ax[0].plot(dst[:, 0], dst[:, 1], '.r')
# ax[1].imshow(warped, cmap=plt.cm.gray)
#
# for a in ax:
#     a.axis('off')
#
# plt.tight_layout()
#
# plt.show()
trans_names = ['similarity', 'affine', 'piecewise-affine', 'projective']  # transform list

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
# Define the points that are common:
src = [(520, 522),
       (290, 750),
       (780, 94),
       (864, 508)]
dst = [(561, 527),
       (325, 740),
       (799, 190),
       (882, 576)]
for tform_type, axis in zip(trans_names, axes.flat):  # looping through transforms

    # build the model
    tform = transform.estimate_transform(tform_type, np.array(src), np.array(dst))

    # use the model
    raw_corrected_Z = transform.warp(Z, inverse_map=tform.inverse, output_shape=(3840, 3840, 3))

    axis.imshow(raw_corrected_Z, origin='lower')

fig.suptitle('Different transforms applied to the images', y=1.03)
fig.tight_layout()
plt.show()