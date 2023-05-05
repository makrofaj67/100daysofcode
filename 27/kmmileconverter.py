import tkinter

ekran = tkinter.Tk()
ekran.title("dönüştürücü")
ekran.minsize(width=300, height=100)
ekran.config(padx=50, pady=50)

kmlabel = tkinter.Label(text="km")
kmlabel.grid(column=3, row=2)

milelabel = tkinter.Label(text="mile")
milelabel.grid(column=3, row=1)

esittirlabel = tkinter.Label(text="eşittir")
esittirlabel.grid(column=1, row=2)

kmciktilabel = tkinter.Label(text="0")
kmciktilabel.grid(column=2, row=2)

girdi = tkinter.Entry()
girdi.grid(column=2, row=1)
girdi.get()

def milestokm():
 mile = int(girdi.get()) * 1.609344
 mile = f"{mile:.2f}"
 kmciktilabel.config(text=mile)

buton = tkinter.Button(text="dönüştür", command=milestokm)
buton.grid(column=2, row=3)

ekran.mainloop()