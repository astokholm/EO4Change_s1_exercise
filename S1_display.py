#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    30574 Earth observations for monitoring changes (EO4Change) Day 3 exercise with Sentinel-1 SAR
    Display Sentinel-1 SAR image.
"""

# -- File info -- #
__author__ = ['Andreas R. Stokholm']
__copyright__ = ['A. Stokholm']
__contact__ = ['stokholm@space.dtu.dk']
__version__ = '0.0.1'
__date__ = '2022-06-06'

# -- Built-in modules -- #
import os

# -- Third-party modules -- #
import matplotlib.pyplot as plt
import numpy as np
import PIL

# -- Proprietary modules -- #
from s1_get import SENTINELSAT_OPTIONS
from s1_unzip import unzip

PIL.Image.MAX_IMAGE_PIXELS = 933120000  # PIL will complain that the image is too large without this.


def main(sentinelsat_options: dict):
    # -- Enter name of the Sentinel-1 file here: (Do not include the file extension). -- #
    file = 'S1A_IW_GRDH_1SDV_20220604T170128_20220604T170153_043516_05321B_F7C2'

    # -- Your filename goes above here -- #

    # Unzips zip files to open .SAFE file in data directory.
    unzip(sentinelsat_options=SENTINELSAT_OPTIONS)

    # Keep track of work directory.
    cwd = os.getcwd()
    # Enter data folder
    os.chdir(SENTINELSAT_OPTIONS['data_dir'])

    # Read SAR file. Note that this is just one polarization.
    tiff_index = 1  # Should be VV. Change to 0 for VH.
    tiff_file = os.listdir(file + '.SAFE/measurement/')[tiff_index]
    img = plt.imread(file + '.SAFE/measurement/' + tiff_file)  # Read tiff file.
    os.chdir(cwd)  # Return to original directory.

    print(f"Displaying: {file}")

    # The script should run as long as the filename has been added. However, the displayed file is likely not
    # displaying anything useful. What could be the reason for this?
    # Hint. look at the mean value (print(img.mean())) and the maximum and/or minimum values (print(img.max())).
    # -- Insert your code --#



    # -- End of your code -- #



    # Typically the colorscale is stretched between the minimum and maximum values because of a few outliers.
    # We can get around this by displaying the image without outliers. This can be done using quartiles of the image.
    # E.g. np.quantile(a=img, q=), where q is the percentile between 0-1. Typical values are 5% and 95%.
    # It may be useful to print the quartile values. The quartiles should be added to the plt.imshow function below.
    # The relevant arguments are: vmin=q05, vmax=q95  (where q05, q95 are example of variable names).
    # https://numpy.org/doc/stable/reference/generated/numpy.quantile.html
    # -- Insert your code --#




    # -- End of your code -- #


    # Hopefully you should now see a SAR image of some place on Earth.
    # Is it upside down? If it is, what could be the reason for this? You can fix this by flipping the img array
    # using np.flip(img, axis= ) (axis = 0 or 1)
    # -- Your code goes here -- #
    s1_img = plt.figure()
    plt.imshow(img, cmap='gray')  # It is custom to display SAR images in grayscale.
    plt.colorbar()
    plt.show()

    # Find anything interesting in the image? Let's look at it tomorrow in the lecture.
    # Send me a copy at stokholm@space.dtu.dk either by screenshotting or by saving the image with
    # s1_img.savefig('cool_s1_image.png', format='png'). (The image should be closed directly.)


    return img


if __name__ == '__main__':
    main(sentinelsat_options=SENTINELSAT_OPTIONS)
