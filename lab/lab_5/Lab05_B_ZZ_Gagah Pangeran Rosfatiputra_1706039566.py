#Fungsi cetak pertanyaan
def cetak_pertanyaan(urutan, angka_biner):
    print("Soal "+str(urutan)+": Berapakah angka desimal dari bilangan biner "+angka_biner+"?")

#Fungsi cek jawaban  
def cek_jawaban(jawaban, angka_biner):
    if(int(angka_biner, 2) == jawaban): return 25
    else: return 0

#Fungsi utama 
def main():
    print("Selamat datang di Mini Kuis DDP-1: Sistem Bilangan!")
    soal1 = "11111100001"
    soal2 = "11111001111"
    soal3 = "10001100"
    soal4 = "100011101"
    counter_soal = 1
    skor = 0
    while counter_soal <= 4:
        #Cek urutan soal
        if(counter_soal == 1): soal = soal1
        elif(counter_soal == 2): soal = soal2
        elif(counter_soal == 3): soal = soal3
        elif(counter_soal == 4): soal = soal4

        # di sini cetak pertanyaan sesuai dgn counter soal dan angka biner untuk counter tsb
        cetak_pertanyaan(counter_soal,soal)

        # di sini minta input jawaban, format output: “Jawab: (di sini input dimasukkan)”

        jawab = int(input("Jawab: "))

        # di sini cek apakah jawabannya benar
        skor += cek_jawaban(jawab,soal)

        # counter soal bertambah
        counter_soal += 1

    #cetak skor akhir disini, format output: “Skor akhir: <skor>
    print("Skor akhir:", skor)    

if __name__ == '__main__':
    main()


#Soal Bonus
'''
#Fungsi cetak pertanyaan
def cetak_pertanyaan(urutan, angka_biner):
    print("Soal "+str(urutan)+": Berapakah angka desimal dari bilangan biner "+angka_biner+"?")

#Fungsi cek jawaban  
def cek_jawaban(jawaban, angka_biner):
    if(int(angka_biner, 2) == jawaban): return 25
    else: return 0

#Fungsi utama 
def main():
    print("Selamat datang di Mini Kuis DDP-1: Sistem Bilangan!")
    soal = input("Masukkan 4 soal: ").split()
    counter_soal = 1
    skor = 0
    while counter_soal <= 4:
        # di sini cetak pertanyaan sesuai dgn counter soal dan angka biner untuk counter tsb
        cetak_pertanyaan(counter_soal,soal[counter_soal-1])

        # di sini minta input jawaban, format output: “Jawab: (di sini input dimasukkan)”

        jawab = int(input("Jawab: "))

        # di sini cek apakah jawabannya benar
        skor += cek_jawaban(jawab,soal[counter_soal-1])

        # counter soal bertambah
        counter_soal += 1

    #cetak skor akhir disini, format output: “Skor akhir: <skor>
    print("Skor akhir:", skor) 

if __name__ == '__main__':
    main()
'''
