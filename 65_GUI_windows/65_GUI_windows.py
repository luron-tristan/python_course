from tkinter import *

# windows = serves as a container to hold or contain these widgets
# widgets = GUI elements: buttons, textboxes, labels, images

window = Tk() # instatiate an instance of a window
window.geometry("420x420")
window.title("Triss' first GUI Program")

icon = PhotoImage(file="C:\\Users\\user\\projets\\python\\helloWorld\\65_GUI_windows\\owl.png")
window.iconphoto(True, icon)
window.config(background="#F4F7FA")

window.mainloop() # place windsow on computer screen, listen for events
