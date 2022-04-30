
from tkinter import *
from tkinter import ttk


root = Tk()
photo = PhotoImage(file="gari.png")

lable = Label(root,text="Hello",font=('Arial',40),fg="green",relief=RAISED,bg="#00ffff",padx=100,pady=10,bd=5,image=photo,compound="bottom").pack()



	
	




def click():
	print('clicked')
	
def delete():
	entry.delete(0,END)
	
def backspace():
	entry.delete(len(entry.get())-1,END)	



entry= Entry(root)
entry.pack()




del_but = Button(root,text="delete",command=delete)
bs_but = Button(root,text="back space",command=backspace)


del_but.pack()
bs_but.pack()








root.config(background="#00ffff")

root.mainloop()



		