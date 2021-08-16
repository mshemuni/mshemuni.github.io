from astropy.io import fits as fts
import numpy as np
from photutils.detection import DAOStarFinder

# # Veriyi okuma
data = fts.getdata(r"C:\Users\mshem\Desktop\pix.fits")

# Verinin istatistiki değerleri
average = np.mean(data)
median = np.median(data)
std = np.std(data)

# Daofind Objesi oluşturma
daofind = DAOStarFinder(fwhm=2.0, threshold=std/2)
sources = daofind(data - median)
for col in sources.colnames:
    sources[col].info.format = '%.8g'

print(sources.info)
print(sources)

# # Anlamlı görüntü oluşturmak için matplotlib işlemleri
# fig, (ax1, ax2) = plt.subplots(1, 2)
#
# ax1.imshow(data, interpolation='nearest',
#            cmap='gray', vmin=average - std, vmax=average + std)
# ax2.imshow(data, interpolation='nearest',
#            cmap='gray', vmin=average - std, vmax=average + std)
# for source in sources:
#     ax2.scatter(source["xcentroid"], source["ycentroid"], s=5, facecolor="red")
#
# plt.suptitle("M51 (IRAF dev$pix Verisi)")
#
# ax1.set_title("Görüntü")
# ax1.set_xticks([])
# ax1.set_yticks([])
#
# ax2.set_title("Kaynaklar")
# ax2.set_xticks([])
# ax2.set_yticks([])
#
# plt.tight_layout()
# plt.show()
