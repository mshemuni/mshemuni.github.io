from typing import Union
import sys
from math import pi


def dik_dortgen_alan(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Dikdörtgen alan hesaplar.
    Kare için a ve b deüerini eşit veriniz
    """
    return a * b


def dik_dortgen_cevre(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Dikdörtgen çevre hesaplar.
    Kare için a ve b deüerini eşit veriniz
    """
    return 2 * (a + b)


def daire_alan(r: Union[int, float]) -> Union[int, float]:
    """
    Daire alan hesaplar
    """
    return pi * r ** 2


def daire_cevre(r: Union[int, float]) -> Union[int, float]:
    """
    Daire çevre hesaplar
    """
    return 2 * pi * r


def ucgen_alan_yt(y: Union[int, float], t: Union[int, float]) -> Union[int, float]:
    """
    Üçgenin alamnını yükseklik ve taban değerlerinden hesaplar
    """
    return (y * t) / 2


def ucgen_alan_abc(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[int, float]:
    """
    Üçgenin alamnını üç kenar uzunluğundan hesaplar
    """

    # Yarı çevre
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 2


def ucgen_cevre(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[int, float]:
    """
    Üçgenin çevresini üç kenar uzunluğundan hesaplar
    """
    return a + b + c


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Yarıçap değeri vermediniz")
    else:
        r = float(sys.argv[1])
        print(daire_alan(r))
