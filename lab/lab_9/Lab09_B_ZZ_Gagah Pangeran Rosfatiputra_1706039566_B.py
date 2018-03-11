#Membuat fungsi angka cantik
def angka_cantik(angka):
    #base case saat angka berupa satuan
    if(angka < 10): return angka

    #kasus rekursi
    else: return angka_cantik((angka % 10) + angka_cantik(angka//10))

#Input sekaligus Output
print(angka_cantik(int(input(">>> "))))
