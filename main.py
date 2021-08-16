from astropy.io import fits as fts
import numpy as np

hdu = fts.open(r"C:\Users\mshem\Desktop\pix.fits", "readonly")
data = hdu[0].data

average = np.mean(data)
median = np.median(data)
std = np.std(data)

print(f"{average=}, {median=}, {std=}")
