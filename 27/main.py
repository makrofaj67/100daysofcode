import tkinter

ekran  = tkinter.Tk()
ekran.title("dönüştürücü")
ekran.minsize(width= 600, height=600)


label = tkinter.Label(text= "celcius")
label.pack()

def klik():
 kalem = giris.get()
 label.configure(text=kalem)

buton = tkinter.Button(text= "clickme", command = klik)
buton.pack()


giris = tkinter.Entry()
giris.pack()

ekran.mainloop()

##pack(side = "left"), place(x=0, y=0) //sol üst köşeye, grid(column= row=)
##grid and pack aynı anda kullanılamaz

##ekran.config(padx=, pady)