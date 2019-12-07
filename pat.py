import proj as w
from tkinter import *

p = w.Pateint()

def patient():
	pat = Tk()
	pat.title('patient')
	pat.geometry(w.dimen)


	button = Button(pat, text='exit', width=10, command=pat.destroy)
	button.grid(row = 18, column = 0, columnspan = 2, pady = 10,padx = 20, ipadx = 130)

	global PID,Pname,phno,address,D_o_ad,D_o_dis,delete_box

	PID = Entry(pat, width = 30)
	PID.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

	Pname = Entry(pat, width = 30)
	Pname.grid(row = 1, column = 1)

	phno = Entry(pat, width = 30)
	phno.grid(row = 2, column = 1)

	address = Entry(pat, width = 30)
	address.grid(row = 3, column = 1)

	D_o_ad = Entry(pat, width = 30)
	D_o_ad.grid(row = 4, column = 1)

	D_o_dis = Entry(pat, width = 30)
	D_o_dis.grid(row = 5, column = 1)

	delete_box = Entry(pat, width = 30)
	delete_box.grid(row = 9, column = 1, pady = 5)

	#create text box labels
	PID_label = Label(pat, text = "PID")
	PID_label.grid(row = 0,column = 0, pady = (10,0))

	Pname_label = Label(pat, text = "Pname")
	Pname_label.grid(row = 1,column = 0)

	phno_label = Label(pat, text = "phono")
	phno_label.grid(row = 2,column = 0)

	address_label = Label(pat, text = "Address")
	address_label.grid(row = 3,column = 0)

	D_o_dis_label = Label(pat, text = "D_o_dis")
	D_o_dis_label.grid(row = 4,column = 0)

	D_o_ad_label = Label(pat, text = "D_o_ad")
	D_o_ad_label.grid(row = 5,column = 0)

	delete_box_label = Label(pat, text = "id number")
	delete_box_label.grid(row = 9 , column =0, pady =5)


	submit_btn = Button(pat, text = "add record to database", command = submit)
	submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

	query_btn = Button(pat, text = "show records", command = display)
	query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 137)


	delete_btn = Button(pat, text = "delete records", command = delete)
	delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 136)


	edit_btn = Button(pat, text = "update records", command = edit)
	edit_btn.grid(row = 17, column = 0, columnspan = 2, pady = 10, padx = 20, ipadx = 143)





def delete():
    pid = delete_box.get()
    p.deleteVal(pid)
    pass

def submit():
    pid = PID.get()
    pname = Pname.get()
    addr = address.get()
    pphno = phno.get()
    date_admit = D_o_ad.get()
    date_exit = D_o_dis.get()
    p.insertVal(pid,pname,addr,pphno,date_admit,date_exit)
    pass

def edit():
    oldpid = delete_box.get()
    pid = PID.get()
    pname = Pname.get()
    addr = address.get()
    pphno = phno.get()
    date_admit = D_o_ad.get()
    date_exit = D_o_dis.get()
    p.updateVal(oldpid,pid,pname,addr,pphno,date_admit,date_exit)

    pass

def display():
    p.showTable()
    pass
'''
root = Tk()
root.geometry(w.dimen)
patient_btn = Button(root, text = "patient",width = 20, command = patient)
patient_btn.place(relx = 0.1, rely = 0.3, anchor = 'n')

root.mainloop()
'''
