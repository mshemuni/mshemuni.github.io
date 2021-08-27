# Hazırlık
Python'da kod yazmak veya yazılmış bir kodu çalıştırmak isterseniz, Python'ı kurmanız gerekiyor.

## Resmi Python

Python'ı [resmi web sayfasından](https://www.python.org/) tam olarak 0&#x20BA;'ye indirip kurabilirsiniz. İndirimlerden haberdar olmak için 
Python'ın resmi web sayfasına abone olmayı unutmayınız.

```{image} ../images/hahaha.png
:class: bg-primary mb-1
:width: 400px
:align: center
```
<hr>

Python'ın farklı versiyonları vardır. Bu metni yazdığımda kararlı en güncel versiyon ```3.10``` olmalı. Fakat biz daha
geriden gelerek işimizi garantiye alacağız. Dolayısıyla ```3.9``` versiyonunu kullanacağız.

```{image} ../images/python_official.png
:alt: Python resmi web sayfası
:class: bg-primary mb-1
:width: 400px
:align: center
```

### Kurulum
Python'ı indirdik. Şimdi bir ritüel olan ``çif tıkla->next->next->next...`` yapacağımızı sanıyorsanız yanılıyorsunuz.
Okuyup anlayacağız...

```{image} ../images/official_python_installation/1.png
:alt: Python kurulum 1
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{image} ../images/official_python_installation/2.png
:alt: Python kurulum 2
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{image} ../images/official_python_installation/3.png
:alt: Python kurulum 3
:class: bg-primary mb-1
:width: 400px
:align: center
```

Kuruldu ya la...

## Anaconda Python
Biz TİPlerin tembelliği ve tembellikten doğan fazla mesaimizi bildiğim için, size daha mantıklı bir python ortamı 
tavsiye edeceğim.

Python'ın anaconda versiyonunu kuracağız. Bunun için Anaconda'nın 
[individual edition](https://www.anaconda.com/products/individual) 'ını kuracağız.

### Kurulum

indirme işlemi bitince kurulum işlemi yapacağız ve sizi temin ederim ``çif tıkla->next->next->next...`` olmayacak.

```{image} ../images/anaconda_python_installation/1.png
:alt: Anaconda kurulum 1
:class: bg-primary mb-1
:width: 400px
:align: center
```
İlk pencere merhaba penceresidir. 

```{image} ../images/anaconda_python_installation/2.png
:alt: Anaconda kurulum 2
:class: bg-primary mb-1
:width: 400px
:align: center
```
İkinci pencere lisans ve sözleşme penceresidir. 

```{image} ../images/anaconda_python_installation/3.png
:alt: Anaconda kurulum 3
:class: bg-primary mb-1
:width: 400px
:align: center
```
Üçüncü pencere kurulumu sistem genelinde mi yoksa kullanıcıya mı yapılacağını sorar. Yalnızca kullanıcıya kurulum 
yapmanız tavsiye edilir.

```{image} ../images/anaconda_python_installation/4.png
:alt: Anaconda kurulum 4
:class: bg-primary mb-1
:width: 400px
:align: center
```
Dördüncü pencere kurulumu nereye yapacağını sorar. Kullanıcı dizininde olması tavsiye edilir.

```{image} ../images/anaconda_python_installation/5.png
:alt: Anaconda kurulum 5
:class: bg-primary mb-1
:width: 400px
:align: center
```
Beşinci pencere Python'ın sistem yoluna eklemek isteyip istemediğinizi sorar. Bence istemeyin.

```{image} ../images/anaconda_python_installation/6.png
:alt: Anaconda kurulum 6
:class: bg-primary mb-1
:width: 400px
:align: center
```
Bu pencerede kahve alın.

```{image} ../images/anaconda_python_installation/7.png
:alt: Anaconda kurulum 7
:class: bg-primary mb-1
:width: 400px
:align: center
```
Bu pencerede güle güle penceresidir.

```{image} ../images/anaconda_python_installation/8.png
:alt: Anaconda kurulum 18
:class: bg-primary mb-1
:width: 400px
:align: center
```
"Giderayak sitemize girmek ister misin?" penceresi.

Gördünüz mü? Ne kadar kolay.

## Neden Anaconda?

Tipik bir TİP'in kurulumu daha kolay olan resmi Python'ı kurmak yerine neden Anaconda'yı tercih edeceğini merak 
ediyorsunuz değil mi?

Zira ileride anaconda hayatımızı acayip kolaylaştıracak.

## Deneme
Bakalım Python çalışıyor mu?

```{image} ../images/conda_on_start_menu.png
:alt: Anaconda başlat menüsü
:class: bg-primary mb-1
:width: 400px
:align: center
```

Başlat menüsünden anaconda alt menüsü açarak ```Anaconda Prompt```'a tıklayınız.

```{image} ../images/conda_terminal.png
:alt: Anaconda terminal
:class: bg-primary mb-1
:width: 400px
:align: center
```

Tebrikler. Artık aşırı gelişmiş bir hesap makineniz var.

## IDE
Python ile terminalde işlemler yapabilirsiniz. Hatta sırf bunun için geliştirilmiş ortamlar bile var. ```ipython``` gibi. 
Lakin bizim bir geliştirme ortamına ihtiyacımız olacak.

Bunun için IDE(Integrated Development Environment: Tümleşik Geliştirme Ortamı) kullanacağız. IDE'ler Steroid almış 
metin düzenleyicileridir. Hedeflendikleri dillerde yazılım geliştiricisine, kodun farklı bölgelerini renklendirerek, 
gerektiğinde "Hop aga. Yanlışın var." diyerek yardımcı olurlar.
