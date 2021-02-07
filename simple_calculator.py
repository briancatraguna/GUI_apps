from tkinter import *

mainWindow = Tk()

mainWindow.title("My Simple Calculator")
mainWindow.geometry("1000x700+50+50")

displayFrame = Frame(mainWindow,bg="gray",width=900,height=100)
displayFrame.grid(row=0,column=0)
displayFrame.config(relief="sunken",borderwidth=5)

mainWindow.mainloop()