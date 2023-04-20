import turtle
import pandas
ekran = turtle.Screen()
ekran.addshape("25/us-states-game-start/blank_states_img.gif")
turtle.shape("25/us-states-game-start/blank_states_img.gif")
data = pandas.read_csv("25/us-states-game-start/50_states.csv")
states = data.state.to_list() 
 
skor = 0
dogrubilinensehirler = []
while skor != 50: 
 input = turtle.textinput(f"{skor}/50", "ameriakadaheyalatbul").title()
 if input.title() in states:
  skor = skor + 1
  dogrubilinensehirler.append(input.title())
  corx = data[data.state == input.title()].iloc[0].x
  cory = data[data.state == input.title()].iloc[0].y
  
  sehirismi = turtle.Turtle()
  sehirismi.penup()
  sehirismi.goto(int(corx), int(cory))  
  sehirismi.ht()
  sehirismi.write(f"{input}")
  
ekran.mainloop()