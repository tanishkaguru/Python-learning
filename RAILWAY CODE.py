import mysql.connector as m
mydb = m.connect(host='localhost',user='root',passwd='1234',database='railway')
cu = mydb.cursor() 
if mydb.is_connected():
    print("SUCCESSFULLY CONNECTED")
mydb.autocommit = True
cu.execute('USE RAILWAY')

s = "create table if not exists user_accounts(fname varchar(100) NOT NULL,lname varchar(100) NOT NULL,user_name varchar(100) primary key,password varchar(100) NOT NULL,phno int(15),gender varchar(50),dob date NOT NULL,age int(4))"
cu.execute(s)
s = "create table if not exists train(train_no int(5) NOT NULL,train_name varchar(100) NOT NULL,starting_station varchar(100) NOT NULL, destination varchar(100) NOT NULL,platform_no int(4) NOT NULL,arrival_time time NOT NULL,departure_time time NOT NULL,seats_available int(3) NOT NULL,Date date NOT NULL)"
cu.execute(s)
s = "create table if not exists ticket(user_name varchar(100) NOT NULL,phno int(10) NOT NULL,train_no int(5) NOT NULL,status varchar(100) NOT NULL,seats_available int(3) NOT NULL)"
cu.execute(s)


s="insert into train values(1,'CHENNAI EXPRESS','DELHI','CHENNAI',1,'09:00:00','09:15:00',60,'2022-02-12')"
cu.execute(s)
s="insert into train values(2,'JAMMU EXPRESS','DELHI','JAMMU',2,'09:10:00','09:20:00',60,'2022-02-12')"
cu.execute(s)
s="insert into train values(3,'KOLKATA EXPRESS','DELHI','KOLKATA',3,'13:10:00','13:20:00',60,'2022-02-13')"
cu.execute(s)
s="insert into train values(4,'GEMINI RAILWAY','PUNJAB','GUJARAT',1,'09:10:00','09:20:00',60,'2022-02-14')"
cu.execute(s)
s="insert into train values(4,'GEMINI RAILWAY','DELHI','GUJARAT',4,'07:10:00','07:20:00',60,'2022-02-18')"
cu.execute(s)
s="insert into train values(2,'JAMMU EXPRESS','PUNJAB','JAMMU',2,'09:10:00','09:20:00',60,'2022-02-18')"
cu.execute(s)
s="insert into train values(1,'CHENNAI EXPRESS','GUJARAT','CHENNAI',3,'09:00:00','09:15:00',60,'2022-02-16')"
cu.execute(s)
s="insert into train values(1,'CHENNAI EXPRESS','MUMBAI','CHENNAI',4,'09:00:00','09:15:00',60,'2022-02-17')"
cu.execute(s)
s="insert into train values(3,'KOLKATA EXPRESS','JAMMU','KOLKATA',1,'09:00:00','09:15:00',60,'2022-02-12')"
cu.execute(s)
s="insert into train values(4,'GEMINI RAILWAY','MUMBAI','GUJARAT',4,'09:10:00','09:20:00',60,'2022-02-18')"
cu.execute(s)



def ticket_booking():
    st=input('FROM (station):')
    dt=input('TO (station):')
    st=st.upper()
    dt=dt.upper()
    se="select * from train where starting_station='{}' and destination='{}'".format(st,dt)
    cu.execute(se)
    dat=cu.fetchall()
    dat=list(dat)
    print('\n')
    print('..........................................................................................................................................................')
    print('HERE ARE THE RESULTS THAT MATCH YOUR SEARCH:')
    print('..........................................................................................................................................................')
    for i in dat:
        print ('Train no:'+str(i[0]),'Train name:'+i[1],'Starting Station:'+i[2],'Destination:'+i[3],'Platform no.:'+str(i[4]),'Arrival time:'+str(i[5]),'Departure time:'+str(i[6]),'\n','Seats available:'+str(i[7]),'Date:'+str(i[8]),sep='   ')
    print('..........................................................................................................................................................')
    print('\n')
    nm=input("Enter your user name: ")
    phno=int(input("Enter your phone number: "))
    no=int(input("Enter the train no. to book ticket: "))
    da=input('Enter date to book ticket: ')
    se="select * from train where train_no='{}' and starting_station='{}' and destination='{}' and date='{}'".format(no,st,dt,da)
    cu.execute(se)
    dat=cu.fetchone()
    dat=list(dat)
    sno=dat[7]-1
    if dat[7]==0:
        print('TICKET NOT AVAILABLE')
    else:
        s="insert into ticket values('{}','{}','{}','{}','{}')".format(nm,phno,no,'SUCCESSFUL',sno)
        cu.execute(s)
        print("BOOKING SUCCESSFUL")
        s="update train set seats_available=seats_available-1 where train_no='{}' and starting_station='{}' and destination='{}' and date='{}'".format(no,st,dt,da)
        cu.execute(s)


def ticket_checking():
    print("1. Yes")
    print("2. No")
    ch = int(input("Do you wish to continue? "))
    if ch==1:
        nm=input('enter your username:')
        try:
            se="select * from ticket where user_name='{}'".format(nm)
            cu.execute(se)
            dat=cu.fetchall()
            if dat==[]:
                print("TICKET DOES NOT EXIST")
            Data=list(dat)
            for i in Data:
                a=['USERNAME','PHONE NUMBER','TRAIN NO.','TICKET STATUS','SEATS_AVAILABLE']
                print(a[0],':',i[0].upper())
                print(a[1],':',i[1])
                print(a[2],':',i[2])
                print(a[3],':',i[3].upper())
                print(a[4],':',i[4])
        except:
            print('TICKET DOES NOT EXISTS')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')


def ticket_cancelling():
    ch=int(input("Do you wish to continue? (1.YES 2.NO) "))
    if ch==1:
        nm=input("ENTER YOUR USER NAME: ")
        no=input("ENTER TRAIN NO OF TICKET YOU WISH TO DELETE: ")
        s="delete from ticket where user_name='{}' and train_no='{}'".format(nm,no)
        cu.execute(s)
        print("YOUR TICKET IS CANCELLED")
        s="update train set seats_available=seats_available+1 where train_no='{}'".format(no)
        cu.execute(s)
    elif ch==2:
        print("THANK YOU")
    else:
        print("ERROR")


def checking1():
    f = input("First name: ")
    l = input("Last name: ")
    u = input("User name: ")
    x = input("Enter password: ")
    y = input("Re-enter password: ")
    p = input("Enter phone no: ")
    print("M=male, F=female, N=not to mention")
    gender=input("Enter your Gender: ")
    Gender=gender.upper()
    z = {'M':'MALE','F':'FEMALE','N':'NOT TO MENTION'}
    r = z[Gender]
    dat = input("Enter date(yyyy-mm-dd): ")
    age = int(input("Enter your age: "))
    if x==y:
        try:
            d="insert into user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,l,u,x,p,r,dat,age)
            cu.execute(d)
            print("WELCOME",f,l)
            return True
        except:
            print("PASSWORDS DO NOT MATCH")
            return False
    else:
        print("PASSWORDS DO NOT MATCH")
        return False

def checking2():
    a=input('USERNAME:')
    b=input('PASSWORD:')
    try:
        c1="select fname,lname from user_accounts where user_name='{}' and password='{}'".format(a,b)
        cu.execute(c1)
        data1=cu.fetchone()
        data1=list(data1)
        data2=data1[0]+' '+data1[1]
        print('HELLO',data2)
        return True
    except:
        print('ACCOUNT DOES NOT EXIST')
        return False
 
def checking3():
    a = input("Enter username: ")
    b = input("Enter password: ")
    try:
        c2 = "delete from user_accounts where user_name='{}' and password = '{}'".format(a,b)
        cu.execute(c2)
        return True
    except:
        print("ACCOUNT DOES NOT EXIST")
        return False
 
def checking4():
    a=input('USERNAME:')
    b=input('PASSWORD:')
    try:
        c1="select fname,lname,phno,gender,dob,age from user_accounts where user_name='{}' and password='{}'".format(a,b)
        cu.execute(c1)
        dat=cu.fetchall()[0]
        dat=list(dat)
        x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
        print(x[0],':',dat[0])
        print(x[1],':',dat[1])
        print(x[2],':',dat[2])
        print(x[3],':',dat[3])
        print(x[4],':',dat[4])
        print(x[5],':',dat[5])
        return True
    except:
        ("ACCOUNT DOES NOT EXIST")
        return False


def menu():
    ch=1
    while ch==1:
        print('\n')
        print('______________________________________________')
        print("WELCOME TO ONLINE RAILWAY RESERVATION SYSTEM")
        print('______________________________________________')
        print('1.SIGN IN')
        print('2.REGISTER NEW ACCOUNT')
        print('3.DELETE ACCOUNT')
        print('4.EXIT')
        print('______________________________________________')
        print('\n')
        ch1=int(input('ENTER YOUR CHOICE:'))
        if ch1==1:
            a=checking2()
            if a==True:
                print('WELCOME')
                main()
            else:
                continue
        elif ch1==2:
            b=checking1()
            if b==True:
                main()
            else:
                print('ACCOUNT ALREADY EXISTS')
                continue
        elif ch1==3:
            c=checking3()
            if c==True:
                print('ACCOUNT DELETED')
                continue
            else:
                print('YOUR PASSWORD OR USERNAME IS INCORRECT')
                continue
        elif ch1==4:
            print('THANK YOU')
            break
        else:
            print("ERROR")
            break


def main():
    print("1. Yes")
    print("2. No")
    ans = int(input("Do you wish to continue? "))
    while (ans==1):
        print('\n')
        print('__________________________')
        print("   CHOICES")
        print('__________________________')
        print("1. TICKET BOOKING")
        print("2. TICKET CHECKING")
        print("3. TICKET CANCELLING")
        print("4. CHECK ACCOUNT DETAILS")
        print("5. LOG OUT")
        print('__________________________')
        print('\n')
        ch = int(input("Enter your choice: "))
        if ch==1:
            ticket_booking()
        elif ch==2:
            ticket_checking()
        elif ch==3:
            ticket_cancelling()
        elif ch==4:
            checking4()
        elif ch==5:
            print("Thank you")
            break
        else:
            print("Error")

menu()