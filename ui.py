#!/usr/bin/python

from Tkinter import *

#################################################
def print_to_console(event):
	if( len(entry_1.get()) > 0 ):
		print entry_1.get()
	else:
		print "Entry field is empty, add some text and try again"

def close_app(event):
	mw.quit()

#################################################

mw = Tk()

label_1 = Label(mw, text="Enter some text: ")
entry_1 = Entry(mw)
button_1 = Button(mw, text="Print to Console")
button_2 = Button(mw, text="Quit")

label_1.grid(row=0, column=0, sticky=W)
entry_1.grid(row=0, column=1, sticky=E)
button_1.grid(row=1, column=1, sticky=E)
button_2.grid(row=2, column=1, sticky=E)

button_1.bind("<Button-1>", print_to_console)
button_2.bind("<Button-1>", close_app)

mainloop()