from tkinter import *
import calendar

root = Tk()
root.title("My Own Gui Calendar") # setting title of our Gui
year = 2020 # year for which we want the calendar to be shown on our Gui 
myCal = calendar.calendar(year)  # storing 2020 year calendar data inside myCal
cal_year = Label(root,text = myCal, font = "Consolas 10 bold") # showing calendar data using label  widget
cal_year.pack() # packing the label widget
root.mainloop() # running ther program in ready state