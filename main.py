import tkinter

my_window = tkinter.Tk()
my_window.minsize(width=300,height=300)
my_window.title("Kitle Endeks")

#labels
label_yas = tkinter.Label(text="Yasınızı giriniz: ",bg="light blue").place(x=110,y=10)
label_boy = tkinter.Label(text="Boyunuzu giriniz: ",bg="light blue").place(x=102,y=80)
label_boy = tkinter.Label(text="Kilonuzu giriniz: ",bg="light blue").place(x=108,y=150)

yas = tkinter.IntVar()
boy = tkinter.IntVar()
kilo = tkinter.IntVar()
#entry
enter_yas = tkinter.Entry(bg="#E6E6FA",textvariable=yas).place(x=90,y=40)
enter_boy = tkinter.Entry(bg="#E6E6FA",textvariable=boy).place(x=90,y=110)
enter_kilo = tkinter.Entry(bg="#E6E6FA",textvariable=kilo).place(x=90,y=180)

def indeks():
    a = yas.get()
    b = boy.get()
    c = kilo.get()
    sonuc = float(c/(b*b/10000))
    print(sonuc)
    if sonuc <=18.5:
        my_sonuc_label = tkinter.Label(text="ZAYIF",bg="orange").place(x=50,y=225)
    elif sonuc > 18.5 and sonuc <= 24.9:
        my_sonuc_label = tkinter.Label(text="NORMAL", bg="light blue").place(x=50, y=225)
    elif sonuc >= 25 and sonuc <= 29.9:
        my_sonuc_label = tkinter.Label(text="Fazla Kilolu", bg="blue").place(x=50, y=225)
    elif sonuc >= 30 and sonuc <= 34.9:
        my_sonuc_label = tkinter.Label(text="1.Derece Obezite", bg="red").place(x=50, y=225)
    elif sonuc >=35 and sonuc <=40:
        my_sonuc_label = tkinter.Label(text="2.Derece Obezite", bg="red").place(x=50, y=225)
    elif sonuc >=40.1 and sonuc <=49.9:
        my_sonuc_label = tkinter.Label(text="3.Derece Obezite", bg="red").place(x=50, y=225)
    elif sonuc >=50 and sonuc<=60:
        my_sonuc_label = tkinter.Label(text="Süper Obezite", bg="red").place(x=50, y=225)
    else :
        my_sonuc_label = tkinter.Label(text="Sen öl", bg="yellow").place(x=50, y=225)
#buton
islem_button = tkinter.Button(text="HESAPLA",bg="light blue",command=indeks).place(x=200,y=250)



my_window.mainloop()