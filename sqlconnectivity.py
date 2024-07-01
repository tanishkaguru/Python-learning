import mysql.connector as m
mydb=m.connect(host='localhost',user='root',passwd='1234',database='railway')
cu=mydb.cursor()
if mydb.is_connected():
    print("successfully connected")

#5.
s="create table if not exists company(CNO int(3) primary key,CNAME varchar(100),ADDRESS varchar(50),NOOFEMPLOYEES int(6),ANNUALTURN float(10,2))"
cu.execute(s)

def q1():
    n=int(input("enter no of entries: "))
    for i in range(n):
        sno=int(input("enter company no:"))
        sname=input("enter company name:")
        ad=input("enter the address:")
        iname=int(input("enter the no of employees:"))
        iprice=float(input("enter annual turnover of company:"))
        s="insert into company values('{}','{}','{}','{}','{}')".format(sno,sname,ad,iname,iprice)
        cu.execute(s)

def q2():
    s="select * from company"
    cu.execute(s)
    dat=cu.fetchall()
    for i in dat:
        print(i)

def q3():
    s="select cname from company where annualturn>1000000.00"
    cu.execute(s)
    dat=cu.fetchall()
    for i in dat:
        print(i)

def q4():
    s="select * from company where noofemployees<10"
    cu.execute(s)
    dat=cu.fetchall()
    for i in dat:
        print(i)

def main():
    ch=True
    while ch==True:
        print("1. insert rows in this table")
        print("2. display all rows")
        print("3. TO DISPLAY THE NAMES OF THE COMPANIES WHOSE TURNOVER IS MORE THAN 10 LAKH")
        print("4. TO DISPLAY THE DETAILS OF THE COMPANIES WHO HAVE EMPLOYEES LESS THAN 10")
        print("5. exit")
        c=int(input("enter your choice: "))
        if c==1:
            q1()
        if c==2:
            q2()
        if c==3:
            q3()
        if c==4:
            q4()
        if c==5:
            print("thank you")
            ch=False
main()