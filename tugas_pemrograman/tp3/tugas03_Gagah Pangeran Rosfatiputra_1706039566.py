nama_akun = {}  #Membuat dictionary untuk nama akun yang berisi object

#Dictionary yang isinya rincian tipe akun
tipe_akun = {'Pelajar': (25,150,0),
             'Reguler': (100,500,5),
             'Bisnis': (500,2000,15),
             'Elite': (10000,100000,50)
             }

#List Perintah
list_per = ["DAFTAR","SETOR","TARIK","TRANSFER","TAMBAH","UBAH","INFO"]

curr_dict = {}  #Dictionary untuk nilai mata uang

history = {}    #Dictionary untuk catatan transaksi

#Untuk eksekusi perintah
def perintah(cmd):
    cmd = cmd.split()
    ini_perintah = cmd[0].upper()

    #Cek apakah perintah valid
    if(ini_perintah in list_per):

        #Perintah Daftar
        if(ini_perintah == list_per[0]):
            nama = cmd[1].upper()      #Nama dibuat huruf besar
            jenis = cmd[2].capitalize() #Jenis akun

            #Cek nama akun
            if(nama in nama_akun):
                print("Akun atas nama {} sudah ada.".format(nama.capitalize()))
            else:
                #Instansiasi object dalam class BenCoin
                nama_akun[nama] = BenCoin(nama, jenis)

        #Perintah Tambah dan Ubah
        elif(ini_perintah == list_per[4] or ini_perintah == list_per[5]):
            
            #Periksa apakah format angkanya benar
            try:
                nominal = int(cmd[2])
                uang(ini_perintah,cmd[1].upper(),nominal) #Memanggil fungsi uang untuk tambah atau ubah
            except ValueError:
                print("Rate harus berupa nominal angka.")

        #Perintah Transfer
        elif(ini_perintah == list_per[3]):
            pengirim = cmd[1].upper() #Nama Pengirim
            penerima = cmd[2].upper() #Nama Penerima

            #Cek nama akun
            if(pengirim not in nama_akun):
                print("Akun pengirim atas nama {} tidak ada.".format(pengirim.capitalize()))
            elif(penerima not in nama_akun):
                print("Akun penerima atas nama {} tidak ada.".format(penerima.capitalize()))
            elif((pengirim not in nama_akun) and (penerima not in nama_akun)):
                print("Akun penerima atas nama {} dan pengirim atas nama {} tidak ada.".format(pengirim.capitalize(),penerima.capitalize()))

            else:
                #Periksa apakah format angkanya benar
                try:
                    nominal = int(cmd[3]) #Nominal BenCoin
                    #Memanggil method transfer
                    nama_akun[pengirim].transfer(penerima,nominal)
                except ValueError:
                    print("Transfer harus berupa nominal angka.")

        #Perintah Info
        elif(ini_perintah == list_per[6]):
            nama_akun[cmd[1].upper()].info()
            
        #Perintah Setor, Tarik, Info            
        else:
            nama = cmd[1].upper()
            #Cek nama akun
            if(nama not in nama_akun): print("Akun atas nama {} tidak ada.".format(nama.capitalize()))
            else:
                mata_uang = cmd[3].upper()

                #Perintah Setor
                if(ini_perintah == list_per[1]):
                    #Cek mata uang
                    if(mata_uang in curr_dict):
                        #Periksa apakah format angkanya benar
                        try:
                            nominal = int(cmd[2])
                            #Memanggil method setor
                            nama_akun[nama].setor(nominal,mata_uang)
                        except ValueError:
                            print("Penyetoran harus berupa nominal angka.")
                    else:
                        print("Mata Uang {} tidak ada.".format(mata_uang))

                #Perintah Tarik
                elif(ini_perintah == list_per[2]):
                    #Cek mata uang
                    if(mata_uang in curr_dict):
                        #Periksa apakah format angkanya benar
                        try:
                            nominal = int(cmd[2])
                            #Memanggil method tarik
                            nama_akun[nama].tarik(nominal,mata_uang)
                        except ValueError:
                            print("Penarikan harus berupa nominal angka.")
                    else:
                        print("Mata Uang {} tidak ada.".format(mata_uang))

    #Jika perintah tidak valid
    else:
        print("Perintah Tidak Tepat")
        

#Fungsi konversi mata uang dan BenCoin
def konversi(value,curr1,curr2):
    if(curr1 == "BC"): return value * curr_dict[curr2]  #Konversi dari BenCoin ke Mata Uang
    else: return value / curr_dict[curr1]               #Konversi dari Mata Uang ke Bencoin

#Fungsi tambah dan ubah rate uang
def uang(perintah,curr,nilai):
    cek = curr in curr_dict #Cek mata uang

    #Perintah tambah
    if(perintah == "TAMBAH"):
        #Jika mata uang ada maka tidak bisa ditambahkan, jika tidak ada bisa ditambahkan
        if(cek):
            print("Mata uang {} sudah pernah ditambahkan dengan rate {} per BenCoin".format(curr,nilai))
        else:
            curr_dict[curr] = nilai
            print("Mata uang {} telah ditambahkan dengan rate {} per BenCoin.".format(curr,nilai))

    #Perintah ubah
    else:
        #Jika mata uang ada maka bisa diubah, jika tidak ada maka tidak bisa diubah
        if(cek):
            curr_dict[curr] = nilai
            print("Rate mata uang {} berubah menjadi {} per BenCoin.".format(curr,nilai))
        else:
            print("Mata uang {} tidak ada.".format(curr))

#Membuat class BenCoin
class BenCoin:

    #Method untuk mendaftarkan akun BenCoin
    def __init__(self, name, type_acc):
        self.name = name.capitalize()   #Nama Akun
        self.type_acc = type_acc        #Jenis Akun
        self.saldo = 0                  #Saldo Awal
        self.trans_limit, self.tab_limit, self.trans_fee = tipe_akun[type_acc] #Batas Transaksi, Batas Tabungan, Biaya Transaksi
        history[self.name] = []         #Riwayat Transaksi
        print("Akun atas nama {} telah terdaftar dengan paket {}.".format(self.name,self.type_acc))

    #Method untuk penyetoran
    def setor(self, cash, currency):
        #Cek apakah penyetoran lebih dari nol
        if(cash <= 0):
            print("Setoran harus lebih dari nol {}.".format(currency))
        else:
            #Konversi dari mata uang ke bencoin
            bc = konversi(cash,currency,"BC")

            #Kalau akun sudah penuh, maka gagal menyetor
            if(self.saldo == self.tab_limit):
                print("Akun {} sudah memenuhi kapasitas".format(self.name))

            #Kalau akun belum penuh, tapi penyetoran melebihi kapasitas
            elif((self.saldo + bc) > self.tab_limit):
                bc = self.tab_limit - self.saldo    #Jumlah bencoin yg bisa disetor
                self.saldo = self.tab_limit         #Saldo akun menjadi penuh
                print("Akun {} telah bertambah {} BenCoin.".format(self.name,bc))
                history[self.name].append("SETOR {} {} {}".format(currency, cash, bc)) #Menambah riwayat transaksi

            #Kalau akun belum penuh dan bisa menyetor normal
            else:
                self.saldo += bc #Menambahkan bencoin ke saldo
                print("Akun {} telah bertambah {} BenCoin.".format(self.name,bc))
                history[self.name].append("SETOR {} {} {}".format(currency, cash, bc)) #Menambah riwayat transaksi

    #Method untuk Penarikan
    def tarik(self, bc, currency):
        #Cek apakah penyetoran lebih dari nol
        if(bc <= 0):
            print("Penarikan harus lebih dari nol BenCoin.")
        else:
            #Cek apakah saldo masih cukup untuk melakukan transaksi
            if(self.saldo <= self.trans_fee):
                print("Akun {} tidak cukup untuk melakukan penarikan.".format(self.name))

            #Akun masih bisa melakukan penarikan, tapi sejumlah penarikan dikurangi biaya transaksi
            elif((bc + self.trans_fee) > self.saldo):
                bc = self.saldo - self.trans_fee    #Jumlah bencoin yang bisa ditarik
                self.saldo = 0                      #Saldo menjadi kosong karena habis ditarik

                #Jika bencoin yang ditarik melebihi batas transaksi
                if(bc > self.trans_limit):
                    self.saldo += bc - self.trans_limit #Sisa Saldo
                    bc = self.trans_limit               #Jumlah Bencoin yang bisa ditarik

                #Konversi dari bencoin ke mata uang
                cash = konversi(bc,"BC",currency)
                print("Penarikan {} dari akun {} berhasil !".format(cash,self.name))
                history[self.name].append("TARIK {} {} {}".format(currency, cash, bc)) #Menambah riwayat transaksi

            #Saat penarikan normal
            else:
                #Jika bencoin yang ditarik melebihi batas transaksi
                if(bc > self.trans_limit): bc = self.trans_limit #Jumlah Bencoin yang bisa ditarik
                self.saldo -= (bc + self.trans_fee)              #Sisa Saldo

                #Konversi dari bencoin ke mata uang
                cash = konversi(bc,"BC",currency)
                print("Penarikan {} dari akun {} berhasil !".format(cash,self.name))
                history[self.name].append("TARIK {} {} {}".format(currency, cash, bc)) #Menambah riwayat transaksi

    def transfer(self,penerima,bc):
        #Cek apakah Transfer lebih dari nol
        if(bc <= 0):
            print("Transfer harus lebih dari nol BenCoin.")
        else:
            penerima = nama_akun[penerima]

            #Cek apakah saldo masih cukup untuk melakukan transaksi
            if(self.saldo <= self.trans_fee):
                print("Akun {} tidak cukup untuk melakukan transfer.".format(self.name))

            #Akun masih bisa melakukan transfer, tapi sejumlah transfer dikurangi biaya transaksi
            elif((bc + self.trans_fee) > self.saldo):
                bc = self.saldo - self.trans_fee                #Jumlah bencoin yang bisa ditransfer

                #Jika bencoin yang ditransfer melebihi batas tabungan penerima
                if((bc + penerima.saldo) > penerima.tab_limit):
                    bc = penerima.limit - penerima.saldo        #Jumlah bencoin yang bisa ditransfer
                    penerima.saldo = penerima.tab_limit         #Saldo penerima menjadi penuh
                    
                    #Jika bencoin yang ditransfer melewati batas transaksi
                    if(bc > self.trans_limit):
                        penerima.saldo -= (bc - self.trans_limit)   #Saldo penerima
                        bc = self.trans_limit                       #Bencoin yang bisa ditransfer
                    
                    self.saldo = (penerima.saldo + bc) - penerima.tab_limit #Sisa saldo pengirim
                    print("{} berhasil mentransfer {} BenCoin kepada {}.".format(self.name,bc,penerima.name))
                    history[self.name].append("TRANSFER {} {}".format(penerima.name,bc)) #Menambah riwayat transaksi

                #Bencoin yang ditransfer tidak melebihi batas tabungan penerima
                else:
                    #Jika bencoin yang ditransfer melewati batas transaksi
                    if(bc > self.trans_limit): bc = self.trans_limit #Bencoin yang bisa ditransfer
                    penerima.saldo += bc                #Saldo penerima
                    self.saldo -= (bc + self.trans_fee) #Sisa saldo pengirim
                    print("{} berhasil mentransfer {} BenCoin kepada {}.".format(self.name,bc,penerima.name))
                    history[self.name].append("TRANSFER {} {}".format(penerima.name,bc)) #Menambah riwayat transaksi

            #Pengirim mentransfer normal
            else:
                #Jika bencoin yang ditransfer melebihi batas tabungan penerima
                if((bc + penerima.saldo) > penerima.tab_limit):
                    bc = penerima.limit - penerima.saldo    #Jumlah bencoin yang bisa ditransfer
                    penerima.saldo = penerima.tab_limit     #Saldo penerima menjadi penuh

                    #Jika bencoin yang ditransfer melewati batas transaksi
                    if(bc > self.trans_limit):
                        penerima.saldo -= (bc - self.trans_limit)   #Saldo penerima
                        bc = self.trans_limit                       #Bencoin yang bisa ditransfer

                    self.saldo -= (bc + self.trans_fee)             #Sisa saldo pengirim
                    print("{} berhasil mentransfer {} BenCoin kepada {}.".format(self.name,bc,penerima.name))
                    history[self.name].append("TRANSFER {} {}".format(penerima.name,bc)) #Menambah riwayat transaksi

                #Bencoin yang ditransfer tidak melebihi batas tabungan penerima
                else:
                    #Jika bencoin yang ditransfer melewati batas transaksi
                    if(bc > self.trans_limit): bc = self.trans_limit #Bencoin yang bisa ditransfer
                    penerima.saldo += bc                #Saldo penerima
                    self.saldo -= (bc + self.trans_fee) #Sisa saldo pengirim
                    print("{} berhasil mentransfer {} BenCoin kepada {}.".format(self.name,bc,penerima.name))
                    history[self.name].append("TRANSFER {} {}".format(penerima.name,bc)) #Menambah riwayat transaksi

    #Method Info
    def info(self):
        print("{:<15s}: {}".format("Nama",self.name))                   #Print Nama
        print("{:<15s}: {}".format("Jenis Akun",self.type_acc))         #Print Jenis Akun
        print("{:<15s}: {}".format("Jumlah BenCoin",float(self.saldo))) #Print sisa saldo sampai saat di print
        print("Transaksi :")

        #Mengakses data riwayat transaksi
        for data in history[self.name]:
            print(data)
        
print("Selamat datang di BenCoin!")
print("Gunakan perintah berikut untuk bertransaksi:")
print("DAFTAR - SETOR - TARIK - TRANSFER - TAMBAH - UBAH - INFO")
print("Gunakan perintah AKHIR untuk mengakhiri transaksi")

while(True):
    masukkan = input(">>> ")
    if(masukkan == "AKHIR"):
        print("Terima kasih sudah menggunakan layanan BenCoin")
        break
    else: perintah(masukkan)
