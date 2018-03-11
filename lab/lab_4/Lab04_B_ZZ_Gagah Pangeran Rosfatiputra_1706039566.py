file = input("Masukkan nama file input dan output: ")

#Mencoba membuka file
try:
    file_in = open(file.split()[0],"r")     #membuka file
    file_out = open(file.split()[1],"w")    #menulis file

    for kalimat in file_in: kata = kalimat  #mendapatkan string dari text

    #inisialisasi variabel awal
    i1 = 0 #index awal untuk index <start>
    i2 = 0 #index awal untuk index <end>
    hasil = "" #variabel hasil untuk menampung kata yang akan dicari
    index_start = 0 #inisialisasi index <start>
    index_end = 0   #inisialisasi index <end>

    #melakukan pencarian kata
    while(True):
        index_start = kata.find("<start>",i1) #mencari index awal dari <start>
        index_end = kata.find("<end>",i2)     #mencari index awal dari <end>
        if(index_start == -1): break          #jika sudah tidak ditemukan lagi, maka pencarian berhenti
        hasil = hasil + kata[index_start+7:index_end].strip() + " "  #melakukan slicing kata di antara <start> dan <end>, lalu ditambahkan ke variabel hasil
        i1 = index_start + 1    #update index awal untuk mencari indek <start>
        i2 = index_end + 1      #update index awal untuk mencari indek <end>

    print(hasil, file=file_out) #menulis di file output
    print("Rahasia telah terbongkar, silakan cek file", file.split()[1]) #memberitahu kalau sudah berhasil

    #tutup file
    file_in.close()
    file_out.close()

#Jika terjadi error, print bermasalah
except:
    print("File " + file.split()[0] + " bermasalah! Benny lolos kali ini.") #memberitahu kalau bermasalah
