# Python Kalibrasyon
Astronomide algılayıcılar zamanda değişim göstermiş durumdadır. Günümüze kadar kullanılan algılayıcıları kabaca 
listelemek gerekirse:

- Göz
- Fotoğraf Plağı
- Fotokatlandırıcı
- CMOS/CCD

## Göz
En az hassasiyete sahip olan göz ile yapılmış gözlemler, bir gözlemcinin gök yüzünde gördüğü kaynakların bir birine 
göre parlaklığını (Göz kararınca demek yanlış olmaz) kaydetmesinden ibarettir. 

En düşük hassasiyete sahip bu tür gözlemler, öznel olup gözlemi yapan kişiye bağlılık gösterir. Kayıt esnasına 
gerçekleşebilecek hataların düzeltilmesi olası değildir.

Ayrıca göz logaritmik bir dedektördür. Dolayısıyla akıda oluşan değişime logaritmik olarak yant verir. Yani, eğer akıda 
2 kat değişim olursa gözlemcinin kaydedeceği değer iki katına çıkmaz.


## Fotoğraf plağı
Bu tür gözlemlerde, teleskobun odak düzlemine yerleştirilen ışıkduyar bir düzlem ile ifade edilebilir. Söz konusu 
düzleme gözlem esnasında düşen ışık plaka üzerinde kimyasal reaksyona neden olur ve böylece kayıt altına alınır.

Avantajlar:
- Kişiden bağımsızdır
- Tekrar incelenebilir
- Gözlenen ve çevresindeki kaynakları kaydeder

Dezavantajları:
- Kuantum etkinliği azdır (Üzerine düşen ışığın küçük bir kısmına yanıt verir)
- Kayıtlı veri zamanla aşınabilir
- Görüntüyü işlemek için ayrı ekipmanlar gerekir
- Teorik olarak tekrar kullanılamaz
- Pahalıdır

## Fotokatlandırıcı
Foto katlandırıcılar, üzerine düşen ışığı elektrik potansiyeline çeviren cihazlardır. Böylece bir kaynağın akısını Volt 
cinsinden kaydetmek mümkün olacağından, yeterli bilgi ile Volt değeri ADU'ya (Analog-to-Digital Unit) çevrilebilir. 
Böylece sayısal ortamda (Bilgisayarda) işlenebilir.

Avantajlar:
- Kişiden bağımsızdır
- Tekrar incelenebilir
- Tekrar kullanılabilir
- Kuantum etkinliği yüksektir (Üzerine düşen ışığın büyük bir kısmına yanıt verir)
- Ucuzdur

Dezavantajları:
- yalnızca gözlenen cismin akısını kaydeder

## CMOS/CCD
Bu cihazları, bir fotokatlandırıcı dizisi olarak algılayabiliriz. n satır ve m sütundan oluşan bir CCD $n x m$ 
piksele sahip olup, çıktı olarak sayısal görüntü verir.

Avantajlar:
- Kişiden bağımsızdır
- Tekrar incelenebilir
- Tekrar kullanılabilir
- Kuantum etkinliği yüksektir (Üzerine düşen ışığın büyük bir kısmına yanıt verir)
- Gözlenen ve çevresindeki kaynakları kaydeder

Dezavantajları:
- Pahalıdır

Günümüz gözlemlerinde çoğunlukla CCD kullanılır. Bazı durumlarda CMOS kullanıldığı da görülür.

## CCD
CCD bir dizi pikselden oluşan, üzerine düşen ışığı elektrik potansiyeli olarak tutan ve gerektiğinde bu değeri okuyup ADU 
birimine çeviren bir cihazdır.

Bir CCD'nin aslında $n x m$'lik bir fotokatlandırıcı dizi gibi davrandığından bahsetmiştik. Dolayısıyla her bir piksel 
tekil olup diğer piksellere göre farklı davranabilir.

Bu nedenle  CCD'nin bilinen hataları vardır.

- Bias
- Dark
- Flat

### Bias
CCD'nin her pikseli bir potansiyel çukur gibi davranır. Ölçüme (Pozlamaya) başlamadan önce bu potansiyel çukurun 
taşıdığı elektronlar vardır. Bu elektronlar daha sonra sayısal görüntü üzerinde ek olarak görülmektedir.

Bir CCD'nin Bias seviyesini ölçmek için, $0$ saniyede (olabilecek en kısa süre) CCD'nin bütün piksellerinin değerleri 
okunur. Oluşan bu verinin bütün sayısal verilerde var olduğu kabul edilir. Dolayısıyla Bütün verilerden Bias değeri 
çıkartılır.

Bias, sıfır düzey hatası olarak da bilinir.

### Dark
CCD ışıkduyar bir yüzey olup fotoelektronların ADU'ya dönüştürerek görüntü oluşturur. Fakat pozlama esnasında 
fotoelektronların yanında termoelektronlar da oluşur. Kısacası pozlama süresince ısıdan dolayı kopan elektronlar da 
ADU'ya dönüştürülür. Bu hatayı gidermek adına kameranın önü kapalıyken, sayısal görüntünün pozlandığı sürece, bir 
görüntü pozlanır. Böylece oluşan görüntünün içinde, Bias ve termoelektronlar bulunmuş olur.

Bu veri sayısal verilerden Flat ve Bilimsel görüntülerde bulunur ve çıkarılması gerek.

Yeterince (<$-100 {}^o C$) soğutulan CCD'lerde Dark ihmal edilebilir.

Dark, kara akım hatası olarak da bilinir.

### Flat
CCD'nin her pikselinin bir fotokatlandırıcı gibi davrandığından defaatle bahsettik. Bu durum, her pikselin, aynı ışık 
miktarına faklı yanıt vermesine neden olabilir.

Ayrıca optik kararsızlık, görüntünün merkezinin daha aydınlık, kenarlarının ise daha karanlık olmasına neden olurken, 
filtre ve/veya ayna üzerindeki kir görüntü bozulmasına neden olabilir. Bütün bu hataları gidermek için Flat kullanılır.

Flat yalnızca Bilimsel görüntüde bulunur ve bölme işlemiyle normalize edilir.

Flat, düz alan hatası olarak da bilinir.

Kalibre edilmiş bilimsel görüntü

$$
K = \frac{(G - B) - (D - B)}{(F - B) - (D - B)}
$$

:::{note}
$K$ Kalibre edilmiş görüntü, $G$ ham bilimsel görüntü, $F$ flat görüntü, $D$ dark görüntü ve $B$ bias görüntü olmak üzere
:::

olarak hesaplanır.
