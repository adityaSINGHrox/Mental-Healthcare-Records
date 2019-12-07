
from tkinter import *
from PIL import ImageTk,Image
import proj as p
import app as a
import dis as d
import emp as e
import pat as pp
import pres as pr




root = Tk()
root.title('MENTALHEALTHCARE')
root.geometry(p.dimen)

myLabel1 = Label(root, text = "MENTAL HEALTH CARE", bg = 'blue', font = 'Times 16 bold italic')
myLabel1.grid()

background_image = PhotoImage(file='mh.png')
background_label =Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

myLabel1 = Label(root, text = "MENTAL HEALTH CARE", bg = 'blue', font = 'Times 16 bold italic')
myLabel1.grid(padx = 0.5)

employee_btn = Button(root, text = "employee",width = 20, command = e.employee)
employee_btn.place(relx = 0.1, rely = 0.2, anchor = 'n')

patient_btn = Button(root, text = "patient",width = 20, command = pp.patient)
patient_btn.place(relx = 0.1, rely = 0.3, anchor = 'n')


appointments_btn = Button(root, text = "appointments",width = 20, command = a.appointments)
appointments_btn.place(relx = 0.1, rely = 0.4, anchor = 'n')


prescription_btn = Button(root, text = "prescription",width = 20, command = pr.prescription)
prescription_btn.place(relx = 0.1, rely = 0.5, anchor = 'n')


disease_btn = Button(root, text = "disease",width = 20, command = d.disease)
disease_btn.place(relx = 0.1, rely = 0.6, anchor = 'n')

button = Button(root, text='exit', width=25, command=root.destroy)
button.place(relx = 0.1, rely = 0.8,anchor = 'n')

root.mainloop()
