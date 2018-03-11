#Membuat fungsi kompresi
def kompresi(kata):
    #inisialisasi indeks awal
    indeks = -1

    #Base case saat hanya satu huruf
    if(len(kata) <= 1): return kata

    #Kasus rekursi
    else:
        #Mencari indeks akhir untuk replace huruf pertama
        for i in range(1,len(kata)):
            if(kata[i] != kata[0]):
                indeks = i
                break
            
        #Rekursi lagi setelah huruf pertama di replace
        return kata[0] + kompresi(kata.replace(kata[0],'',indeks))

#Input sekaligus Output
print("Hasil​ ​kompresinya​ ​adalah {}".format(kompresi(input(">>> "))))
