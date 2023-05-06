import tkinter
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def resettimer():
 global reps
 ekran.after_cancel(timer)
 kanvas.itemconfig(timertext, text="00:00")
 pomodorotext.config(text="TIMER", fg=PINK)
 checktext.config(text="")
 reps = 0
 
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def baslatici():
 global reps
 reps += 1
 
 if reps % 8 == 0:
  countdown(LONG_BREAK_MIN * 60)
  pomodorotext.config(text="L BREAK", fg=GREEN)
 elif reps % 2 == 0:
  countdown(SHORT_BREAK_MIN * 60)
  pomodorotext.config(text="S BREAK", fg=PINK)
 else:
  countdown(WORK_MIN * 60)
  pomodorotext.config(text="WORK", fg=RED)
 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(sure):
 dakika = sure // 60
 saniye = sure % 60
 
 if len(str(saniye)) == 1:
  saniye = "0" + str(saniye)
 
 kanvas.itemconfig(timertext , text=f"{dakika}:{saniye}")
 if sure > 0:
  global timer
  timer = ekran.after(1000, countdown, sure - 1)
 if sure == 0:
  baslatici()
  gorils = ""
  worksessions = math.floor(reps/2)
  for i in range(worksessions):
   gorils += "🧌"
  checktext.config(text=gorils)
# ---------------------------- UI SETUP ------------------------------- #

ekran = tkinter.Tk()
ekran.title("pamodero")
ekran.config(padx=100, pady=50, bg=YELLOW)
ekran.minsize(width=500, height=300)
ekran.resizable(width=False, height=False)

startbutton = tkinter.Button(text="start", command=baslatici)
startbutton.grid(column=1, row=3)
startbutton.config(bg=YELLOW)

resetbutton = tkinter.Button(text="reset", command=resettimer)
resetbutton.grid(column=3, row=3)
resetbutton.config(bg=YELLOW)

pomodorotext = tkinter.Label(text="TIMER", font=(FONT_NAME, 45, "bold"), foreground=GREEN)
pomodorotext.grid(column=2, row=1)
pomodorotext.config(pady=10, bg=YELLOW)

checktext = tkinter.Label(text="", font=(FONT_NAME, 25, "bold"))
checktext.config(bg=YELLOW, pady=10)
checktext.grid(column=2, row=4)

foto = tkinter.PhotoImage(file="28/tomato.png")
kanvas = tkinter.Canvas(width=210, height=210, bg=YELLOW, highlightthickness=0)
kanvas.create_image(103, 90, image=foto)
timertext = kanvas.create_text(103, 115, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
kanvas.grid(column=2, row=2, pady=20)

ekran.mainloop()
