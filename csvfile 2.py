import csv

def create():
    f=open('e1.csv','w',newline='')
    ewriter=csv.writer(f)
    ewriter.writerow(['Name','Age','Qualification','Experience'])
    ewriter.writerow(['Ananya',32,'PG',8])
    f.close()

def append():
    f = open('e1.csv','a',newline ='')
    csvwr = csv.writer(f)
    ans = 'y'
    while ans.lower()=='y':
        n = input("Enter name: ")
        a = int(input("Enter age: "))
        q = input("Enter qualification: ")
        e = int(input("Enter experience: "))
        csvwr.writerow([n,a,q,e])
        ans = input("Want to continue? ")
    f.close()

'''
Enter choice(1-6): 1
Enter name: HARRY
Enter age: 32
Enter qualification: PG
Enter experience: 5
Want to continue? Y
Enter name: HARI
Enter age: 23
Enter qualification: BTECH
Enter experience: 4
Want to continue? Y
Enter name: PRIYA
Enter age: 26
Enter qualification: PG
Enter experience: 3
Want to continue? Y
Enter name: JIN  
Enter age: 29
Enter qualification: BTECH
Enter experience: 3
Want to continue? Y
Enter name: HOSEOK
Enter age: 35
Enter qualification: PG
Enter experience: 5
Want to continue? N'''

def display():
    f=open('e1.csv','r',newline='')
    a=csv.reader(f)
    for x in a:
        print(x)
    f.close()

'''
Enter choice(1-6): 2
['Name', 'Age', 'Qualification', 'Experience']
['Ananya', '32', 'PG', '8']
['HARRY', '32', 'PG', '5']
['HARI', '23', 'BTECH', '4']
['PRIYA', '26', 'PG', '3']
['JIN', '29', 'BTECH', '3']
['HOSEOK', '35', 'PG', '5']
'''

def display_2():
    f=open('e1.csv','r')
    a=csv.reader(f)
    l=[]
    for x in a:
        if x[1]<str(30):
            print (x)
    f.close()

'''
Enter choice(1-6): 3
['HARI', '23', 'BTECH', '4']
['PRIYA', '26', 'PG', '3']
['JIN', '29', 'BTECH', '3']
'''

def exp():
    f=open('e1.csv','r',newline='')
    a=csv.reader(f)
    c = 0
    l = []
    for x in a:
        if c == 0:
            c+=1
            l.append(x)
        else:
            x[3]=int(x[3])+1
            l.append(x)
    f.close()
    f=open('e1.csv','w',newline='')
    f.write(str(l))
    f.close()
    display()

'''Enter choice(1-6): 4
["[['Name'", " 'Age'", " 'Qualification'", " 'Experience']", " ['Ananya'", " '32'", " 'PG'", ' 9]', " ['HARRY'", " '32'", " 'PG'", ' 9]',
 " ['HARI'", " '23'", " 'BTECH'", ' 5]', " ['PRIYA'", " '26'", " 'PG'", ' 4]', " ['JIN'", " '29'", " 'BTECH'", ' 4]',
  " ['HOSEOK'", " '35'", " 'PG'", ' 6]]']
  '''

def delete():
    l=[]
    f=open('e1.csv','r',newline='')
    n=input("Enter name: ")
    a=int(input("Enter age: "))
    for i in csv.reader(f):
        l.append(i)
    f.close()
    for x in l:
        if x[0]==n and x[1]==a:
            l.remove(x)
    f=open('e1.csv','w',newline='')
    b=csv.writer(f)
    b.writerows(l)
    f.close()
    display()

def choices():
    print('Menu')
    print('1. Append record(s) to the file')
    print('2. Display all the data from the file')
    print('3. Display all the records with Age<30')
    print('4. Increase the Experience of all the records by 1')
    print('5. Delete a record with given name and age (to be input from the user)')
    print('6. Exit')

def main():
    create()
    while True:
        choices()
        
        ch=input('Enter choice(1-6): ')
        
        if ch=='1':
            append()
            
        elif ch=='2':
            display()

        elif ch=='3':
            display_2()
            
        elif ch=='4':
            exp()

        elif ch=='5':
            delete()

        elif ch=='6':
            print("Exit")
            break
        
        else:
            print('Invalid input')
            
main() 


