from astropy.io import fits as fts

header = fts.getheader(r"C:\Users\mshem\Desktop\pix.fits")
print(header["Date"])
