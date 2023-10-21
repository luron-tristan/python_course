from tkinter import *

# Tk() => independant window
# Toplevel() => related window

# def create_window():
#   new_window = Toplevel() # Toplevel() = new window 'on top' of other windows. linked to a 'bottom' window

# window = Tk() # bottom window
# window.geometry("420x420")

# Button(window, text="Create new window", command=create_window).pack()

# window.mainloop()

def create_window():
  new_window = Tk()
  old_window.destroy() # close out of old window

old_window = Tk()

Button(old_window, text="Create new window and close old", command=create_window).pack()

old_window.mainloop()