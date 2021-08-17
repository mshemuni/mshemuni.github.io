# Kurulum

ALÜP 2021 (Pyhton, IRAF ve MYRaf ile) açıklık fotometri çalıştayında kullanılcak yazılım ve kütüphane listesi:

## Python
Python kurulumunun anaconda ile yapılması tavsiye edilir.

Sisteminize uygun anaconda versiyonunu [anaconda individual*](https://www.anaconda.com/products/individual) 'dan 
indirip kurabilirsiniz.

:::{note}
Python'ı farklı kaynaklardan kuaracak katılımcıların dikkatine.

Lütfen python'ın 3. (python3.6 ve üstü) versiyonunu kurunuz.
:::

### IDE
IDE (Integrated Development Environment, Tümleşik Geliştirme Ortamı) herhangi bir programlama/betik dilinde kod yazarken 
renklendirme veya öneriler ile yardımcı olan bir yazılımdır.

Python için çok sayıda IDE bulabilirsiniz. Günümüzde en yaygın kullanılan Python IDE'ler arasında
- Pycharm 
- Visual Studio Code
- Spyder

yer almaktadır.

:::{note}
Katılımcının kullandığı IDE ile ilgili oluşabilecek sorunlar Uzman ve Teknik ekip tarafından çözülemeyebilir.
Dolayısıyla tecrübeli olduğunuz veya yaygın kullanılan IDE'leri tercih etmeniz rica olunur.
:::

### Python kütüphaneleri
ALÜP 2021 çalıştayında kullanılacak kütüphaneler:

- ```astropy```
- ```photutils```
- ```numpy```
- ```matplotlib```

#### astropy
[Astropy](https://www.astropy.org/), astronomların kullanımına sunulmuş, pyhton programa dili ile yazılmış, bir yazılımlar koleksyonudur.

```
pip install astropy
```

#### photutils
[photutils](https://photutils.readthedocs.io/en/stable/) Astropy’ın bağlı paketlerinden olup kaynak tesbiti ve photometry için kullanılır

```
pip install photutils
```

#### numpy
[numpy](https://numpy.org/), python'un bilimsel hesaplama paketi

```
pip install numpy
```

:::{note}
Astropy kurulurken bağımlılık olarak ```numpy``` da kurulur
:::

#### matplotlib
[matplotlib](https://matplotlib.org/), python'un görselleştirme kütüphanesi

```
pip install matplotlib
```

## IRAF
### GNU/Linux
Ubuntu dağıtımlarında ```iraf``` kurulumu basitçe ```apt``` ile gerçekleşebilir.
```
sudo apt install iraf saods9 xterm
```

### Windows
Windows işletim sisteminde IRAF kurulumu için WSL (Windows Subsystem for Linux) kurulumu yapmanız gerek.

Bunun için lütfen [bu](https://docs.microsoft.com/en-us/windows/wsl/install-win10) bağlantıdaki yönergeleri takip ediniz.

Daha sonra Microsoft Store'dan ubuntu kurulumunu gerçekleştiriniz.

Ubuntu uygulamasını çalıştırıp açılan terminalde

```
sudo apt install iraf saods9 xterm
```

komutunu çalıştırınız.

Bu aşamada teorik olarak iraf kurulumu tamamlanmış durumda. Fakat Windows'da IRAF'ı kullanabilmel için xserver kurulumu 
yapmalısınız.

[Bu](https://sourceforge.net/projects/xming/) adresten xming kurulum dosyasını indirip kurduktan sonra 
```Xming Server```'ı çalıştırın.

Son olarak windows'ta açtığınız ubuntu terminalde 

```
export DISPLAY=$(route.exe print | grep 0.0.0.0 | head -1 | awk '{print $4}'):0.0
```

komutunu çalıştırınız.

:::{note}
Terminal her kapanıp açıldığında yukarıdaki komutu tekrarlamanız gerek.

Bu durumu önlemek adına yukarıdaki satırı ```.bashrc``` dosyasına yazınız

:::
