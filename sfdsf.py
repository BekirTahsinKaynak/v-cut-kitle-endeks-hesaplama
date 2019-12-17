#3.Soru Cevap 

def hesaplama():
    kilo= float(input("Lütfen Kilonuzu Giriniz(Kg): "))
    boy =float(input("Lütfen Boyunuzu Giriniz(Cm): "))
    # vki = kg/m^2

    vki= kilo/ ((boy/100) * (boy/100))
    print ("Vücut Kitle İndeksiniz: ", vki)
    print ("Mevcut Durumunuz: ")

    if (vki<=20):
        print ("Zayıf")
    elif (20<vki<25):
        print ("Normal")
    elif (25<vki<30):
        print ("Hafif Kilolu")
    elif (30<vki<35):
        print ("Kilolu")
    else:
        print ("Obez")         

hesaplama()