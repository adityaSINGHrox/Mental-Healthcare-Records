import proj as w
from tkinter import *

p = w.Prescription()

def prescription():
	ditor = Tk()
	ditor.title('prescription')
	ditor.geometry(w.dimen)

	button = Button(ditor, text='exit', width=10, command=ditor.destroy)
	button.grid(row = 18, column = 0, columnspan = 2, pady = 10,padx = 20, ipadx = 130)

	global EID,PID,MID,DI_ID,M_name,quantity,delete_box

	EID = Entry(ditor, width = 30)
	EID.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

	PID = Entry(ditor, width = 30)
	PID.grid(row = 1, column = 1)

	MID = Entry(ditor, width = 30)
	MID.grid(row = 2, column = 1)

	DI_ID = Entry(ditor, width = 30)
	DI_ID.grid(row = 3, column = 1)

	M_name = Entry(ditor, width = 30)
	M_name.grid(row = 4, column = 1)

	quantity = Entry(ditor, width = 30)
	quantity.grid(row = 5, column = 1)

	delete_box = Entry(ditor, width = 30)
	delete_box.grid(row = 9, column = 1, pady = 5)

	#create text box labels
	EID_label = Label(ditor, text = "EID")
	EID_label.grid(row = 0,column = 0, pady = (10,0))

	PID_label = Label(ditor, text = "PID")
	PID_label.grid(row = 1,column = 0)

	MID_label = Label(ditor, text = "MID")
	MID_label.grid(row = 2,column = 0)

	DI_ID_label = Label(ditor, text = "DI_ID")
	DI_ID_label.grid(row = 3,column = 0)

	M_name_label = Label(ditor, text = "M_name")
	M_name_label.grid(row = 4,column = 0)

	quantity_label = Label(ditor, text = "quantity")
	quantity_label.grid(row = 5,column = 0)

	delete_box_label = Label(ditor, text = "mid number")
	delete_box_label.grid(row = 9 , column =0, pady =5)


	submit_btn = Button(ditor, text = "add record to database", command = submit)
	submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

	query_btn = Button(ditor, text = "show records", command = display)
	query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 137)


	delete_btn = Button(ditor, text = "delete records", command = delete)
	delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 136)


	edit_btn = Button(ditor, text = "update records", command = update)
	edit_btn.grid(row = 17, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 143)


def delete():
    mid = MID.get()
    p.deleteVal(mid)
    pass

def submit():
    mid = MID.get()
    pid = PID.get()
    eid = EID.get()
    did = DI_ID.get()
    mname = M_name.get()
    quant = quantity.get()
    p.insertVal(mid,pid,eid,did,mname,quant)
    pass

def update():
    oldmid = delete_box.get()
    mid = MID.get()
    pid = PID.get()
    eid = EID.get()
    did = DI_ID.get()
    mname = M_name.get()
    quant = quantity.get()
    p.updateVal(oldmid,mid,pid,eid,did,mname,quant)
    pass

def display():
    p.showTable()
    pass

'''
root = Tk()
root.geometry(w.dimen)
prescription_btn = Button(root, text = "prescription",width = 20, command = prescription)
prescription_btn.place(relx = 0.1, rely = 0.5, anchor = 'n')
root.mainloop()
'''
