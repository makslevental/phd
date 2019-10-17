from math import sqrt

import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.transform import rescale

img = skimage.io.imread("bertrand.png")
img = rgb2gray(img)

plt.imshow(img, cmap=plt.cm.gray)
plt.show()
for i in range(0, 6):
    new_filtered = gaussian(img, sqrt(2) ** i * 1.5)
    if i > 0:
        dog = new_filtered - old_filtered
        skimage.io.imsave(f"dog_bertrand_sigma_{i}.png", dog)
        plt.imshow(dog, cmap=plt.cm.gray)
        plt.show()
    skimage.io.imsave(f"bertrand_sigma_{i}.png", new_filtered)
    plt.imshow(new_filtered, cmap=plt.cm.gray)
    old_filtered = new_filtered
    plt.show()
