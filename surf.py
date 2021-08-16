from astropy.io import fits as fts
from matplotlib import pyplot as plt


data = fts.getdata(r"C:\Users\mshem\Desktop\pix.fits")
print(data.min(), data.max())

x, y = data.shape
z = data

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
