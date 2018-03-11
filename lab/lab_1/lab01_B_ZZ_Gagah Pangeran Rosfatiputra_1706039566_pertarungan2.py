biaya = int(input("Masukkan biaya pernikahan: Rp "))

hari = biaya // 500000
tahun = hari // 336
bulan = (hari % 336) // 28
minggu = ((hari % 336) % 28) // 7
hari = (((hari % 336) % 28) % 7)

print("Anda harus bekerja selama ", end="")
print(tahun, "tahun ", end="")
print(bulan, "bulan ", end="")
print(minggu, "minggu ", end="")
print(hari, "hari ", end="")
print("untuk memenuhi biaya pernikahan.")
