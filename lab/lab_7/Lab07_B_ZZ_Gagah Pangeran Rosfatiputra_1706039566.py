#Inisialisasi dictionari driver dan tipe ojek
driver = {}
tipe_ojek = {'NORMAL': (0,1000),
             'SPORT': (10,2500)}

#Fungsi untuk menjalankan perintah
def lakukan(cmd):
    #Fungsi untuk daftar
    if(cmd[0] == "DAFTAR"):
        if(cmd[1] not in driver): driver[cmd[1]] = BenJek(cmd[1],cmd[2]) #cek nama dan menjalankan perintah di init benjek
        else: print(cmd[1] + " gagal mendaftar sebagai driver BenJek")

    #Fungsi untuk mulai perjalanan
    elif(cmd[0] == "MULAI"):
        if(cmd[2] in driver): driver[cmd[2]].jalan(int(cmd[3]))     #Cek nama dan menjalankan method jalan di benjek
        else: print(cmd[2] + " tidak ada di dalam sistem")

    #Fungsi untuk cek pendapatan
    elif(cmd[0] == "CEK"):
        if(cmd[2] in driver): driver[cmd[2]].cek_pend()             #Cek nama dan menjalankan method cek_pend di benjek
        else: print(cmd[2] + " tidak ada di dalam sistem")

    #Fungsi untuk akhir bulan
    elif(cmd[0] == "AKHIR"):
        #menghitung pendapatan benjek
        pend_benjek = 0
        for i in driver.keys(): pend_benjek += driver[i].pendapatan
        pend_benjek = int(pend_benjek * 0.2)

        #print hasil dan pendapatan tiap driver
        print("Sudah akhir bulan! Pendapatan BenJek bulan ini adalah Rp." + str(pend_benjek))
        print("Daftar pendapatan pengemudi:")
        for i in driver.keys():
            driver[i].akhir_bulan()
    
class BenJek:
    #Mendaftarkan driver ke benjek
    def __init__(self,nama,tipe):
        self.nama = nama
        self.tipe = tipe
        self.pendapatan = 0
        self.minn, self.tarif = tipe_ojek[tipe]
        print(self.nama + " berhasil mendaftar sebagai driver BenJek layanan " + self.tipe)

    #Perjalan Benjek
    def jalan(self, jarak):
        self.jarak = jarak

        #Cek apakah jarak minimal bisa untuk perjalanan
        if(self.jarak >= self.minn):
            self.pendapatan += self.tarif * self.jarak
            print(self.nama + " melakukan perjalanan sejauh " + str(self.jarak) + " dan mendapatkan pendapatan sebesar " + str(int(self.tarif * self.jarak)))
        else:
            print(self.nama + " tidak bisa melakukan perjalanan")

    #Mengeluarkan pendapatan driver yang diminta
    def cek_pend(self):
        print(self.nama + " memiliki pendapatan sebesar Rp." + str(int(self.pendapatan)))

    #Mengeluarkan pendapatan tiap driver akhir bulan
    def akhir_bulan(self):
        print(self.nama + ":Rp." + str(int(self.pendapatan * 0.8)))

#Program utama
while True:
    perintah = input().split()          #Baca perintah
    lakukan(perintah)                   #Melakukan perintah
    if(perintah[0] == "AKHIR"): break   #Jika sudah akhir bulan, maka program berhenti
    
