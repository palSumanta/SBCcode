#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:35:37 2020

@author: David Velasco
"""

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from skimage import  exposure, io 
from skimage.util import compare_images


img1 = io.imread('/home/pi/SBCcode/DAQ/Cameras/RPi_CameraServers/python/Captures/0.png')
img2 = io.imread('/home/pi/SBCcode/DAQ/Cameras/RPi_CameraServers/python/Captures/2.png')

diff = compare_images(img1, img2, method='diff')



fig = plt.figure(figsize=(8, 9))

gs = GridSpec(3, 2)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[0, 1])
ax2 = fig.add_subplot(gs[1:, :])

ax0.imshow(img1, cmap='gray')
ax0.set_title('Image 1')
ax1.imshow(img2, cmap='gray')
ax1.set_title('Image 2')
ax2.imshow(diff, cmap='gray')
ax2.set_title('Diff comparison')
for a in (ax0, ax1, ax2):
    a.axis('off')
plt.tight_layout()
plt.plot()
