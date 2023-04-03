import random
random.seed()   #Prepare random number generator

olasilik = 0
tura = 0
yazi = 0
print("Deneme sayısını giriniz")
denemeSayisi = int(input())
for i in range(1, denemeSayisi + 1, 1):
    gelen = int(random.random() * 2)
    if gelen == 0:
        yazi = yazi + 1
    else:
        tura = tura + 1
print("gelen yazı adedi:" + str(yazi))
olasilik = float(yazi) / denemeSayisi
print("Yazı gelme olasılığı" + str(olasilik))
print("gelen tura adedi:" + str(tura))
print("Tura gelme olasılığı" + str(1 - olasilik))
