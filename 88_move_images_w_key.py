from tkinter import *

# # move an image on a window

# def move_up(event):
#   label.place(x=label.winfo_x(), y=label.winfo_y()-10)

# def move_down(event):
#   label.place(x=label.winfo_x(), y=label.winfo_y()+10)

# def move_left(event):
#   label.place(x=label.winfo_x()-10, y=label.winfo_y())

# def move_right(event):
#   label.place(x=label.winfo_x()+10, y=label.winfo_y())

# window = Tk()
# window.geometry("500x500")

# window.bind("<z>", move_up)
# window.bind("<s>", move_down)
# window.bind("<q>", move_left)
# window.bind("<d>", move_right)
# window.bind("<Up>", move_up)
# window.bind("<Down>", move_down)
# window.bind("<Left>", move_left)
# window.bind("<Right>", move_right)

# myImage = PhotoImage(file="88_formula_one.png").subsample(4)
# label = Label(window, image=myImage)
# label.place(x=0, y=0)

# window.mainloop()


# move an image on a canvas

def move_up(event):
    canvas.move(my_image, 0, -10)


def move_down(event):
    canvas.move(my_image, 0, 10)


def move_left(event):
    canvas.move(my_image, -10, 0)


def move_right(event):
    canvas.move(my_image, 10, 0)


window = Tk()

window.bind("<z>", move_up)
window.bind("<s>", move_down)
window.bind("<q>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

photo_image = PhotoImage(file="88_formula_one.png").subsample(4)
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

window.mainloop()
