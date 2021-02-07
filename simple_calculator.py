from tkinter import *

mainWindow = Tk()

mainWindow.title("My Simple Calculator")
mainWindow.geometry("1000x700+50+50")

displayFrame = Label(mainWindow,bg="skyblue",text="test")
displayFrame.grid(row=0,column=0)

mainWindow.mainloop()