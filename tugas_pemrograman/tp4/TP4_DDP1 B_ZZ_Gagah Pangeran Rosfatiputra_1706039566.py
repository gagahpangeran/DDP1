#import semua module yang diperlukan
from tkinter import *
from tkinter.font import *
from pygame import *
from time import *

#Membuat class my piano
class MyPiano:
    def __init__(self,master):
        #Membuat window tkinter
        self.master = master            #Inisiasi window
        master.title("Piano Jaman Now") #Judul
        master.geometry("850x500")      #Ukuran window
        master.resizable(width=False, height=False) #Membuat window tidak bisa di resize

        #Membuat label untuk tulisan di dalam window
        Label(master, text="Piano Jaman Now", font=Font(family="Comic Sans MS", size=30), height=1).grid(row=1,column=5,columnspan=8)

        #Membuat textbox
        self.inp = StringVar()
        self.teks = Entry(master,width=25,font=Font(family="Comic Sans MS",size=20))
        self.teks.grid(row=2,column=4,columnspan=8)

        #Membuat tombol disamping textbox
        but_play = Button(master, text="Play!",width=8,font=Font(family="Comic Sans MS",size=13),bg="black",fg="white")
        but_play.grid(row=2,column=12,columnspan=2)
        but_play.bind("<Button-1>",self.mainkan)

        #Membuat radiobutton
        self.oktaf = IntVar()
        self.oktaf.set(1)
        for i in range(1,8):
            Radiobutton(master, text=str(i), variable=self.oktaf, value=i, height="3").grid(row=3,column=4+i)

        #Membuat dictionary untuk warna tiap button
        tuts = {"C":"#b80000","D":"#ff3701","E":"#fef900","F":"#3fb900","G":"#00406b","A":"#20004e","B":"#581540","C'":"#510034",}
        tuts2 = {"C#":"#fd0100","D#":"#fd8000","F#":"#007612","G#":"#001588","A#":"#6f0080"}

        #Membuat dictionary untuk konversi
        self.nadaa = {"C#":"Db","D#":"Eb","F#":"Gb","G#":"Ab","A#":"Bb"}

        #Membuat tuts piano biasa
        h=0
        for i in tuts:
            tombol = Button(master, text=i+"\n", width="6", height="8", bg=tuts[i], font=Font(family="Comic Sans MS",size=20),anchor=S)
            tombol.grid(row=4,column=1+h,rowspan=2,columnspan=2)
            tombol.bind("<Button-1>",self.klik)
            h+=2

        #Membuat tuts piano yang di atas
        h=0
        for i in tuts2:
            tombol = Button(master, text=i+"\n"+self.nadaa[i]+"\n", width="6", height="7", bg=tuts2[i], fg="white", font=Font(family="Comic Sans MS"),anchor=S)
            tombol.grid(row=4,column=2+h,rowspan=1,columnspan=2,sticky=(N))
            tombol.bind("<Button-1>",self.klik)
            if h==2: h+=4
            else: h+=2

        #Membuat bind agar bisa keypress
        keypress1 = ["s","d","f","g","h","j","k","l","e","r","y","u","i"]
        keypress2 = ["C","D","E","F","G","A","B","C'","C#","D#","F#","G#","A#"]
        for tombol,nada in zip(keypress1,keypress2):
            master.bind(tombol, lambda event, nada = nada: self.pencet(nada))

    #Fungsi untuk konversi nama nada
    def nada(self,huruf,angka):
        if(huruf in self.nadaa): huruf = self.nadaa[huruf]
        if(huruf == "C'"):
            huruf = "C"
            angka += 1
        return "sound/Piano.mf."+huruf+str(angka)+".wav"
            

    #Fungsi saat tombol di klik oleh mouse
    def klik(self,event):
        cek = event.widget.cget('text').split()
        mixer.init()
        suara = self.nada(cek[0],self.oktaf.get())
        sound = mixer.Sound(suara)
        sound.play()

    #Fungsi untuk memainkan nada dari textbox
    def mainkan(self,event):
        ndnd = self.teks.get().split()
        mixer.init()
        for i in ndnd:
            if(len(i) == 3): suara = self.nada(i[:2],i[2])
            else: suara = self.nada(i[0],i[1])
            sound = mixer.Sound(suara)
            sound.play()
            sleep(0.5)

    #Fungsi saat keyboard di tekan
    def pencet(self,event):
        mixer.init()
        suara = self.nada(event,self.oktaf.get())
        sound = mixer.Sound(suara)
        sound.play()
            

#Program utama
root = Tk()
piano = MyPiano(root)
root.mainloop()
