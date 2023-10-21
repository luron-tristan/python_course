# a listing of selectable items within it's own container = dropdown

def submit():
  # selected = listbox.get(listbox.curselection()) # unique
  # print("You have ordered " + selected)

  food = []

  for index in listbox.curselection():
    food.insert(index, listbox.get(index))

  for index in food:
    print(index)

def add():
  listbox.insert(listbox.size(), entryBox.get())
  resizeBox()

def delete():
  # listbox.delete(listbox.curselection()) # unique

  for index in reversed(listbox.curselection()):
    listbox.delete(index)
  resizeBox()

def resizeBox():
  listbox.config(height=listbox.size())


from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE,
                  )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

resizeBox()

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()




window.mainloop()