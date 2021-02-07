from tkinter import *

mainWindow = Tk()

mainWindow.title("My Simple Calculator")
mainWindow.geometry("1000x700+50+50")

displayFrame = Frame(mainWindow,bg="gray",width=900,height=100)
displayFrame.grid(row=0,column=0,sticky="n")
displayFrame.config(relief="sunken",borderwidth=5)

buttons = ["1,2,3,4,5,6,7,8,9"]

mainWindow.mainloop()