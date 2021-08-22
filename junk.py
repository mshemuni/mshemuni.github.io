import json


dct = {
    "personel_1": {
        "adi": "Mohammad",
        "soyadi": "Shameoni niaei",
        "Gelistirici": True,
        "TCKNO": None,
        "Uzmanlik": ["Yazilim Uzmani", "Uzman Astronom"]
    }
}

print(json.dumps(dct))
