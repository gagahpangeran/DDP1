import string

masukan = input("Masukkan operasi: ")
index_spasi = masukan.find(" ")         #Mencari letak spasi pertama
angka = int(masukan[0:index_spasi])     #Mendapatkan angka dalam masukkan
kata = masukan[index_spasi+1:]          #Mendapatkan kalimat enkripsi

alfabet = string.ascii_lowercase        #Inisialisasi daftar alfabet huruf kecil
hasil = ''                              #Inisialisasi variabel hasil untuk membuat kalimat yang asli

for i in kata:
    if(i != " "):                           #Memeriksa huruf dalam kalimat enkripsi selain spasi
        index = alfabet.find(i)             #Mencari index huruf
        geser = index - angka               #Menggeser index huruf yang di enkripsi
        if(geser < 0): geser = 26 + geser   #Jika hasil gesernya kurang dari nol, maka digeser dari belakang
        hasil = hasil + alfabet[geser]      #Merangkai kalimat yang di enkripsi huruf per huruf
        
    else:                                   #Kalau spasi maka tambahkan spasi di hasil
        hasil = hasil + " "

#Mencetak kalimat aslinya
print("Kalimat aslinya adalah:",hasil)


#Soal bonus
"""

masukan = input("Masukkan operasi: ")
index_spasi = masukan.find(" ") #Mencari letak spasi pertama
angka = int(masukan[0:index_spasi]) #Mendapatkan angka dalam masukkan
kata = masukan[index_spasi+1:] #Mendapatkan kalimat enkripsi

hasil = '' #Inisialisasi variabel hasil untuk membuat kalimat yang asli

for i in kata:
    #Memeriksa huruf dalam kalimat enkripsi selain spasi
    if(i != " "):
        index = ord(i) #Mencari index huruf
        geser = index - angka #Menggeser index huruf yang di enkripsi
        if(geser < ord("a")): geser = (ord("z")+1) - (ord("a") - geser) #Jika hasil gesernya sebelum huruf a, maka digeser dari belakang
        hasil = hasil + chr(geser) #Merangkai kalimat yang di enkripsi huruf per huruf
        
    #Kalau spasi maka tambahkan spasi di hasil
    else:
        hasil = hasil + " "

#Mencetak kalimat aslinya
print("Kalimat aslinya adalah:",hasil)



"""

