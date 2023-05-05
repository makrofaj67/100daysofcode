def calculate(*args):
 toplam = 0
 for n in args:
  toplam = toplam + n
 print(toplam)
  
calculate(8,89,98,49,4,98)

def kalkulate(n, **kwargs):
 print(kwargs)
 print(kwargs["add"])
 print(kwargs["multiply"])
 for anahtar, deger in kwargs.items():
  print(anahtar)
  print(deger)
 
kalkulate(8, add=5, multiply = 8) #keyword argumentlerin değerini vermek zorundasın // n değerini pozisyonel olarak girmelisin


class Arabayapici:
 
 def __init__(self, **kwargs):
  self.marka = kwargs["marka"]
  self.model = kwargs["model"]
  
araba = Arabayapici(marka = "Nissan", model = "GT-R")

print(araba.model)
print(araba.marka)

class Arabayapici2:
 
 def __init__(self, **kwargs):
  self.marka = kwargs.get("marka")
  self.model = kwargs.get("model")
  self.yil = kwargs.get("yil")
  self.renk = kwargs.get("renk", "kırmızı")
araba2 = Arabayapici2(model = "tofaş", renk = "mavi")
print(araba2.model)
print(araba2.renk)