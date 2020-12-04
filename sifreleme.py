class kök:
    def __init__(self,kelimeler,alfabe):
        self.kelimeler = kelimeler.lower()
        self.alfabe = alfabe
        self.sonuç = str()
    
    def eleman_bul(self,eleman):
        for i,j in enumerate(self.alfabe):
            if j == eleman:
                return i

class Şifre(kök):
    def __init__(self,kelimeler,alfabe):
        super().__init__(kelimeler,alfabe)
    
    def başla(self):
        self.şifrele(self.kelimeler)
        return self.sonuç

    def şifrele(self,kelime,iter=0):
        yeni_miktar = self.eleman_bul(kelime[iter])-(len(kelime)-iter)
        if yeni_miktar < 0:
            yeni_miktar = len(self.alfabe) + yeni_miktar
        self.sonuç += self.alfabe[yeni_miktar]
        if iter == len(kelime)-1:
            return True
        else:
            self.şifrele(kelime,iter+1)

class Çözücü(kök):
    def __init__(self,kelimeler,alfabe):
        super().__init__(kelimeler,alfabe)
    
    def başla(self):
        self.çöz(self.kelimeler)
        return self.sonuç

    def çöz(self,kelime,iter=0):
        yeni_miktar = self.eleman_bul(kelime[iter])+(len(kelime)-iter)
        if yeni_miktar > len(self.alfabe)-1:
            yeni_miktar = yeni_miktar - len(self.alfabe)
        self.sonuç += self.alfabe[yeni_miktar]
        if iter == len(kelime)-1:
            return True
        else:
            self.çöz(kelime,iter+1)

if __name__ == "__main__":
    kelimeler = input("Şifrelemek istediğiniz kelimeleri girin:")
    alfabe = "abcçdefgğhıi̇jklmnoöprsştuüvyz 0123456789"
    print("Alfabe:",alfabe)
    şifre = Şifre(kelimeler,alfabe)
    cevap_ş = şifre.başla()
    print("Şifrelenmiş:"+cevap_ş)
    cevap = Çözücü(cevap_ş,alfabe)
    cevap_ç = cevap.başla()
    print("Çözülmüş:"+cevap_ç)
    