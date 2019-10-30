import numpy
import numpy as np
import skimage
from matplotlib import pyplot
from matplotlib.transforms import Affine2D
from skimage.color import rgb2gray
from skimage.data import stereo_motorcycle
from skimage.feature import register_translation
from skimage.registration import optical_flow_tvl1

reference_image, moving_image, disp = stereo_motorcycle()
reference_image = rgb2gray(reference_image)
moving_image = rgb2gray(moving_image)

reference_image = skimage.io.imread("image003.png", as_gray=True)
moving_image = skimage.io.imread("image004.png", as_gray=True)
dpi = 24
px, py = reference_image.shape
fig = pyplot.figure(figsize=(py / numpy.float(dpi), px / numpy.float(dpi)))
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(moving_image, cmap="gray")
fig.savefig("moving_image.png", transparent=True)
ax.imshow(reference_image, cmap="gray")
fig.savefig("reference_image.png", transparent=True)

shift, error, diffphase = register_translation(reference_image, moving_image)
print(shift)

flow = optical_flow_tvl1(reference_image, moving_image)
downscale = 10
flow = skimage.measure.block_reduce(flow, (1, downscale, downscale), numpy.mean)

h, w = flow[0].shape
X = np.arange(w)
Y = np.arange(h)
U, V = flow[1], flow[0]

M = np.hypot(U, V)
q = ax.quiver(
    X, Y, U, V,
    transform=Affine2D().scale(downscale, downscale) + ax.transData,
    width=.01,
    color="red"

)
fig.savefig("flow.png", transparent=True)
fig.show()
