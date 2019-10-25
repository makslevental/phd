import matplotlib.pyplot as plt
import numpy
import skimage
from skimage import exposure, draw
from skimage.feature import hog
from skimage.transform import downscale_local_mean, resize


def compute_grad_orientations(c_row, c_col, orientations, orientation_histogram, bins):
    radius = min(c_row, c_col) // 2 - 1
    orientations_arr = numpy.arange(orientations)
    # set dr_arr, dc_arr to correspond to midpoints of orientation bins
    orientation_bin_midpoints = (
            numpy.pi * (orientations_arr + .5) / orientations)
    # dr_arr = radius * numpy.sin(orientation_bin_midpoints)
    # dc_arr = radius * numpy.cos(orientation_bin_midpoints)
    grads = orientation_bin_midpoints[orientation_histogram.argmax(axis=2)]
    # grads = resize(grads, (16, 16), preserve_range=True)
    grads_x , grads_y= numpy.cos(grads)/20, numpy.sin(grads)/20
    domin_grad = grads.mean()
    half_bins = 2*bins
    x = numpy.linspace(1/half_bins, (half_bins-1)/half_bins, bins)
    y = numpy.linspace(1/half_bins, (half_bins-1)/half_bins, bins)
    xv, yv = numpy.meshgrid(x, y)
    grads_stack = numpy.vstack([xv.flatten(), yv.flatten(), grads_x.flatten(), grads_y.flatten()]).T
    domin_grad =  numpy.degrees(numpy.arctan(numpy.sin(domin_grad)/ numpy.cos(domin_grad)))

    subgrad_hists = numpy.ceil(skimage.measure.block_reduce(orientation_histogram, (bins//4,bins//4,1), numpy.max))
    return grads_stack, domin_grad, subgrad_hists.reshape(subgrad_hists.shape[0]*subgrad_hists.shape[1],8)

def compute_hog():
    bins = 16
    n_orientations = 8
    img = skimage.io.imread("bert_keypoint_window.png")
    h, w, _ = img.shape
    pixels_per_cell = (h // bins, w // bins)
    # img = rgb2gray(img)
    #
    fd, hog_image, orient_hist = hog(
        img,
        orientations=n_orientations,
        pixels_per_cell=pixels_per_cell,
        cells_per_block=(1, 1),
        visualize=True,
        multichannel=True
    )
    plt.imshow(hog_image); plt.show()
    grads, domin_grad, subgrad_hists = compute_grad_orientations(*pixels_per_cell, n_orientations, orient_hist, bins)
    # print(domin_grad)
    # numpy.savetxt('grads.csv', grads, delimiter=' ',fmt='%1.4f', header="x y u v", comments="")
    # subhist = numpy.around(orient_hist).reshape(16, 8)
    numpy.savetxt('subgrad_hists.csv', subgrad_hists, delimiter=' ',fmt='%1.0f')
    # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)
    #
    # ax1.axis('off')
    # ax1.imshow(img, cmap=plt.cm.gray)
    # ax1.set_title('Input image')
    #
    # # Rescale histogram for better display
    # hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
    #
    # ax2.axis('off')
    # ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
    # ax2.set_title('Histogram of Oriented Gradients')
    # plt.show()
# for i in range(0, 6):
#     new_filtered = gaussian(img, sqrt(2) ** i * 1.5)
#     if i > 0:
#         dog = new_filtered - old_filtered
#         skimage.io.imsave(f"dog_bertrand_sigma_{i}.png", dog)
#         plt.imshow(dog, cmap=plt.cm.gray)
#         plt.show()
#     skimage.io.imsave(f"bertrand_sigma_{i}.png", new_filtered)
#     plt.imshow(new_filtered, cmap=plt.cm.gray)
#     old_filtered = new_filtered
#     plt.show()

if __name__ == '__main__':
    compute_hog()