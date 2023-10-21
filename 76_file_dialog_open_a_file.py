from tkinter import *
from tkinter import filedialog

def openFile():
  filepath = filedialog.askopenfilename(initialdir="C:\\Users\\user\\projets\\python\\helloWorld",
                                        title="Open file ok?",
                                        filetypes= (("text files", "*.txt"),
                                                    ("all files", "*.*"))
                                        )
  print(filepath)
  file = open(filepath, "r")
  print(file.read())
  file.close()

window = Tk()
button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()