import proj as p
from tkinter import *

d = p.Disease()


def disease():
	edi = Tk()
	edi.title('disease')
	edi.geometry(p.dimen)

	global DI_ID,D_name,delete_box

	button = Button(edi, text='exit', width=10, command=edi.destroy)
	button.grid(row = 18, column = 0, columnspan = 2, pady = 10,padx = 20, ipadx = 130)

	DI_ID = Entry(edi, width = 30)
	DI_ID.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

	D_name = Entry(edi, width = 30)
	D_name.grid(row = 1, column = 1)

	delete_box = Entry(edi, width = 30)
	delete_box.grid(row = 9, column = 1, pady = 5)

	DI_ID_label = Label(edi, text = "DI_ID")
	DI_ID_label.grid(row = 0,column = 0, pady = (10,0))

	D_name_label = Label(edi, text = "Dname")
	D_name_label.grid(row = 1,column = 0)


	delete_box_label = Label(edi, text = "id number")
	delete_box_label.grid(row = 9 , column =0, pady =5)


	submit_btn = Button(edi, text = "add record to database", command = submit)
	submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

	query_btn = Button(edi, text = "show records", command = display)
	query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 137)


	delete_btn = Button(edi, text = "delete records", command = delete)
	delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 136)


	edit_btn = Button(edi, text = "update records", command = update)
	edit_btn.grid(row = 17, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 143)


def delete():
    did = delete_box.get()
    d.deleteVal(did)
    pass

def submit():
    did = DI_ID.get()
    dis = D_name.get()
    d.insertVal(did,dis)
    pass

def update():
    did = DI_ID.get()
    dis = D_name.get()
    d.updateVal(did,dis)
    pass

def display():
    d.showTable()
    pass

'''
root = Tk()
root.geometry(p.dimen)
disease_btn = Button(root, text = "disease", command = disease)
disease_btn.grid(row = 5, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 100)
root.mainloop()
'''
