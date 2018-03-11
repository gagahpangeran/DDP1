import turtle

panjang = int(input("Masukkan panjang setiap anak tangga: "))

t = turtle.Turtle()
t.pendown()

#Bagian Kuning
t.color('yellow')
t.left(90)
t.forward(panjang)
t.right(90)
t.forward(panjang)

#Bagian Biru
t.color('blue')
t.left(90)
t.forward(panjang)
t.right(90)
t.forward(panjang)

#Bagian merah
t.color('red')
t.left(90)
t.forward(panjang)
t.right(90)
t.forward(panjang)

#Bagian hijau
t.color('green')
t.right(90)
t.forward(3*panjang)
t.right(90)
t.forward(3*panjang)

t.penup()

turtle.exitonclick()
