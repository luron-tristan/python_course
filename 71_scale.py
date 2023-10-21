from tkinter import *

def submit():
  print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()

hotImage = PhotoImage(file='71-hot.png').subsample(10)
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL, # orientation of scale
              font=("consolas", 20),
              tickinterval=10, # adds numeric indicators for value
              # showvalue=0, #hide current value
              troughcolor='#69eaff',
              fg="#ff1c00",
              bg="#111",
              )
# scale.set(56)
scale.set(((scale['from'] - scale['to']) / 2) + scale["to"]) # set current value of slider to th middle
scale.pack()

coldImage = PhotoImage(file='71-cold.png').subsample(23)
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()