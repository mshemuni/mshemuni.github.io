# Giriş
Tembeller için programlama (TİP), anlaşılabilir problemler ile python kodlama öğretmeyi hedefler.

TİP bir yaşam biçimi, bir felsefedir. 

:::{tip}
15 dakikada yapabileceğiniz bir işi otomatikleştirmek için 45 dakika mı harcıyorsunuz? **Siz bir TİPsiniz**.
:::

## Bilgisayar nedir?
Bilgisayar, kendisine komuta edilmiş aritmetik ya da mantıksal işlemleri yapabilen bir makinedir.

Bilgisayar'ı tam olarak anlamak için donanım ve yazılımın ne olduğunu anlamak gerek.

### Donanım
Bilgisayarı oluşturan fiziksel parçaların tamamıdır. Bunlara 
- işlemci
- hafıza 
- veri depolama birimleri
- ekran 
- fare
- klavye 

örnek olabilir.

### Yazılım
Donanım ile insan arasında kalan tercüman olarak algılanabilir.

Örneğin, depolama birimi olan hard disk'te bir bilgiyi depolamak isterseniz, bu bilginin büyüklüğü, içeriği, türü vb. 
özelliklerini bilmeniz, daha sonra hard disk üzerindeki boş olarak işaretlenmiş sektörleri tespit edip söz konusu 
bilgiyi o sektörlere yazdıktan sonra, kaydetmiş olduğunuz bilginin hangi sektörlere yayıldığını bildiren index 
bilgisini girmeniz gerek.

Bu işlemleri, işlemciye yaptırmak ```talimat```lar ile gerçekleşir. Bu talimatlar ise Makine Dili (Machine Code) ile 
verilir.

Makine dili şuna benzer:


```{tabbed} Binary
001000 00001 00010 0000000101011110
```

```{tabbed} Hexadecimal
080102015E
```
Gördüğünüz değerler işlemciye ```bir şeyler``` yaptırıyor. Fakat gördüğünüzden de anlaşılacağı üzere bizim bunu bir bakışta 
(2. bakıştan da pek emin değilim) anlamamız pek olası değildir. Bu talimatların daha anlaşılabilir olması  adına 
```Tercüman```lar kullanırız. Bu tercümanlar, insan dilini, makine diline dönüştürür. Bunlar ```Kabuklar```, 
```Betik/Programlama dilleri```'dir.


## Kullanıcı ile Donanım arasındaki haberleşme

Bir kullanıcı donanıma bir şeyler yaptırmak istediğinde bunu çok farklı şekillerde yapabilir. Anlaşılabilir olması için 
örnekle açıklayalım.

Kullanıcı ```a``` adlı dosyayı ```b``` olarak yeniden adlandırmak istiyor. Bunun için nasıl yollar izlenebilir?

1. Makine dili ile, ```a``` dosyasının diskte bulunduğu bölgeyi okuyup... Yok ya anlatırken sıkıldım. Geç!
2. İşletim sisteminde bulunan yeniden adlandırma işi yapabilen programa başvurabiliriz. ```ren``` veya ```mv```.
   Bunun için terminal açıp ```mv a b``` yazarız. Yeniden adlandırma işlemi tamamlanmış olur.
   Fena değil. Ama ben tembelim. Daha kolayı?
3. Arayüzden dosyaya sağ tıkla, açılan menüden ```yeniden adlandır```'a tıkla. Dosya adını yaz <kbd>enter</kbd>'a bas. 
   Daha iyi.
4. ```Python``` terminali aç. ```shutil``` kütüphanesini içe aktar. ```copyfile``` metodunu kullanarak, kaynak ve 
   hedef yolları sağla. Kodu çalıştır.
   ```{image} ../images/WAT.jpg
   :alt: wat
   :class: bg-primary mb-1
   :width: 400px
   :align: center
   ```

Dördü geç!

İkinci adımda bir program kullandık. O program, işletim sistemi çekirdeğine yeniden adlandırma işlemini bildirdi. 
İşletim sistemi çekirdeği ise donanımla konuşup işi yaptı.

Üçüncü adımda ise yeniden adlandırma yapan program ile kullanıcı arasına bir arayüz yerleştirdik. İşi daha da 
kolaylaştırdık. 

Peki, biz yeniden adlandırma kodunu kendimiz yazsaydık ne olurdu? Kodu hangi dilde yazdığımıza bağlı olarak değişir ama 
aşağı yukarı ayni şeyler gerçekleşir.

Kod ile donanım arasındaki haberleşme {numref}`code_hardware_communication`'de verilmiştir.

```{figure} ../images/code_hardware_communication.png
---
height: 500px
name: code_hardware_communication
---
Kod ile donanım iletişimi
```

## Kod
Kod neydi? Kod iyilikti, dostluktu, kod emekti. Başlarsam bir daha kurtulamam...

Kod, bir programlama veya betik (script) dili için hazırlanmış, talimatlar (metin) dizisidir. Söz konusu metin 
(ki bu metin yazılışı itibariyle insan diline daha yakındır) derleyici veya yorumlayıcı yardımıyla işleme dönüşür.

Peki, nedir programlama veya betik dili? Prensipte benzer işleri yaparlar fakat art alanda çok farklı yollar izlerler.

### Dil seviyesi
Programlamada dil seviyesi diye bir kavram vardır. Bir programlama veya betik dilinin seviyesi insan diline 
yakınlığıyla (ve diğer parametrelerle) ölçülür.

- Yüksek seviye bir dil: İnsan diline daha yakın
- Düşük seviye bir dil: Makine diline daha yakın

anlamına gelir.

Seviyelerin bir rankı yoktur. Göreli olarak ifade edilir. Örneğin: 
```Python, C++'a göre daha yüksek seviye bir dildir.```



### Programlama dili
Bir programlama dili aslında bir derleyicidir. Bu derleyicinin yazım kuralları vardır. 
İçinde barındırdığı araçlar vardır.

Çalışma şekli ise şöyledir:

1. Size dikte edilen yazım kurallarına sadık kalarak bir takım talimatlar yazarsınız.
2. Yazdığınız talimatları bir yalın metin (txt gibi) belgesine kaydedersiniz.
3. Derleyiciye bu metin belgesini verirsiniz.

Derleyici ise metni okur, hata görmez ise, size çalıştırabileceğiniz bir dosya sunar. O dosyayı kullanarak talimat 
listesinde verdiğiniz işlemleri makineye yaptırabileceksiniz.

Derleyiciye verdiğiniz metin ```kaynak kod``` (```source code```), ortaya çıkan çalıştırılabilir dosya ise 
```program```'dır.

Buradaki anahtar kelime derlemek ve derlemenin sonucunda çalıştırılabilir dosyanın oluşmasıdır.

Derlediğiniz kodun çıktısı olan program işletim sistemi çekirdeği ile konuşur. Dolayısıyla bu programı başkasıyla 
paylaşırsanız insanlara yardımcı olabilirsiniz.

:::{note} 
Kodu hangi işletim sisteminde derlediyseniz, oluşan program söz konusu işletim sisteminde çalışır.

Windows'da derledim, Linux'ta çalışmadı. E, çalışmaz tabii.
:::

Programınızı kullanacak insanların derleyiciye ihtiyacı olmaz. Programı çalıştırır.

### Betik dili
Betik dili bir yorumlayıcıdır. Programlama dilinde olduğu gibi betik dilinde de yazım kuralları ve içinde 
barındırdığı araçlar vardır.

Çalıştırma şekli ise şöyledir:
1. Size dikte edilen yazım kurallarına sadık kalarak bir takım talimatlar yazarsınız.
2. Yazdığınız talimatları bir yalın metin (txt gibi) belgesine kaydedersiniz.
3. Yorumlayıcıya bu metin belgesini verirsiniz.

Yorumlayıcı ise bu işlemleri sırasıyla gerçekleştirir.

Farkı hissettiniz mi? Çalıştırılabilir dosya oluşmadı. Talimatlar direkt gerçekleşti.

:::{note} 
Betik dili derleme yapmaz demek doğru olmayabilir. Derleme işlemi ve çalıştırma işlemini aynı anda yapar...
:::

Betik dillerinde program dosyası oluşmaz. Eğer yazdığınızı biriyle paylaşmak isterseniz, kaynak kodu paylaşmanız 
gerekecek.

Herkes ne kadar berbat kod yazdığınızı görecek.
```{image} ../images/oh_god_please_no.gif
:class: bg-primary mb-1
:width: 400px
:align: center
```

Ayrıca yazdığınız kodun yorumlanması için yorumlayıcıya gerek var. Python'da yazdığınız kodu başkası çalıştıracaksa, 
Python'ı kurması gerekiyor.

### Betik VS Programlama
Haydi, programlama ve betiği karşılaştıralım. Bu sırada puan da verelim.

1. **Round**:
   Programlama dilinde kaynak kodu gizleyebilirsiniz. Böylece insanlar yazdığınız şiirimsi içerikten mahrum kalabilir. 
   Betik dilinde kaynağı paylaşmak zorundasınız.(Buradan kimseye puan çıkmaz)
   
   Programlama: $0$
   
   Betik: $0$
2. **Round**:
   Programlama dilinde oluşturduğunuz programı paylaşırsınız. Tek başına çalışır.
   Betik dilinde kodu paylaşırsınız ve yorumlayıcıya ihtiyaç duyulur.
   
   Programlama: $1$
   
   Betik: $0$

3. **Round**: 
   Programlama dilinde direkt işletim sistemi çekirdeği ile muhatap olduğunuzdan teoride, betik diline göre çok daha 
   hızlıdır.

   Programlama: $2$
   
   Betik: $0$
4. **Round**: 
   Programlama dilleri bir defa derlenir, sonra defalarca çalıştırılabilir.
   Betik dillerinde her çalıştırmada kod yorumlanmak zorunda.
   
   Programlama: $3$
   
   Betik: $0$
5. **Round**: 
   Programlama dilleri donanımın tüm kaynaklarından yararlanabilir, betik dillerinde ise bu kaynaklar çok 
   daha kısıtlıdır.
   
   Programlama: $4$
   
   Betik: $0$
6. **Round**: Programlama dillerinin kullanımı daha zordur ve maliyeti daha fazladır. Betik dillerinde ise kullanım 
   daha kolay ve maliyeti daha azdır.
   
   Programlama: $4$
   
   Betik: $65535$

   ```{image} ../images/one_billion_point.png
   :class: bg-primary mb-1
   :width: 400px
   :align: center
   ```

## Python
Aslında yaptığımız tanımlara göre Python bir betik olmalı. Fakat, prensipte Python bir programlama dilidir. 

Biz yine de betikmiş gibi davranacağız.

Python, nesne yönelimli, yorumlamalı, birimsel (modüler) ve etkileşimli yüksek seviyeli bir programlama dilidir. 
[Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))

Python kodu yalın metinde tutulur. Fakat dosya uzantısı olarak ```py``` kullanılır. 


Buraya kadar geldiyseniz sizi tebrik ederim.
