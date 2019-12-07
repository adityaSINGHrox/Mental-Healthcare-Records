import  mysql.connector
import datetime
import os
os.system('clear')
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "aditya99",
    database = "mhs"
)

c = mydb.cursor()

dimen = "500x500+120+120"
height = 500
width = 500

class Disease:

    def showTable(self):
        c.execute("select * from mhs.disease")
        for db in c:
            print(db)

    def insertVal(self,did,dname):
        temp = (
        "insert into mhs.disease(did,dname)"
        "values(%s,%s)"
        )
        data = (did,dname)
        c.execute(temp,data)
        mydb.commit()

    def deleteVal(self,did):
        querry = "delete from mhs.disease where did = %s"
        c.execute(querry,(did,))
        mydb.commit()

    def updateVal(self,did,dname):
        querry = "update mhs.disease set dname = %s where  did = %s"
        c.execute(querry,(dname,did))
        mydb.commit()

class Appointment:

    def showTable(self):
        c.execute("select * from mhs.appointment")
        for db in c:
            print(db)

    def insertVal(self,pid,eid,date,did):# eg now = datetime.date(2109,3,23)
        temp = (
        "insert into mhs.appointment(pid,eid,date,did)"
        "values(%s,%s,%s,%s)"
        )
        data = (pid,eid,date,did)
        c.execute(temp,data)
        mydb.commit()

    def deleteVal(self,pid,eid,did):
        querry = "delete from mhs.appointment where pid = %s and eid = %s and did = %s"
        c.execute(querry,(pid,eid,did,))
        mydb.commit()

    def updateVal(self,oldpid,newpid,neweid,newdate,newdid):
        querry = "update mhs.appointment set pid =%s,eid =%s,date = %s,did = %s where  pid = %s"
        c.execute(querry,(newpid,neweid,newdate,newdid,oldpid))
        mydb.commit()

class Employee:

    def showTable(self):
        c.execute("select * from mhs.emp")
        for db in c:
            print(db)

    def insertVal(self,eid,ename,phno,addr,jobtype,sal):
        temp = (
        "insert into mhs.emp(eid,ename,phno,addr,job_desc,sal)"
        "values(%s,%s,%s,%s,%s,%s)"
        )
        data = (eid,ename,int(phno),addr,jobtype,int(sal))
        c.execute(temp,data)
        mydb.commit()

    def deleteVal(self,eid):
        querry = "delete from mhs.emp where eid = %s"
        c.execute(querry,(eid,))
        mydb.commit()

    def updateVal(self,oldeid,neweid,newename,newphno,newaddr,newjobtype,sal):
        querry = "update mhs.emp set eid = %s,ename =%s,phno= %s,addr =%s,job_desc = %s,sal =%s where eid = %s"
        c.execute(querry,(neweid,newename,newphno,newaddr,newjobtype,sal,oldeid))
        mydb.commit()

class Pateint:

    def showTable(self):
        c.execute("select * from mhs.patient")
        for db in c:
            print(db)

    def insertVal(self,pid,pname,addr,phno,date_admit,date_exit):
        temp = (
        "insert into mhs.patient(pid,pname,addr,phno,doa,dod)"
        "values(%s,%s,%s,%s,%s,%s)"
        )
        data = (pid,pname,addr,phno,date_admit,date_exit)
        c.execute(temp,data)
        mydb.commit()

    def deleteVal(self,pid):
        querry = "delete from mhs.patient where pid = %s"
        c.execute(querry,(pid,))
        mydb.commit()

    def updateVal(self,oldpid,newpid,newpname,newaddr,newphno,newdate_admit,newdate_exit):
        querry = "update mhs.patient set pid =%s,pname =%s,addr =%s,phno =%s,doa =%s,dod =%s where pid =%s"
        c.execute(querry,(newpid,newpname,newaddr,newphno,newdate_admit,newdate_exit,oldpid))
        mydb.commit()

class Prescription:

    def showTable(self):
        c.execute("select * from mhs.prescription")
        for db in c:
            print(db)

    def insertVal(self,mid,pid,eid,did,mname,quant):
        temp = (
        "insert into  mhs.prescription(mid,pid,eid,did,mname,quant)"
        "values(%s,%s,%s,%s,%s,%s)"
        )
        data = (mid,pid,eid,did,mname,int(quant))
        c.execute(temp,data)
        mydb.commit()

    def deleteVal(self,mid):
        querry = "delete from  mhs.prescription where mid = %s"
        c.execute(querry,(mid,))
        mydb.commit()

    def updateVal(self,oldmid,newmid,newpid,neweid,newdid,newmname,newquant):
        querry = "update  mhs.prescription set mid=%s,pid=%s,eid=%s,did=%s,mname=%s,quant=%s where mid = %s"
        data = (newmid,newpid,neweid,newdid,newmname,int(newquant),oldmid,)
        c.execute(querry,data)
        mydb.commit()
