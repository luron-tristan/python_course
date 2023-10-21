from tkinter import *

# an areawidget that holds text and/or image within a window

window = Tk()
# window.geometry("420x420")
window.title("Triss' second GUI Program")

photo = PhotoImage(file="66-small-house.png")

label = Label(window,
              text="Hello World how is it in the house?",
              font=("Arial", 40, "bold"),
              fg="#0F0",
              bg="black",
              relief="raised",
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom"
              )
label.pack()
# label.place(x=10, y=10)

window.mainloop()