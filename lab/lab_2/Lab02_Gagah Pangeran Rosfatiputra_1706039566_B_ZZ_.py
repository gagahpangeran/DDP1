surga = int(input("Masukkan kalimat surgawi: "))

#inisialisasi variabel dunia
dunia = ''

#melakukan iterasi hingga variabel surga = 0
while(surga >= 0):
    
    #Jika variabel surga dimodulo 2 hasilnya 1, dikonversi menjadi B lalu ditambahkan ke variabel dunia
    if(surga % 2 == 1):
        dunia = 'B' + dunia
        
    #Selain itu, surga dimodulo 2 hasilnya 0, dikonversi menjadi P lalu ditambahkan ke variabel dunia
    else:
        dunia = 'P' + dunia

    #membagi dua variabel surga
    surga = surga // 2

    #Jika nilai surga sudah = 0, iterasi dihentikan
    if(surga == 0): break

print("Makna duniawi:", dunia)
