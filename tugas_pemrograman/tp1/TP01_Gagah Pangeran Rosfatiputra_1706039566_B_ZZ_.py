import turtle
import random

x = turtle.Screen()
x.title("Colorful Cheesboard and Flower") #Membuat Judul

#Meminta masukkan jumlah baris catur dari pengguna
row = int(x.numinput("Membuat Bunga dan Catur", "Masukkan baris catur:\n(2-15 baris)",minval=2,maxval=15))

#Mengatur maksimal ukuran kotak dari masukkan pengguna
if(row<=6):
    maks = 50
elif(7 <= row <= 11):
    maks = 30
else:
    maks = 20
size = int(x.numinput("Membuat Bunga dan Catur", "Masukkan ukuran kotak\n(15-"+str(maks)+") pixel",minval=15,maxval=maks))

#meminta masukkan jumlah kelopak dari pengguna
petal = int(x.numinput("Membuat Bunga dan Catur", "Masukkan jumlah kelopak bunga\n(3-25 kelopak)",minval=3,maxval=25))

t = turtle.Turtle()

t.penup()
t.speed(0) #Mengatur Kecepatan turtle yang paling cepat

#Inisialisasi posisi awal
x_awal = 0
y_awal = 200

#Meletakkan kursor turtle ke posisi awal
t.goto(x_awal,y_awal)

#Mulai menggambar
t.pendown()

#Menggambar Bunga
for i in range(petal):
    t.pensize(3) #Mengatur ukuran pen
    t.color(random.random(),random.random(),random.random()) #Mengatur warna rgb dengan fungsi random
    t.seth(45) #Mengatur posisi kepala kursor turtle
    t.right(360*i/petal) #Mengatur arah putaran kursor turtle

    #Mebuat sebuah kelopak
    t.circle(100,90)
    t.left(90)
    t.circle(100,90)


#Berhenti menggambar
t.penup()

#Inisialisasi posisi awal yang baru
x_awal = -((row*size) / 2)
y_awal = 50

#Meletakkan turtle ke posisi awal menggambar
t.goto(x_awal,y_awal)
t.seth(0) #Mengatur arah kursor turtle ke kanan
t.pensize(1) #Mengembalikan ukuran pena


#Menggambar papan catur
for i in range(row):
    for j in range(row):
        t.color(random.random(),random.random(),random.random()) #Mengatur warna rgb dengan fungsi random
        t.pendown() #mulai menggambar dengan memberikan warna di kotaknya
        t.begin_fill()

        #Menggambar kotak
        for k in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()

        #Berhenti gambar kotak dan ke posisi selanjutnya
        t.penup()
        t.forward(size)

    #Selesai menggambar satu baris lalu pergi ke posisi baris berikutnya
    t.penup()
    t.goto(x_awal,-((i+1)*size)+y_awal)

#Selesai menggambar papan catur, lalu mengatur posisi untuk menuliskan kata-kata
t.penup()
t.goto(0,-((row*size)))

#Membuat variabel untuk ditulis
kata = "Colorful Chessboard of " + str(row*row) +" Square and Flower of " + str(petal) + " Petals"

t.color(random.random(),random.random(),random.random()) #Mengatur warna rgb dengan fungsi random
t.write(kata,align="center",font=("Arial",20,"normal")) #Menulis kata di layar

#Selesai
t.hideturtle()
turtle.exitonclick()
