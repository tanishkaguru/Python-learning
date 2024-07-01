import mysql.connector as m
mydb=m.connect(host='localhost',user='root',password='1234',database='railway')
cu=mydb.cursor()
if mydb.is_connected():
    print("successfully connected")

#1.Create a student(adno,name,address,Avg,Dob) table 
def q1():
    s="create table if not exists STUDENT(adno int(3) primary key,name varchar(100) not null,address varchar(200),marks int(10),dob date)"
    cu.execute(s)


#2.Alter table to add  a new column Phoneno. Now add 5 records
def q2():
    s="alter table STUDENT add phoneno int(10)"
    cu.execute(s)
    for i in range (5):
        adno=int(input("enter adno: "))
        name=input("enter name: ")
        add=input("enter address: ")
        avg=int(input("enter avg: "))
        dob=input("enter DOB: ")
        phno=int(input("enter phone no: "))
        s="insert into STUDENT values('{}','{}','{}','{}','{}','{}')".format(adno,name,add,avg,dob,phno)
        cu.execute(s)

#3.Update a particular student's Avg mks. (and view table)
def q3():
    adno=input("enter adno to update marks: ")
    avg=int(input("enter avg: "))
    s="update STUDENT set marks='{}' where adno='{}'".format(avg,adno)
    cu.execute(s)
    s="select * from STUDENT"
    cu.execute(s)
    DAT=cu.fetchall()
    for i in DAT:
        print(i)


#4.Delete a particular student
def q4():
    adno=int(input("enter adno to delete student record: "))
    s="delete from STUDENT where adno='{}'".format(adno)
    cu.execute(s)


#5.Find out the Max , Min and Average marks scored by students.
def q5():
    s="select max(marks) 'maximum_marks',min(marks) 'minimum_marks', avg(marks) 'average marks' from STUDENT"
    cu.execute(s)
    dat=cu.fetchall()
    print(dat)


def menu():
    b=True
    while b==True:
        print('choices:')
        print("1.Create a student(adno,name,address,Avg,Dob) table")
        print("2.Alter table to add  a new column Phoneno. Now add 5 records")
        print("3.Update a particular student's Avg mks. (and view table) ")
        print("4.Delete a particular student")
        print("5.Find out the Max , Min and Average marks scored by students")
        print("6. exit")
        c=int(input('enter choice: '))
        if c==1:
            q1()
        if c==2:
            q2()
        if c==3:
            q3()
        if c==4:
            q4()
        if c==5:
            q5()
        if c==6:
            b=False

menu()