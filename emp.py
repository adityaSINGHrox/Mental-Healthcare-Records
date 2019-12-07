import proj as p
from tkinter import *
e = p.Employee()



def employee():
	editor = Tk()
	editor.title('employee')
	editor.geometry(p.dimen)


	button = Button(editor, text='exit', width=10, command=editor.destroy)
	button.grid(row = 18, column = 0, columnspan = 2, pady = 10,padx = 20, ipadx = 130)

	global EID,Ename,phno,address,job_des,sal,delete_box

	EID = Entry(editor, width = 30)
	EID.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

	Ename = Entry(editor, width = 30)
	Ename.grid(row = 1, column = 1)

	phno = Entry(editor, width = 30)
	phno.grid(row = 2, column = 1)

	address = Entry(editor, width = 30)
	address.grid(row = 3, column = 1)

	job_des = Entry(editor, width = 30)
	job_des.grid(row = 4, column = 1)

	sal = Entry(editor, width = 30)
	sal.grid(row = 5, column = 1)

	delete_box = Entry(editor, width = 30)
	delete_box.grid(row = 9, column = 1, pady = 5)

	#create text box labels
	EID_label = Label(editor, text = "EID")
	EID_label.grid(row = 0,column = 0, pady = (10,0))

	Ename_label = Label(editor, text = "Ename")
	Ename_label.grid(row = 1,column = 0)

	phno_label = Label(editor, text = "phono")
	phno_label.grid(row = 2,column = 0)

	address_label = Label(editor, text = "Address")
	address_label.grid(row = 3,column = 0)

	job_des_label = Label(editor, text = "job_des")
	job_des_label.grid(row = 4,column = 0)

	sal_label = Label(editor, text = "sal")
	sal_label.grid(row = 5,column = 0)

	delete_box_label = Label(editor, text = "id number")
	delete_box_label.grid(row = 9 , column =0, pady =5)


	submit_btn = Button(editor, text = "add record to database", command = submit)
	submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

	query_btn = Button(editor, text = "show records", command = display)
	query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 137)


	delete_btn = Button(editor, text = "delete records", command = delete)
	delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 136)


	edit_btn = Button(editor, text = "update records", command = update)
	edit_btn.grid(row = 17, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 143)

def submit():
    eid = EID.get()
    ename = Ename.get()
    pphno = phno.get()
    addr = address.get()
    job_desc = job_des.get()
    ssal = sal.get()
    e.insertVal(eid,ename,pphno,addr,job_desc,ssal)
    pass

def delete():
    eid = delete_box.get()
    e.deleteVal(eid)
    pass

def update():
    eid = EID.get()
    ename = Ename.get()
    pphno = phno.get()
    addr = address.get()
    job_desc = job_des.get()
    ssal = sal.get()
    oldeid = delete_box.get()
    e.updateVal(oldeid,eid,ename,pphno,addr,job_desc,ssal)

    pass

def display():
    e.showTable()
    pass
