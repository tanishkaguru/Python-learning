import csv
'''Q2. A csv file is supposed to contain the following data (data only, no headings):
RNo –integer
Name – string
Theory Marks – float
Practical marks – float
Write a menu driven program to perform the following operations on the file:
(i) Create the file if it does not already exist
(ii) Append record(s) to the file
(iii) Display all the data from the file along with Total and Result of each student.
Total is to be calculated as Theo+Prac, Result is “PASS” if Total is above 40,
otherwise the Result is “FAIL”.
(iv) Increase the theory marks by 5 for all those students whose theory marks are
between 35 and 41 (Excluding both).
(v) Display the result summary in the following format:
 Students appeared: Total number of records in the file
 Max Total: Highest of total marks
 Min Total: Lowest of total marks
 Average Total: Average of total marks
 PASS: Total number of passing students
 FAIL: Total number of failed students
 PASS%: (PASS/Students appeared)*100
'''



def create():
    f = open('e2.csv','w',newline='')
    csvwriter = csv.writer(f)
    while True:
        r = int(input("Enter roll no: "))
        t = float(input("Enter theory marks: "))
        p = float(input("Enter practical marks: "))
        csvwriter.writerow([r,t,p])
        ans = input("Want to continue? ")
        if ans in 'Nn':
            break
    f.close()
'''
Enter choice(1-6): 1
Enter roll no: 1
Enter theory marks: 56
Enter practical marks: 12
Want to continue? Y
Enter roll no: 2
Enter theory marks: 33
Enter practical marks: 3
Want to continue? y
Enter roll no: 3
Enter theory marks: 20
Enter practical marks: 5
Want to continue? y
Enter roll no: 4
Enter theory marks: 25
Enter practical marks: 10
Want to continue? y
Enter roll no: 5
Enter theory marks: 45
Enter practical marks: 18
Want to continue? n
'''

def append():
    f=open('e2.csv','a',newline='')
    csvwriter = csv.writer(f)
    ans='y'
    while ans.lower()=='y':
        r = int(input("Enter roll no: "))
        t = float(input("Enter theory marks: "))
        p = float(input("Enter practical marks: "))
        csvwriter.writerow([r,t,p])
        ans = input("Want to continue? ")
    f.close()
'''
Enter choice(1-6): 2
Enter roll no: 6
Enter theory marks: 59
Enter practical marks: 25
Want to continue? n
'''

def display():
    f=open('e2.csv','r')
    a= csv.reader(f)
    for x in a:
        print(x)
        t=float(x[1])+ float(x[2])
        print("Total marks= ",t)
        if t>=40:
            print("Result=PASS ")
        else:
            print("Result=FAIL ")
    f.close()
'''
Enter choice(1-6): 3
['1', '56.0', '12.0']
Total marks=  68.0
Result=PASS
['2', '33.0', '3.0']
Total marks=  36.0
Result=FAIL
['3', '20.0', '5.0']
Total marks=  25.0
Result=FAIL
['4', '25.0', '10.0']
Total marks=  35.0
Result=FAIL
['5', '45.0', '18.0']
Total marks=  63.0
Result=PASS
['6', '59.0', '25.0']
Total marks=  84.0
Result=PASS
'''

def incr():
    f = open('e2.csv','r',newline='')
    a=csv.reader(f)
    l=[]
    for i in a:
        l.append(i)
    for x in l:
        if float(x[1])>35.0 and float(x[1])<41.0:
            x[1]= float(i[1]) + 5.0
    f.close()
    f = open('e2.csv','w',newline='')
    csvwr=csv.writer(f)
    csvwr.writerows(l)
    f.close()
    display()
'''
Enter choice(1-6): 2
Enter roll no: 7
Enter theory marks: 36
Enter practical marks: 8
Want to continue? n
Enter choice(1-6): 4
['1', '56.0', '12.0']
Total marks=  68.0
Result=PASS
['2', '33.0', '3.0']
Total marks=  36.0
Result=FAIL
['3', '20.0', '5.0']
Total marks=  25.0
Result=FAIL
['4', '25.0', '10.0']
Total marks=  35.0
Result=FAIL
['5', '45.0', '18.0']
Total marks=  63.0
Result=PASS
['6', '59.0', '25.0']
Total marks=  84.0
Result=PASS
['7', '41.0', '8.0']
Total marks=  49.0
Result=PASS
'''

def rec():
    f = open('e2.csv','r',newline='')
    a = csv.reader(f)
    c = 0
    for i in a:
        c+=1
    return c
    f.close()

def max():
    f=open('e2.csv','r',newline='')
    a=csv.reader(f)
    m=0
    for x in a:
        t = float(x[1])+ float(x[2])
        if t>m:
            m=t
    print (m)
    f.close()
    
def min():
    f=open('e2.csv','r',newline='')
    a=csv.reader(f)
    m=0
    for x in a:
        t = float(x[1])+ float(x[2])
        if t<m:
            m=t
    print (m)
    f.close()

def avg():
    f=open('e2.csv','r',newline='')
    a=csv.reader(f)
    l=0
    for x in a:
        t = (float(x[1])+ float(x[2]))//rec()
        if t>l:
            l = t
    return l
    f.close()

def tpass():
    f = open('e2.csv','r')
    a = csv.reader(f)
    c = 0
    for x in a :
        t = float(x[1])+ float(x[2])
        if t>=40:
            c+=1
    return c
    f.close()
    
def failed():
    f = open('e2.csv','r')
    a = csv.reader(f)
    c = 0
    for x in a :
        t = float(x[1])+ float(x[2])
        if t<=40:
            c+=1
    return c
    f.close()

def ppercent():
    a = tpass()
    b = rec()
    c = (a/b)*100
    print ('pass% = ',c)

def display_2():
    print("The result summary is:- ")
    print("Students appeared: ",rec())
    print("Max Total: ",max())
    print("Min Total: ",min())
    print("Average Total: ",avg())
    print("PASS: ",tpass())
    print("FAIL: ",failed())
    ppercent()
'''
Enter choice(1-6): 5
The result summary is:- 
Students appeared:  7
84.0
Max Total:  None
0
Min Total:  None
Average Total:  12.0
PASS:  4
FAIL:  3
pass% =  57.14285714285714
'''

def choices():
    print('Menu')
    print('1. Create the file if it does not already exist')
    print('2. Append record(s) to the file')
    print('3. Display all the data from the file along with Total and Result of each student.')
    print('4. Increase the theory marks by 5 for all those students whose theory marks are between 35 and 41 (Excluding both)')
    print('5. Display the result summary')
    print('6. Exit')

def main():
    while True:
        choices()
        ch = input('Enter choice(1-6): ')
        
        if ch == '1':
            create()
            
        elif ch == '2':
            append()

        elif ch == '3':
            display()
            
        elif ch == '4':
            incr()

        elif ch == '5':
            display_2()

        elif ch == '6':
            print("Exit")
            break
        
        else:
            print('Invalid input')
            
main()    
