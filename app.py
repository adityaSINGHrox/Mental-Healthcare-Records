import proj as p
from tkinter import *

e = p.Appointment()


def appointments():

	tor = Tk()
	tor.title('appointments')
	tor.geometry(p.dimen)

	global EID,PID,DATE_TIME,DI_ID,delete_box

	button = Button(tor, text='exit', width=10, command=tor.destroy)
	button.grid(row = 18, column = 0, columnspan = 2, pady = 10,padx = 20, ipadx = 130)

	EID = Entry(tor, width = 30)
	EID.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

	PID = Entry(tor, width = 30)
	PID.grid(row = 1, column = 1)

	DATE_TIME = Entry(tor, width = 30)
	DATE_TIME.grid(row = 2, column = 1)

	DI_ID = Entry(tor, width = 30)
	DI_ID.grid(row = 3, column = 1)

	delete_box = Entry(tor, width = 30)
	delete_box.grid(row = 9, column = 1, pady = 5)

	#create text box labels
	EID_label = Label(tor, text = "EID")
	EID_label.grid(row = 0,column = 0, pady = (10,0))

	PID_label = Label(tor, text = "PID")
	PID_label.grid(row = 1,column = 0)

	DATE_TIME_label = Label(tor, text = "DATE_TIME")
	DATE_TIME_label.grid(row = 2,column = 0)

	DI_ID_label = Label(tor, text = "DI_ID")
	DI_ID_label.grid(row = 3,column = 0)

	delete_box_label = Label(tor, text = "old pid number")
	delete_box_label.grid(row = 9 , column =0, pady =5)


	submit_btn = Button(tor, text = "add record to database", command = submit)
	submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

	query_btn = Button(tor, text = "show records", command = display)
	query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 137)


	delete_btn = Button(tor, text = "delete records", command = delete)
	delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 136)


	edit_btn = Button(tor, text = "update records", command = update)
	edit_btn.grid(row = 17, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 143)

def submit():
    pid = PID.get()
    eid = EID.get()
    date = DATE_TIME.get()
    did = DI_ID.get()
    e.insertVal(pid,eid,date,did)
    pass

def delete():

	eid = EID.get()
	pid = PID.get()
	did = DI_ID.get()
	e.deleteVal(eid,pid,did)
	pass

def update():
	oldpid = delete_box.get()
	pid = PID.get()
	eid = EID.get()
	date = DATE_TIME.get()
	did = DI_ID.get()
	e.updateVal(oldpid,pid,eid,date,did)
	pass

def display():
	e.showTable()
	pass

'''
root = Tk()
root.geometry(p.dimen)
appointments_btn = Button(root, text = "appointments",width = 20, command = appointments)
appointments_btn.place(relx = 0.1, rely = 0.4, anchor = 'n')

root.mainloop()
'''
