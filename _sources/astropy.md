# astropy 

```Astropy```, astronomların kullanımına sunulmuş, pyhton programa dili ile yazılmış, bir yazılımlar koleksyonudur.

## Fits veri

Her bilim topluluğu ortak veri türleri ile çalışır. Astronomide kullanılan veri türü ise 
FITS'tir.(Flexible Image Transport System)

FITS, Header ve Veri olmak üzere iki parçadan oluşur. FITS'in Header kısmı ascii formatında olup human-readable'dır 
(insan tarafından okunabilir). Veri kısmı ise, yer tarasarrufu adına Binary olup human-readable değildir.

FITS formatı kayıpsız bir formattır. Dolayısıyla diskte çokça yer kaplar ve gerektiğinde çeşitli sıkıştırma 
algoritmalarıyla (zip, tar gibi) sıkıştırılabilir.

### Başlık
Bir FITS başlığı ascii formatında olup iki kolonlu bir tablo olarak algılanabilir. Bu tablonun ilk kolonunda başlık 
anahtarı/kartıları, ikinci kolonda ise anahtara karşılık gelen değer yer almaktadır.
```
SIMPLE  =                    T / Fits standard                                  
BITPIX  =                   16 / Bits per pixel                                 
NAXIS   =                    2 / Number of axes                                 
NAXIS1  =                  512 / Axis length                                    
NAXIS2  =                  512 / Axis length                                    
EXTEND  =                    F / File may contain extensions                    
ORIGIN  = 'NOAO-IRAF FITS Image Kernel July 2003' / FITS file originator        
DATE    = '2021-08-16T08:23:55' / Date FITS file was generated                  
IRAF-TLM= '2021-08-16T08:23:55' / Time of last modification                     
OBJECT  = 'm51  B  600s'       / Name of the object observed                    
IRAF-MAX=           1.993600E4  /  DATA MAX                                     
IRAF-MIN=          -1.000000E0  /  DATA MIN                                     
CCDPICNO=                   53  /  ORIGINAL CCD PICTURE NUMBER                  
ITIME   =                  600  /  REQUESTED INTEGRATION TIME (SECS)            
TTIME   =                  600  /  TOTAL ELAPSED TIME (SECS)                    
OTIME   =                  600  /  ACTUAL INTEGRATION TIME (SECS)               
DATA-TYP= 'OBJECT (0)'          /  OBJECT,DARK,BIAS,ETC.                        
DATE-OBS= '05/04/87'            /  DATE DD/MM/YY                                
RA      = '13:29:24.00'         /  RIGHT ASCENSION                              
DEC     = '47:15:34.00'         /  DECLINATION                                  
EPOCH   =                 0.00  /  EPOCH OF RA AND DEC                          
ZD      = '22:14:00.00'         /  ZENITH DISTANCE                              
UT      = ' 9:27:27.00'         /  UNIVERSAL TIME                               
ST      = '14:53:42.00'         /  SIDEREAL TIME                                
CAM-ID  =                    1  /  CAMERA HEAD ID                               
CAM-TEMP=              -106.22  /  CAMERA TEMPERATURE, DEG C                    
DEW-TEMP=              -180.95  /  DEWAR TEMPRATURE, DEG C                      
F1POS   =                    2  /  FILTER BOLT I POSITION                       
F2POS   =                    0  /  FILTER BOLT II POSITION                      
TVFILT  =                    0  /  TV FILTER                                    
CMP-LAMP=                    0  /  COMPARISON LAMP                              
TILT-POS=                    0  /  TILT POSITION                                
BIAS-PIX=                    0  /                                               
BI-FLAG =                    0  /  BIAS SUBTRACT FLAG                           
BP-FLAG =                    0  /  BAD PIXEL FLAG                               
CR-FLAG =                    0  /  BAD PIXEL FLAG                               
DK-FLAG =                    0  /  DARK SUBTRACT FLAG                           
FR-FLAG =                    0  /  FRINGE FLAG                                  
FR-SCALE=                 0.00  /  FRINGE SCALING PARAMETER                     
TRIM    = 'Apr 22 14:11 Trim image section is [3:510,3:510]'                    
BT-FLAG = 'Apr 22 14:11 Overscan correction strip is [515:544,3:510]'           
FF-FLAG = 'Apr 22 14:11 Flat field image is Flat1.imh with scale=183.9447'      
CCDPROC = 'Apr 22 14:11 CCD processing done'                                    
AIRMASS =    1.08015632629395   / AIRMASS                                       
HISTORY 'KPNO-IRAF'                                                             
HISTORY '24-04-87'                                                              
HISTORY 'KPNO-IRAF'           /                                                 
HISTORY '08-04-92'            /                                                 
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
END                                                                             


```

#### Başlık kuraları:

1. Başlıkların anahtar kelimeleri en fazla 8 karakter olabilir
2. Başlığın anahtar kelimesi ve değerine ek olarak açıklama da yazılabilir.
3. Başlık nümerik, metin ve mantıksal olmak üzere 3 çeşit veri tipi taşıyabilir.
4. Başlık bloğunun tamamı 32 ve katları satırdan oluşmak zorunda. ```END``` ile son başlık anahtarı arasındaki boşluk 
   32'nin katına tamamlamak için bırakılöıştır.

:::{note}
Bir FITS dosyasının FITS olabilmesi için gerekli olan en az 4 anahtar bulunmakta. Bunlar: 

- SIMPLE
- BITPIX
- NAXIS
- NAXIS1

dir.
:::

:::{note}
**SIMPLE** başlığı mantıksal bir veri taşır. T veya F değeri alır ve söz konusu dosyanın basit bir FITS dosyası olup 
olmadığını ifade eder.
:::


### Veri
FITS formatı, diğer sayısal görüntü formatlarında olduğu gibi veriyi 2 boyutlu bir matris şeklinde tutar. Söz konusu matrisin 
her hücresindeki değer, sayısal görüntünün aynı pikseline karşılık gelen değeri olacaktır.

![pix](../pix.png)

M51 (IRAF ```dev$pix``` görüntüsü)


## Astropy ile FITS
Astropy astronomların ihtiyaç duyabileceği bir çok kütüphaneyi barındıran bir sistemdir. Bu sistem ile zaman hesabı, 
koordinat dönüşümleri ve modelleme gibi bir çok işlem yapılablir.

Astropy'ın sunduğu hizmetlerden biri de FIST veri işlemleridir. Bunun için Astropy'ın Input/Output modülünün altında Fits 
objesi kullanılır:

```
from astropy.io import fits as fts

help(fts)
```

```fits```'te en çok kullanacağımz metodlar:

- ```getdata```
- ```getheader```
- ```open```

olacaktır.

### getdata
Bir FITS dosyasının Veri kısmına ulaşmak için kullanılır. Dosya üzerinde güncelleme'ye izin vermez. 
Yalnızca veriyi sunar.
```
from astropy.io import fits as fts

data = fts.getdata(r"[Dosya Yolu]")
print(data)
print(type(data))

```
Çıktı:
```
[[38 43 35 ... 45 43 41]
 [36 41 37 ... 42 41 39]
 [38 45 37 ... 42 35 43]
 ...
 [49 52 49 ... 41 35 39]
 [57 52 49 ... 40 41 43]
 [53 57 57 ... 39 35 45]]
 
<class 'numpy.ndarray'>
```

getdata veriyi 2 boyutlu* bir ```numpy.ndarray``` olarak verir.

:::{note}
*: Bir FITS dosyasında birden fazla görüntü taşınabilir. Bu durumda veri 3 boyutlu matris olarak sunulur.
:::

### getheader
Bir FITS dosyasının Başlık kısmına ulaşmak için kullanılır. Dosya üzerinde güncelleme'ye izin vermez. 
Yalnızca başlığı sunar.
```
from astropy.io import fits as fts

header = fts.getheader(r"[Dosya Yolu]")
print(header)
print(type(header))


```
Çıktı:
```
SIMPLE  =                    T / Fits standard                                  BITPIX  =                   16 / Bits per pixel                                 NAXIS   =                    2 / Number of axes                                 NAXIS1  =                  512 / Axis length                                    NAXIS2  =                  512 / Axis length                                    EXTEND  =                    F / File may contain extensions                    ORIGIN  = 'NOAO-IRAF FITS Image Kernel July 2003' / FITS file originator        DATE    = '2021-08-16T08:23:55' / Date FITS file was generated                  IRAF-TLM= '2021-08-16T08:23:55' / Time of last modification                     OBJECT  = 'm51  B  600s'       / Name of the object observed                    IRAF-MAX=           1.993600E4  /  DATA MAX                                     IRAF-MIN=          -1.000000E0  /  DATA MIN                                     CCDPICNO=                   53  /  ORIGINAL CCD PICTURE NUMBER                  ITIME   =                  600  /  REQUESTED INTEGRATION TIME (SECS)            TTIME   =                  600  /  TOTAL ELAPSED TIME (SECS)                    OTIME   =                  600  /  ACTUAL INTEGRATION TIME (SECS)               DATA-TYP= 'OBJECT (0)'          /  OBJECT,DARK,BIAS,ETC.                        DATE-OBS= '05/04/87'            /  DATE DD/MM/YY                                RA      = '13:29:24.00'         /  RIGHT ASCENSION                              DEC     = '47:15:34.00'         /  DECLINATION                                  EPOCH   =                 0.00  /  EPOCH OF RA AND DEC                          ZD      = '22:14:00.00'         /  ZENITH DISTANCE                              UT      = ' 9:27:27.00'         /  UNIVERSAL TIME                               ST      = '14:53:42.00'         /  SIDEREAL TIME                                CAM-ID  =                    1  /  CAMERA HEAD ID                               CAM-TEMP=              -106.22  /  CAMERA TEMPERATURE, DEG C                    DEW-TEMP=              -180.95  /  DEWAR TEMPRATURE, DEG C                      F1POS   =                    2  /  FILTER BOLT I POSITION                       F2POS   =                    0  /  FILTER BOLT II POSITION                      TVFILT  =                    0  /  TV FILTER                                    CMP-LAMP=                    0  /  COMPARISON LAMP                              TILT-POS=                    0  /  TILT POSITION                                BIAS-PIX=                    0  /                                               BI-FLAG =                    0  /  BIAS SUBTRACT FLAG                           BP-FLAG =                    0  /  BAD PIXEL FLAG                               CR-FLAG =                    0  /  BAD PIXEL FLAG                               DK-FLAG =                    0  /  DARK SUBTRACT FLAG                           FR-FLAG =                    0  /  FRINGE FLAG                                  FR-SCALE=                 0.00  /  FRINGE SCALING PARAMETER                     TRIM    = 'Apr 22 14:11 Trim image section is [3:510,3:510]'                    BT-FLAG = 'Apr 22 14:11 Overscan correction strip is [515:544,3:510]'           FF-FLAG = 'Apr 22 14:11 Flat field image is Flat1.imh with scale=183.9447'      CCDPROC = 'Apr 22 14:11 CCD processing done'                                    AIRMASS =    1.08015632629395   / AIRMASS                                       HISTORY 'KPNO-IRAF'                                                             HISTORY '24-04-87'                                                              HISTORY 'KPNO-IRAF'           /                                                 HISTORY '08-04-92'            /                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 END                                                                             

<class 'astropy.io.fits.header.Header'>


```
getheader veriyi bir ```fits.header``` olarak verir.


Bir FITS dosyasında başlıkların listesini almak için ise
```
from astropy.io import fits as fts

header = fts.getheader(r"[Dosya Yolu]")
print([card[0] for card in header.cards if card[0] != ""])
```
Çıktı:
```
['SIMPLE', 'BITPIX', 'NAXIS', 'NAXIS1', 'NAXIS2', 'EXTEND', 'ORIGIN', 'DATE', 'IRAF-TLM', 'OBJECT', 'IRAF-MAX', 'IRAF-MIN', 'CCDPICNO', 'ITIME', 'TTIME', 'OTIME', 'DATA-TYP', 'DATE-OBS', 'RA', 'DEC', 'EPOCH', 'ZD', 'UT', 'ST', 'CAM-ID', 'CAM-TEMP', 'DEW-TEMP', 'F1POS', 'F2POS', 'TVFILT', 'CMP-LAMP', 'TILT-POS', 'BIAS-PIX', 'BI-FLAG', 'BP-FLAG', 'CR-FLAG', 'DK-FLAG', 'FR-FLAG', 'FR-SCALE', 'TRIM', 'BT-FLAG', 'FF-FLAG', 'CCDPROC', 'AIRMASS', 'HISTORY', 'HISTORY', 'HISTORY', 'HISTORY']
```

### open
FITS dosyası açar. Dosyanın içeriğini bir obje olarak tutar. Dosyayı açma biçimine bağlı olarak güncellemeye izin 
verir.

```open``` ile dosyanın veri ve başlığına erişilebilir.

```
from astropy.io import fits as fts

hdu = fts.open(r"[Dosya Yolu]", "readonly")
print(type(hdu))

data = hdu[0].data
print(data)
print(type(data))


header = hdu[0].header
print(header)
print(type(header))

```
Çıktı:
```

<class 'astropy.io.fits.hdu.hdulist.HDUList'>

[[38 43 35 ... 45 43 41]
 [36 41 37 ... 42 41 39]
 [38 45 37 ... 42 35 43]
 ...
 [49 52 49 ... 41 35 39]
 [57 52 49 ... 40 41 43]
 [53 57 57 ... 39 35 45]]
<class 'numpy.ndarray'>
SIMPLE  =                    T / Fits standard                                  BITPIX  =                   16 / Bits per pixel                                 NAXIS   =                    2 / Number of axes                                 NAXIS1  =                  512 / Axis length                                    NAXIS2  =                  512 / Axis length                                    EXTEND  =                    F / File may contain extensions                    ORIGIN  = 'NOAO-IRAF FITS Image Kernel July 2003' / FITS file originator        DATE    = '2021-08-16T08:23:55' / Date FITS file was generated                  IRAF-TLM= '2021-08-16T08:23:55' / Time of last modification                     OBJECT  = 'm51  B  600s'       / Name of the object observed                    IRAF-MAX=           1.993600E4  /  DATA MAX                                     IRAF-MIN=          -1.000000E0  /  DATA MIN                                     CCDPICNO=                   53  /  ORIGINAL CCD PICTURE NUMBER                  ITIME   =                  600  /  REQUESTED INTEGRATION TIME (SECS)            TTIME   =                  600  /  TOTAL ELAPSED TIME (SECS)                    OTIME   =                  600  /  ACTUAL INTEGRATION TIME (SECS)               DATA-TYP= 'OBJECT (0)'          /  OBJECT,DARK,BIAS,ETC.                        DATE-OBS= '05/04/87'            /  DATE DD/MM/YY                                RA      = '13:29:24.00'         /  RIGHT ASCENSION                              DEC     = '47:15:34.00'         /  DECLINATION                                  EPOCH   =                 0.00  /  EPOCH OF RA AND DEC                          ZD      = '22:14:00.00'         /  ZENITH DISTANCE                              UT      = ' 9:27:27.00'         /  UNIVERSAL TIME                               ST      = '14:53:42.00'         /  SIDEREAL TIME                                CAM-ID  =                    1  /  CAMERA HEAD ID                               CAM-TEMP=              -106.22  /  CAMERA TEMPERATURE, DEG C                    DEW-TEMP=              -180.95  /  DEWAR TEMPRATURE, DEG C                      F1POS   =                    2  /  FILTER BOLT I POSITION                       F2POS   =                    0  /  FILTER BOLT II POSITION                      TVFILT  =                    0  /  TV FILTER                                    CMP-LAMP=                    0  /  COMPARISON LAMP                              TILT-POS=                    0  /  TILT POSITION                                BIAS-PIX=                    0  /                                               BI-FLAG =                    0  /  BIAS SUBTRACT FLAG                           BP-FLAG =                    0  /  BAD PIXEL FLAG                               CR-FLAG =                    0  /  BAD PIXEL FLAG                               DK-FLAG =                    0  /  DARK SUBTRACT FLAG                           FR-FLAG =                    0  /  FRINGE FLAG                                  FR-SCALE=                 0.00  /  FRINGE SCALING PARAMETER                     TRIM    = 'Apr 22 14:11 Trim image section is [3:510,3:510]'                    BT-FLAG = 'Apr 22 14:11 Overscan correction strip is [515:544,3:510]'           FF-FLAG = 'Apr 22 14:11 Flat field image is Flat1.imh with scale=183.9447'      CCDPROC = 'Apr 22 14:11 CCD processing done'                                    AIRMASS =    1.08015632629395   / AIRMASS                                       HISTORY 'KPNO-IRAF'                                                             HISTORY '24-04-87'                                                              HISTORY 'KPNO-IRAF'           /                                                 HISTORY '08-04-92'            /                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 END                                                                             

<class 'astropy.io.fits.header.Header'>

```

## İstatistik
Astropy bir FITS verisini ```numpy.ndarray``` tipinde sunduğu için istatistiki işlemlerde numpy'ın gücü kullanılabilir.
Bir verinin ortalaması, ortancası, standart satpması gibi değerlerine ulaşmak için ```numpy``` kullanılabilir.

```
from astropy.io import fits as fts
import numpy as np

hdu = fts.open(r"[Dosya Yolu]", "readonly")
data = hdu[0].data

average = np.mean(data)
median = np.median(data)
std = np.std(data)

print(f"{average=}, {median=}, {std=}")

```
Çıktı:
```
average=108.3154067993164, median=88.0, std=131.29777476298327
```
