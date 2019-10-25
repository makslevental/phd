import numpy
# noinspection PyUnresolvedReferences
from mpl_toolkits.mplot3d import Axes3D
import skimage
from matplotlib import pyplot, cm
from numpy import unravel_index
from skimage.feature import greycomatrix


def ncc():
    image = skimage.io.imread("cat.jpg", as_gray=True)
    fig = pyplot.figure()
    ax = fig.gca(projection='3d')
    trim = 500
    shift = -100
    trimmed_image = image[trim:-trim, trim:-trim]
    # skimage.io.imsave("trimmed_cat.jpg", trimmed_image)
    shifted_trimmed = image[trim + shift:-trim + shift, trim + shift:-trim + shift]
    # skimage.io.imsave("shifted_trimmed_cat.jpg", shifted_trimmed)

    image_product = numpy.fft.fft2(trimmed_image) * numpy.fft.fft2(shifted_trimmed).conj()
    nor = (image_product * image_product.conj())
    cc_image = numpy.fft.fftshift(numpy.fft.ifft2(image_product/nor))
    print(cc_image.shape)

    hh, ww = cc_image.shape
    print(cc_image.real.max(),
          numpy.asarray(unravel_index(cc_image.argmax(), cc_image.shape)) - numpy.asarray((hh / 2, ww / 2)))
    X, Y = numpy.meshgrid(range(ww), range(hh))
    surf = ax.plot_surface(X, Y, cc_image.real, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    fig.show()

    cc = skimage.measure.block_reduce(cc_image.real, (50, 50), numpy.max)
    h, w = cc.shape
    print(h, w)
    X, Y = numpy.meshgrid(range(w), range(h))
    X = X.flatten() * 50
    Y = Y.flatten() * 50

    surf = numpy.vstack([X - ww / 2, Y - hh / 2, numpy.around((10*cc)).flatten()]).T
    numpy.savetxt('delta_surf.csv', surf, delimiter=',', fmt='%1.0f')

def joint_entropy():
    image1 = skimage.io.imread("shifted_trimmed_cat.jpg", as_gray=True)
    image2 = skimage.io.imread("trimmed_cat.jpg", as_gray=True)
    h, w = image1.shape
    joint_hist = numpy.zeros((256,256))
    for i in range(h):
        for j in range(w):
            int1 = image1[i,j]
            int2 = image2[i,j]
            joint_hist[int1, int2] += 1

    joint_prob = joint_hist/(h*w)
    fig = pyplot.figure()
    ax = fig.gca(projection='3d')
    ww, hh = joint_prob.shape
    X, Y = numpy.meshgrid(range(ww), range(hh))
    surf = ax.plot_surface(X, Y, joint_prob, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    fig.show()
    joint_entropy = -numpy.sum(joint_prob[joint_prob>0] * numpy.log(joint_prob[joint_prob>0]))
    print(joint_entropy)

if __name__ == '__main__':
    joint_entropy()