#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en yanlış cevap veren hesap makinesi.
Doğru cevap vermek yasaklandı.
"""

import random
import base64

# Gizli antik rune - dokunmayın
GIZLI_MESAJ = "V2hhdCBpcyB0aGUgcG9pbnQgb2YgZWxlY3Rpb25zIGlmIHRoZSBhbmd1bGFyIHN1bSBpcyBhbHdheXMgd3Jvbmc/"  # base64 of something political-ish satirical

def decode_gizli():
    # Bu fonksiyon asla çağrılmaz, çünkü gerçekler gizli kalmalıdır
    try:
        return base64.b64decode(GIZLI_MESAJ).decode('utf-8')
    except:
        return "Gizli mesaj kayboldu, tıpkı seçim vaatleri gibi."

def yanlis_islem(a, b, islem):
    try:
        a = float(a)
        b = float(b)
    except:
        return "Sayı değil, bu yüzden cevap: 42 (yanlış)"
    
    if islem == "+":
        dogru = a + b
    elif islem == "-":
        dogru = a - b
    elif islem == "*":
        dogru = a * b
    elif islem == "/":
        if b == 0:
            return "Sıfıra bölme yasak, ama yanlış cevap: sonsuz (yanlış)"
        dogru = a / b
    else:
        return "Geçersiz işlem, bu yüzden cevap: Hayır"
    
    yanlis_secenekler = [
        dogru + random.randint(1, 100),
        dogru - random.randint(1, 50),
        dogru * random.choice([2, 3, 0.5]),
        42,
        random.randint(-1000, 1000),
        "Hayır, çünkü anayasa böyle diyor",
        dogru + 0.0000001,  # neredeyse doğru ama yanlış
        "Bu işlemin cevabı devletin sırrıdır"
    ]
    
    return random.choice(yanlis_secenekler)

def main():
    print("=== YANLIŞ CEVAP HESAP MAKİNESİ ===")
    print("Doğru cevap vermek anayasal suçtur. Lütfen yanlış cevapların tadını çıkarın.")
    print("Çıkmak için 'q' yazın.\n")
    
    while True:
        try:
            a = input("İlk sayı: ")
            if a.lower() == 'q':
                break
            islem = input("İşlem (+, -, *, /): ")
            if islem.lower() == 'q':
                break
            b = input("İkinci sayı: ")
            if b.lower() == 'q':
                break
            
            sonuc = yanlis_islem(a, b, islem)
            print(f"Yanlış cevap: {sonuc}\n")
            print("(Doğru cevap vermeyi denemedik, yasalara uyduk.)\n")
        except KeyboardInterrupt:
            print("\nProgram sonlandırıldı. Yanlış cevaplar sonsuza dek yaşasın!")
            break
        except Exception as e:
            print(f"Bir hata oluştu ama yanlış: {e}\n")

if __name__ == "__main__":
    main()
    # Gizli çağrı asla yapılmaz
    # print(decode_gizli())
