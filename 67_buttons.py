from tkinter import *

window = Tk()

count = 0
def click():
  global count
  count += 1
  print(count)

photo = PhotoImage(file="66-small-house.png")

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#0f0",
                bg="black",
                activeforeground='#0f0',
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom",
                )
button.pack()

window.mainloop()