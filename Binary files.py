#Q1
'''(A)Write menu-driven program using functions for the following operations
on a file of Employees having [Empno,Name,Salary,Deptt,Phone]:-
1. Create
2. Display entire file
3. Search for an employee whose empno is given.
4. Search for an employee whose name is given
5. Display employees of a given deptt , also count them.
6. Search for an employee whose phone number is given.
7. Search for an employee whose Salary is highest.
8. Delete an employee whose empno is given(don’t use another list/file).
9. Delete employees whose Salary <50000.
10. Append a new employee to the file.
11. Update the salary of employee whose empno is given, by 10%
bonus.(Don’t use another file/list.)

'''
import pickle
def create():
    f = open('emp.dat','wb')
    while True:
        emp = eval(input("Enter Emp no.,Name,Salary,Deptt and Phone: "))
        pickle.dump(emp,f)
        ans = input("Want to continue?")
        if ans in 'Nn':
            break
    f.close()

'''
Enter choice(1-12): 1
Enter Emp no.,Name,Salary,Deptt and Phone: [1,'abc',10000,'advertising',123456789]
Want to contine?y
Enter Emp no.,Name,Salary,Deptt and Phone: [2,'xyz',15000,'advertising',123636789] 
Want to contine?y
Enter Emp no.,Name,Salary,Deptt and Phone: [3,'csb',100000,'sales',453456789]      
Want to contine?n'''
        
def display():
    f = open('emp.dat','rb')
    try:
        while True:
            emp = pickle.load(f)
            print(emp)
    except EOFError:
        f.close()

'''
Enter choice(1-12): 2
[1, 'abc', 10000, 'advertising', 123456789]
[2, 'xyz', 15000, 'advertising', 123636789]
[3, 'csb', 100000, 'sales', 453456789]
'''

def search_empno():
    f = open('emp.dat','rb')
    found = False
    num = int(input("Enter the  employee no to search for: "))
    try:
        while True:
            emp = pickle.load(f)
            if emp[0] == num:
                found = True
                print("Found",emp)
    except EOFError:
        f.close()
    if found == False:
        print("Not found")

'''
Enter choice(1-12): 3
Enter the  employee no to search for: 2
Found [2, 'xyz', 15000, 'advertising', 123636789]
'''

def search_name():
    f = open('emp.dat','rb')
    n = input("Enter employee name to search: ")
    n = n.strip()
    n = n.lower()
    found = False
    try:
        while True:
            emp = pickle.load(f)
            if emp[1].lower()==n:
                found = True
                print("Found",emp)
    except EOFError:
        f.close()
    if found == False:
        print("Not found")

'''
Enter choice(1-12): 4
Enter employee name to search: abc 
Found [1, 'abc', 10000, 'advertising', 123456789]
'''

def search_deptt():
    f = open('emp.dat','rb')
    n = input("Enter department name: ")
    n = n.strip()
    n = n.lower()
    c = 0
    try:
        while True:
            emp = pickle.load(f)
            if emp[3].lower()==n:
                c+=1
                print(emp)
                print("Total no of employees in",n,"are: ",c)
    except EOFError:
        f.close()

'''
Enter choice(1-12): 5
Enter department name: advertising
[1, 'abc', 10000, 'advertising', 123456789]
Total no of employees' of advertising are 1
[2, 'xyz', 15000, 'advertising', 123636789]
Total no of employees' of advertising are 2
'''

def search_phone():
    f = open("emp.dat",'rb')
    n = int(input("Enter employee's phone no. to search: "))
    found = False
    try:
        while True:
            emp = pickle.load(f)
            if emp[4]==n:
                found = True
                print("Found",emp)
    except EOFError:
        f.close()
    if found == False:
        print("Not found")

'''
Enter choice(1-12): 6
Enter employee phone no to search for: 123456789
Found [1, 'abc', 10000, 'advertising', 123456789]
'''

def highsalary():
    f = open("emp.dat",'rb')
    h=0
    while True:
        try:
            emp=pickle.load(f)
            if emp[2]>h:
                h=emp[2]
                e=emp
        except EOFError:
            break
    print(h,'is the highest salary of',e)
    f.close()

'''
Enter choice(1-12): 7
100000 is the highest salary of [3, 'csb', 100000, 'sales', 453456789]
'''

def del_empno():
    n=int(input("enter emp no to delete: "))
    f = open("emp.dat",'rb')
    l=[]
    try:
        while True:
            e = pickle.load(f)
            l.append(e)
    except EOFError:
        f.close()
    for i in l:
        if i[0]==n:
            l.remove(i)
            break
    f=open("emp.dat",'wb')
    pickle.dump(l,f)
    f.close()
    display()

'''
Enter choice(1-12): 8
enter emp no to delete: 2
[1, 'abc', 10000, 'advertising', 123456789]
[3, 'csb', 100000, 'sales', 453456789]
'''

def del_empsalary():
    f = open("emp.dat",'rb')
    l=[]
    try:
        while True:
            e = pickle.load(f)
            l.append(e)
    except EOFError:
        f.close()
    f = open("emp.dat",'wb')
    for i in l:
        if i[2] > 50000:
            pickle.dump(i,f)
    f.close()
    display()

'''
Enter choice(1-12): 9
[3, 'csb', 100000, 'sales', 453456789]
'''


def append():
    f = open("emp.dat",'ab')
    while True:
        emp = eval(input("Enter Emp no.,Name,Salary,Deptt and Phone: "))
        pickle.dump(emp,f)
        ans = input("Want to continue?")
        if ans in 'Nn':
            break
    f.close()
    display()

'''
Enter choice(1-12): 10
Enter Emp no.,Name,Salary,Deptt and Phone: [4, 'xsb', 120000, 'sales', 4534123789]
Want to continue?n
[1, 'abc', 10000, 'advertising', 123456789]
[3, 'csb', 100000, 'sales', 453456789]
[4, 'xsb', 120000, 'sales', 4534123789]
'''

def update():
    f = open('emp.dat','rb')
    s = int(input("Enter empno whose salary is to be updated: "))
    l=[]
    try:
        while True:
            e = pickle.load(f)
            l.append(e)
            if e[0] == s:
                print("Found name= ",e[1])
                x = e[2] + (e[2]*(10/100))
    except EOFError:
        f.close()
    for i in l:
        if i[0]==s:
            i[2]=x
            break
    f=open("emp.dat",'wb')
    pickle.dump(l,f)
    f.close()
    display()

'''
Enter choice(1-12): 11
Enter empno whose salary is to be updated: 1
Found name=  abc
[1, 'abc', 11000.0, 'advertising', 123456789]
[3, 'csb', 100000, 'sales', 453456789]
[4, 'xsb', 120000, 'sales', 4534123789]
'''

def choices():
    print('Menu')
    print('1. Create')
    print('2. Display')
    print('3. Search with a given empno')
    print('4. Search with a given name')
    print('5. Display employees of given deptt.')
    print('6. Search with a given phone no.')
    print('7. Search for the highest salary')
    print('8. Delete an employee whose empno is given')
    print('9. Delete employees whose Salary <50000.')
    print('10. Append a new employee to the file.')
    print('11. Update the salary of employee whose empno is given by,10% bonus.')
    print('12. Exit')

def main():
    while True:
        choices()
        ch = input('Enter choice(1-12): ')
        
        if ch == '1':
            create()
            
        elif ch == '2':
            display()

        elif ch == '3':
            search_empno()
            
        elif ch == '4':
            search_name()

        elif ch == '5':
            search_deptt()

        elif ch == '6':
            search_phone()

        elif ch == '7':
            highsalary()

        elif ch == '8':
            del_empno()

        elif ch == '9':
            del_empsalary()

        elif ch == '10':
            append()

        elif ch == '11':
            update()

        elif ch == '12':
            print("Exit")
            break
        
        else:
            print('Invalid choice')
            
main() 

#Q2
'''(B) Write a menu-driven program using functions to store data about
students having adno,name,mark1,mark2,mark3 using dictionary .
1. Create
2. Display entire file
3. Search for a particular student whose adno is given.
4. Search,display & count students scoring above 90 in all 3 subjects.
5. Delete a student whose mark is below 40 in all 3 subjects.
6. Update a student’s mark1 by adding 5 grace marks.
7. exit
'''
import pickle
def create():
    f = open('stu.dat','wb')
    while True:
        stu={}
        adno = int(input("Enter adno: "))
        name=input("Enter name: ")
        mark1=int(input("Enter mark1: "))
        mark2=int(input("Enter mark2: "))
        mark3=int(input("Enter mark3: "))
        stu[adno]=[name,mark1,mark2,mark3]
        pickle.dump(stu,f)
        ans = input("Want to continue?")
        if ans in 'Nn':
            break
    f.close()

'''
Enter choice(1-7): 1
Enter adno: 1
Enter name: abc
Enter mark1: 20
Enter mark2: 20
Enter mark3: 30
Want to continue?y
Enter adno: 2
Enter name: dcs
Enter mark1: 99
Enter mark2: 95
Enter mark3: 93
Want to continue?y
Enter adno: 3
Enter name: xyz
Enter mark1: 12
Enter mark2: 56
Enter mark3: 36
Want to continue?n
'''

def display():
    f = open('stu.dat','rb')
    try:
        while True:
            st= pickle.load(f)
            print(st)
    except EOFError:
        f.close()

'''
Enter choice(1-7): 2
{1: ['abc', 20, 20, 30]}
{2: ['dcs', 99, 95, 93]}
{3: ['xyz', 12, 56, 36]}
'''

def search_stu():
    f = open("stu.dat",'rb')
    n = int(input("Enter student admn no to search: "))
    found = False
    try:
        while True:
            stu=pickle.load(f)
            for x in stu:
                if x==n:
                    found=True
                    print ("found",x,stu[x])
    except EOFError:
        f.close()
    if found == False:
        print("Not found")

'''
Enter choice(1-7): 3
Enter student admn no to search: 3
found 3 ['xyz', 12, 56, 36]
'''

def search_marks():
    f = open("stu.dat",'rb')
    found = False
    c = 0
    try:
        while True:
            stu = pickle.load(f)
            for i in stu:
                t=stu[i]
                if t[1]>90 and t[2]>90 and t[3]>90:
                    found = True
                    c+=1
                    print("Found",i,stu[i])
                    print("Total no of students of scoring above 90 in all subjects are",c)
    except EOFError:
        f.close()
    if found == False:
        print("Not found")

'''
Enter choice(1-7): 4
Found 2 ['dcs', 99, 95, 93]
Total no of students of scoring above 90 in all subjects are 1
'''

def  del_marks():
    f = open("stu.dat",'rb')
    l=[]
    try:
        while True:
            stu = pickle.load(f)
            l.append(stu)
    except EOFError:
        f.close()
    for i in l:
        for x in i:
            t=i[x]
            if t[1]<40 and t[2]<40 and t[3]<40:
                l.remove(i) 
    f=open('stu.dat','wb')
    pickle.dump(l,f)
    f.close()
    display()

'''
Enter choice(1-7): 5
[{2: ['dcs', 99, 95, 93]}, {3: ['xyz', 12, 56, 36]}]
'''

def update():
    n=int(input("enter admn no to update: "))
    f = open("stu.dat",'rb')
    st= []
    while True:
        try:
            s=pickle.load(f)
            st.append(s)
        except EOFError:
            f.close()
            break
    for x in st:
        for i in x:
            t=x[i]
            if i==n:
                t[1]+=5
    f = open("stu.dat",'wb')
    pickle.dump(st,f)
    f.close()
    display()

'''
Enter choice(1-7): 6
enter admn no to update: 3
[{2: ['dcs', 99, 95, 93]}, {3: ['xyz', 17, 56, 36]}]
'''


def choices():
    print('Menu')
    print('1. Create')
    print('2. Display')
    print('3. Search for a particular student whose adno is given.')
    print('4. Search,display & count students scoring above 90 in all 3 subjects.')
    print('5. Delete a student whose mark is below 40 in all 3 subjects.')
    print('6. Update a student’s mark1 by adding 5 grace marks.')
    print('7. Exit')

def main():
    while True:
        choices()
        ch = input('Enter choice(1-7): ')
        
        if ch == '1':
            create()
            
        elif ch == '2':
            display()

        elif ch == '3':
            search_stu()
            
        elif ch == '4':
            search_marks()

        elif ch == '5':
            del_marks()

        elif ch == '6':
            update()

        elif ch == '7':
            print("Exit")
            break
        
        else:
            print('Invalid input')
            
main()     


