from tkinter import *
#:from tkinter import canvas


root = Tk()


def add():
	listb.insert(listb.size(),entry.get())
	entry.delete(0,END)
	label = Label(root,text=entry.get())
	label.pack()
	

	
def delete():
	for index in reversed(listb.curselection()):
		listb.delete(index)
	
	



listb = Listbox(root,bg="#f7ffde",selectmode=MULTIPLE)
listb.pack()

entry = Entry(root)
entry.pack()

add_but = Button(root,command=add,text="add")
add_but.pack()

del_but = Button(root,command=delete,text="delete")
del_but.pack()




listb.config(height=listb.size())

root.mainloop()