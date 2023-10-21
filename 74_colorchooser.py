from tkinter import *
from tkinter import colorchooser # submodule

def click():
  # window.config(bg=colorchooser.askcolor()[1])
  color = colorchooser.askcolor()
  colorHex = color[1]
  window.config(bg=colorHex)

window = Tk()
window.geometry("420x420")
button = Button(text="Click me", command=click)
button.pack()
window.mainloop()