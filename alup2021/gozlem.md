# Gözlem

## Işıkölçüm (Photometry) nedir?

**Işıkölçüm** bir astronomik nesnenin ışık akısı veya elektromanyetik radyasyonunun yoğunluğunun ölçülmesi ile ilgili bir astronomi tekniğidir.

## Gerekli tanımlar:

Işıkölçüm'de bir gök cisminin parlaklığındaki değişimin incelenmesi hedeflenir. Buradaki anahtar kelime *zamana bağlı parlaklık*'tır.

### Zaman:
Fizikte en hassas ölçülebilen nicelik zamandır. Zamanın ise faklı biçimleri vardır:

- Yerel zaman
- Evrensel zaman
- vs

Yerel zaman konuma bağlılık gösterir. Dolayısıyla gözlemin yapıldığı gözlemevinin konumu önem gösterir. 

Yerel zaman kullanarak yapılan gözlemlerde aynı gök cisminin faklı konum ve zamanlardaki gözlemlerini birleştirmek 
sorunlara neden olacağından, gözlemlerde genelde **Evrensel Zaman** kullanılır.

Eşgüdümlü Evrensel Zaman ya da özgün kısaltmasıyla UTC (Coordinated Universal Time), pek çok ülkede baz alınan bilimsel zamandır. 
Astronomide ise çoğunlukla UTC zaman biçiminde olan JD kullanılır.

Jülyen günü (**JD**), Jülyen tarih sisteminde yer alan ve astronomi topluluğu tarafından bilimsel çalışmalarda 
kullanılan bir zaman ölçüm sistemidir. Jülyen günü, MÖ 1 Ocak 4713 tarihi Pazartesi günü Evrensel zaman (UTC) ile öğle 
vaktinden itibaren bir günün zaman aralığını gün ve günün kesirleri halinde sunar.

2021-08-17 12:30:25 -> 2459444.02112

### Aydınlatma gücü:

Bir kaynağın birim zamanda, bütün dalga boylarında, bütün yüzeyinden yaydığı enerjiye Aydınlatma Gücü veya Işınım gücü denir.


$$
  L = 4 \pi r^2 \sigma T^4
$$

:::{note}
$L$ ışınım gücü, $r$ kaynağın yarıçapı, $\sigma$ Stefan–Boltzmann sabiti ve $T$ sıcaklık olmak üzere
:::

olarak ifade edilir.

### Akı:

Akı (Flux), bir kaynağın belirli bir uzaklığa, birim zamanda, birim yüzeyden yaydığı enerji miktarıdır.

$$
  F = \frac{L}{4 \pi R^2}
$$

:::{note}
$F$ akı, $L$ ışınım gücü ve $R$ uzaklık olmak üzere
:::

olarak ifade edilir.

### Parlaklık

Parlaklık, bir kaynağın (ürettiği ve/veya yansıttığı) ışığının görsel olarak algılanması ile oluşan bir niceliktir.

Astronomide parlaklık (Magnitude) bir oran cinsinden verilir. Dolayısıyla birimsiz olup kadir sistemiyle ifade edilir.

Kullanılan farklı parlaklık ölçümler:

- Görünür parlaklık
- Görsel parlaklık
- Mutlak parlaklık
- Aletsel parlaklık

#### Görünür parlaklık
Görünür parlaklık, bir kaynağın çıplak göz ile ölçülen parlaklığıdır. Bu parlaklık objenin ışınım gücüne ve uzaklığına 
bağlılık gösterir.

$$
m = -5 log(\frac{F}{F_0})
$$

:::{note}
$m$ görünür parlaklık, $F$ cismin akısı ve $F_0$ referans akı olmak üzere
:::

olarak ifade edilir.

#### Görsel parlaklık

Görsel parlaklık bir kaynağın elektromanyetik tayfın görsel bölgesinde (yaklaşık $0.4 - 0.7 \mu m$) yaydığı energinin 
neden olduğu parlaklıktır.

#### Mutlak parlaklık

Diğer parlaklık türlerine göre uzaklıktan bağımsız bir parlaklık değeridir.

Mutlak parlaklık, bir kaynağın 10 parsek uzaklıktaki görünür parlaklık değeridir. Dolayısıyla görünür parlaklığı ve 
uzaklığı bilinen bir kaynağın mutlak parlaklığı

$$
M = m + 5 log(\frac{1}{\pi})
$$

:::{note}
$M$ mutlak parlaklılk, $m$ görünür parlaklık ve $\pi$ paralaks olmak üzere
:::

olarak ifade edilir.

#### Aletsel parlaklık
Aletsel parlaklık bir kaynağın bir optik sistem (Teleskop, filtre, dedektör vb) ile ölçülen parlaklık değeridir.

:::{note}
Ders süresince Aletsel Parlaklık yerine sıkça *Parlaklık* terimini kullanacağız 
:::


## Gözlem

Bilimsel yöntemde veri elde etmenin iki yöntemi var.

1. Deney
2. Gözlem

Deney ve gözlem arasındaki en belirgin fark, deneyin kontrollü gözlemin ise kontrolsüz olmasıdır.

Bir deneyde ortamı ve ilerleyişi kontrol edebilirsiziniz, gözlemde ise gerçekleşe duran bir olayı takip edebiliriz.

Astronomik gözlemler bir çok yötem ile yapılabilir. Biz ise ışıkölçüm gözlemi ile ilgileniyoruz.

:::{note}
Ders süresince ışıkölçüm gözlemler yerine sıkça *gözlem* termini kullanacağız
:::

Bir gözlemde dikkat edilmesi gereken unsurlar:

1. Günün hava koşulları
2. Günün gözlem programı
3. Ekipmanın sağlığı

### Hava koşulları

Yer tabanlı gözlemevlerinde yaptığımız bütün gözlemlerin, atmosfer dediğimiz, opak bir katmanın içinden gerçekleştiğini 
unutmamamız gerek.

Gözlemin yapılacağı günde, gözlemevinin bulunduğu bölgenin hava koşulları hayati önem taşımaktadır. Söz konusu günün hava 
koşulları gözlem şeklini, gözlenecek objeleri ve gözlemin yapılıp yapılamayacağını belirler.


### Gözlem programı

Gözleme başlamadan önce gözlenecek objelerin ne olduğu bilinmeli.

Gözlem programı genelde bir tablo halinde sunulur ve aşağıdaki bilgileri barındırır:

- Obje adı
- Obje parlaklığı
- Objenin parlaklık değişimi
- Objenin parlaklık değişim periodu
- Objenin koordinatları
- Objenin söz konusu gün için doğma ve batma zamanları (Bazen gözlenebilirlik eğirisi olarak sunulabilir)
- Gözleme başlama zamanı
- Gözlemin yapılacağı filtre ve her filtre için poz süresi (Sönümleme kat sayıları bulunan gözlemevleri için)
- Gözlemin bitiş zamanı
- Gözlenecek objenin bir görüntüsü (Seçimli)

Yukarıdaki bilgiler gün içerisinde gözlenecek bütün objeler için ayrı ayrı verilir.

### Ekipmanın sağlığı
Gözleme başlamadan önce gözlemde kullanacağımız ekipmanların (Teleskop, dedektör, Filtre gibi) sağlığını kontrol etmeli, 
olumsuz bir durum ile karşılaşıldığında ise gözleme başlamadan teknik ekip bilgilendirilmeli.

### Kalibrasyon ölçümleri

Işıkölçüm gözlemlerinde, bilinen görüntü hatalarını düzeltmek için kalibrasyon verisi alınır. Bunlar:

- Bias (Sıfır düzey)
- Dark (Kara akım)
- Flat (Düz alan)

görüntüleridir.

