import hashlib
from datetime import datetime
from decimal import Decimal, InvalidOperation


def hash_sifre(sifre: str) -> str:
    return hashlib.sha256(sifre.encode()).hexdigest()


class BankaHesabi:
    
    def __init__(self, sahibi, sifre_hash, bakiye=Decimal("0"), aktif=True):
        self.sahibi = sahibi
        self.sifre_hash = sifre_hash
        self.bakiye = bakiye
        self.aktif = aktif

    def sifre_dogrula(self, sifre: str) -> bool:
        return self.sifre_hash == hash_sifre(sifre)

    def para_yatir(self, miktar: Decimal) -> bool:
        if not self.aktif or miktar <= 0:
            return False
        self.bakiye += miktar
        return True

    def para_cek(self, miktar: Decimal) -> bool:
        if not self.aktif or miktar <= 0 or miktar > self.bakiye:
            return False
        self.bakiye -= miktar
        return True

    def kapat(self):
        self.aktif = False


class Banka:

    def __init__(self):
        self.hesaplar = {}
        self.yukle()

    def yukle(self):
        try:
            with open("accounts.txt", "r", encoding="utf-8") as f:
                for satir in f:
                    ad, sifre, bakiye, durum = satir.strip().split(",")
                    self.hesaplar[ad] = BankaHesabi(
                        ad,
                        sifre,
                        Decimal(bakiye),
                        durum == "aktif"
                    )
        except FileNotFoundError:
            pass

    def kaydet(self):
        with open("accounts.txt", "w", encoding="utf-8") as f:
            for h in self.hesaplar.values():
                durum = "aktif" if h.aktif else "kapali"
                f.write(f"{h.sahibi},{h.sifre_hash},{h.bakiye},{durum}\n")

    def log(self, mesaj: str):
        with open("transactions.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - {mesaj}\n")

    def hesap_olustur(self, ad: str, sifre: str) -> bool:
        if ad in self.hesaplar:
            return False
        self.hesaplar[ad] = BankaHesabi(ad, hash_sifre(sifre))
        self.kaydet()
        return True

    def giris(self, ad: str, sifre: str):
        hesap = self.hesaplar.get(ad)
        if hesap and hesap.sifre_dogrula(sifre):
            return hesap
        return None


def decimal_input(mesaj: str) -> Decimal | None:
    
    try:
        return Decimal(input(mesaj))
    except (InvalidOperation, ValueError):
        return None


def hesap_menu(banka: Banka, hesap: BankaHesabi):
    while True:
        print(f"\nHoş geldiniz {hesap.sahibi}!")
        print("1- Para Yatır")
        print("2- Para Çek")
        print("3- Bakiye")
        print("4- Hesap Kapat")
        print("5- Çıkış")

        secim = input("Seçim: ")

        if secim == "1":
            miktar = decimal_input("Miktar: ")
            if miktar and hesap.para_yatir(miktar):
                banka.log(f"{hesap.sahibi} {miktar} TL yatırdı")
                banka.kaydet()
                print("İşlem başarılı! Yeni bakiyeniz:", hesap.bakiye, "TL")
            else:
                print("İşlem başarısız.")

        elif secim == "2":
            miktar = decimal_input("Miktar: ")
            if miktar and hesap.para_cek(miktar):
                banka.log(f"{hesap.sahibi} {miktar} TL çekti")
                banka.kaydet()
                print("İşlem başarılı! Kalan bakiyeniz:", hesap.bakiye, "TL")
            else:
                print("Yetersiz bakiye veya geçersiz miktar")

        elif secim == "3":
            print(f"Toplam bakiyeniz {hesap.bakiye} TL'dir.")

        elif secim == "4":
            hesap.kapat()
            banka.kaydet()
            print("Hesap başarıyla kapatıldı.")
            break

        elif secim == "5":
            break

        else:
            print("Geçersiz seçim!")


def main():
    banka = Banka()

    while True:
        print("\n1- Kayıt Ol")
        print("2- Giriş Yap")
        print("3- Çıkış")

        secim = input("Seçim: ")

        if secim == "1":
            ad = input("Kullanıcı adı: ")
            sifre = input("Şifre: ")
            if banka.hesap_olustur(ad, sifre):
                print("Hesabınız başarıyla oluşturuldu.")
            else:
                print("Bu kullanıcı zaten mevcut.")

        elif secim == "2":
            ad = input("Kullanıcı adı: ")
            sifre = input("Şifre: ")
            hesap = banka.giris(ad, sifre)
            if hesap:
                hesap_menu(banka, hesap)
            else:
                print("Hatalı giriş!")

        elif secim == "3":
            print("Program kapatıldı.")
            break

        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()
