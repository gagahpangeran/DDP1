#Class staff untuk instansiasi objek
class Staff:
    #Mendefinisikan nama dan atribut awal
    def __init__(self, nama):
        self.nama = nama    #Nama staf
        self.jam_kerja = 0  #Jumlah jam kerja awal
        self.progress = 0   #Jumlah progress awal

    #Menambahkan jumlah jam kerja staf  
    def kerja(self, jam):
        self.jam_kerja += jam

    #Method untuk hitung gaji
    def hitung_gaji(self):
        pass    


#Class untuk staf acara
class StaffAcara(Staff):
    # TODO : Implementasikan inheritance terhadap kelas ini
    def __init__(self,nama):
        super().__init__(nama)

    #Menambah progress sesuai jam kerja dari kelas Staff
    def kerja(self, jam):
        super().kerja(jam)
        self.progress += (4*jam)

    #Menghitung gaji sesuai progress
    def hitung_gaji(self):
        return 2000 * self.progress

class StaffPartnership(Staff):
    # TODO : Implementasikan inheritance terhadap kelas ini
    def __init__(self,nama):
        super().__init__(nama)

    #Menambah progress sesuai jam kerja dari kelas Staff
    def kerja(self, jam):
        super().kerja(jam)
        self.progress += (1*jam)

    #Menghitung gaji sesuai progress
    def hitung_gaji(self):
        return 4000 * self.progress

class StaffPublikasi(Staff):
    # TODO : Implementasikan inheritance terhadap kelas ini
    def __init__(self,nama):
        super().__init__(nama)

    #Menambah progress sesuai jam kerja dari kelas Staff
    def kerja(self, jam):
        super().kerja(jam)
        self.progress += (20*jam)

    #Menghitung gaji sesuai progress
    def hitung_gaji(self):
        return 1500 * self.progress

#Membuat kelas untuk manager
class Manager:
    #Membuat dictionary untuk menyimpan staf
    def __init__(self):
        self.staffs = {}

    #Menambahkan objek staf ke dictionary
    def recruit_staff(self, staf):
        self.staffs[staf.nama] = staf

    #Mendapatkan objek sesuai nama staf
    def get_staff(self,nama):
        return self.staffs[nama]
    
    #Cek apakah nama staf ada dalam dictionary
    def is_staff_recruited(self, nama):
        return nama in self.staffs

# Tuliskan kode anda untuk alur program dibawah
# Selamat mengerjakan. Semangat!

gpr = Manager()
while(True):
    cmd = input().split(";")    #menerima input perintah
    perintah = cmd[0].upper()   #Memisahkan input perintah

    #Perintah untuk rekrut
    if(perintah == "REKRUT"):
        nama = cmd[1].title()   #Nama
        divisi = cmd[2].upper() #Divisi

        #Cek apakah nama sudah ada atau belum
        if(gpr.is_staff_recruited(nama)):
            print("{}​ sudah direkrut sebelumnya".format(nama))

        #Jika tidak ada
        else:
            print("{} direkrut".format(nama))

            #Cek divisi
            if(divisi == "ACARA"):
                gpr.recruit_staff(StaffAcara(nama))       #Daftarkan ke staf Acara
            elif(divisi == "PARTNERSHIP"):
                gpr.recruit_staff(StaffPartnership(nama)) #Daftarkan ke staf Partnership
            elif(divisi == "PUBLIKASI"):
                gpr.recruit_staff(StaffPublikasi(nama))   #Daftarkan ke staf Publikasi

    #Perintah untuk kerja
    elif(perintah == "KERJA"):
        nama = cmd[1].title()       #Nama staf
        jam = int(cmd[2])           #Jam kerja
        staf = gpr.get_staff(nama)  #Memanggil objek staf sesuai namanya

        #Cek apakah progress belum melebihi 100%
        if(staf.progress <= 100):
            print("{} bekerja selama {} jam".format(nama,jam))
            staf.kerja(jam) #Method kerja untuk menambah jam kerja dan progress

        #Jika diatas 100% maka tidak bisa bekerja lagi
        else:
            print("{}​ sudah mencapai {}​% progress".format(nama,staf.progress))

    #Perintah untuk Log
    elif(perintah == "LOG"):
        nama = cmd[1].title()       #Nama staf
        staf = gpr.get_staff(nama)  #Memanggil objek sesuai nama staf
        print(">> {}".format(nama)) #Print Nama
        print("Telah bekerja selama: {} jam".format(staf.jam_kerja))    #Print jumlah jam kerja
        print("Progress: {} persen".format(staf.progress))              #Print progress kerja
        print("Gaji sementara: {} bencoin".format(staf.hitung_gaji()))  #Print gaji staf

    #Perintah untuk berhenti
    elif(perintah == "EXIT"):
        break
