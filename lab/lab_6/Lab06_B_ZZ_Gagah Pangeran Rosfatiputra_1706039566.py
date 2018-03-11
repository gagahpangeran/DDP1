#Fungsi untuk mengubah inputan menjadin set
def jadikan_set(belum_set):
    ini_set = set()     #Membuat set baru

    #Menghilangkan punctuation
    belum_set = belum_set.replace("{"," ")
    belum_set = belum_set.replace("}"," ")
    belum_set = belum_set.replace(","," ")

    #Mengubah isi element menjadi list
    masih_belum_set = belum_set.split()

    #Memasukkan isi list sebelumnya ke dalam set
    for i in masih_belum_set:
        ini_set.add(int(i)) #Mengubah isi element list menjadi integer

    #Mengembalikan isi set
    return ini_set

angka = int(input())    #Input angka
ini_list = []           #Menyiapkan list baru untuk mengisi set

for i in range(angka):
    bukan_set = input()                 #Membaca Input
    sudah_set = jadikan_set(bukan_set)  #Mengubah input menjadi set
    ini_list.append(sudah_set)          #Memasukkan list yang berisi set

jumlah = len(ini_list)  #Menghitung jumlah set dalam list
gabungan = set()        #Menyiapkan set untuk gabungan semua set

#Menggabungkan semua set
for i in ini_list:
    gabungan = gabungan | i

irisan = set()          #Menyiapkan set untuk gabungan irisan semua set

#Mencari irisan tiap set lalu menggabungkannya dalam satu set
for i in range(jumlah-1):
    for j in range(i+1,jumlah):
        irisan = irisan | (ini_list[i] & ini_list[j])

hasil = gabungan - irisan   #Menghapus element yang sama dalam set gabungan dan irisan


if(len(hasil) == 0): print('{}')    #Jika set kosong maka keluarkan {}
else: print(hasil)                  #Jika tidak kosong maka keluarkan set hasilnya
