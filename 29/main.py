import tkinter
from tkinter import messagebox
import passwordgenerator
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def sifreyap():
 passwordentry.delete(0, "end")
 sifreyapici = passwordgenerator.PasswordYapici()
 sifre = sifreyapici.passwordyap()
 passwordentry.insert(string=sifre, index=0)
 pyperclip.copy(sifre)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
 website = websiteentry.get()
 email = emailusernameentry.get()
 password = passwordentry.get() 
 
 if website != "" and email != "" and password != "": 
  isokay = messagebox.askokcancel(message=f"Website: {website} \n Email:{email} \n Password: {password}", title="Onaylıyor musunuz?")
  if isokay:
   with open("data.txt", "a") as dosya:
    dosya.write(f"{website} | {email} | {password}\n")
   websiteentry.delete("0", "end")
   emailusernameentry.delete("0", "end")
   passwordentry.delete("0", "end") 
 elif website or email or password == "":
  messagebox.showinfo(title="Aman!", message="boş bırakma")  

# ---------------------------- UI SETUP ------------------------------- #
ekran = tkinter.Tk()
ekran.title("kalem")
ekran.config(padx=50, pady=50)

menu = tkinter.Menu(ekran, tearoff=0)
menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menu.add_separator()
menu.add_command(label="Exit", command=ekran.quit)
menu.pack()



websitelabel = tkinter.Label(text="Website")
websitelabel.grid(column=1, row=2)

websiteentry = tkinter.Entry(width=42)
websiteentry.grid(column=2, row=2, columnspan=2)
websiteentry.focus()

emailusernamelabel = tkinter.Label(text="Email/Username")
emailusernamelabel.grid(column=1, row=3)

emailusernameentry = tkinter.Entry(width=42)
emailusernameentry.grid(column=2, row=3, columnspan=2)

passwordlabel = tkinter.Label(text="Password")
passwordlabel.grid(column=1, row=4)

passwordentry = tkinter.Entry(width=22)
passwordentry.grid(column=2, row=4)

generatepasswordbutton = tkinter.Button(text="Generate Password", command=sifreyap)
generatepasswordbutton.grid(column=3, row=4)

addbutton = tkinter.Button(text="Add", width=36, command=save)
addbutton.grid(row=5, column=2, columnspan=2)

foto = tkinter.PhotoImage(file="logo.png")
kanvas = tkinter.Canvas(width=200, height=200)
kanvas.create_image(100, 100, image=foto)
kanvas.grid(row=1, column=2)

ekran.mainloop()