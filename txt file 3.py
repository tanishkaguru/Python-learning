
#1. Print lines beginning with ‘I’

def create():
    f=open('abc.txt','w')
    str1=eval(input('enter a list '))
    f.writelines(str1)
    f.close()

def f1():
    f=open('abc.txt')
    l=f.readlines()
    for x in l:
        if x[0] in 'iI':
            print(x)
    f.close()

#create()
#f1()


#2. Print lines beginning with ‘It’ ,ignore the case.

def f2():
    f=open('abc.txt')
    l=f.readlines()
    for x in l:
        if x[0] in 'iI' and x[1] in 'tT':
            print(x)
    f.close()

#create()
#f2()


#3. Print &; Count lines beginning with VOWELS.

def f3():
    f=open('abc.txt')
    l=f.readlines()
    c=0
    for x in l:
        if x[0].lower() in 'aeiou':
            print(x)
            c+=1
    print('count = ',c)
    f.close()

#create()
#f3()


#4. Copy the contents of one file to another.

def display(f):
        x=open(f)
        str1=x.readlines()
        print(str1)
        x.close()
        
def f4():
    f=open('abc.txt')
    l=f.read()
    f2=open('xyz.txt','w')
    f2.write(l)
    f.close()
    f2.close()
    display('xyz.txt')

#create()
#f4()


#5. Delete the 2nd line.

def f5():
    f=open('abc.txt')
    l=f.readlines()
    f.close()
    f=open('abc.txt','w')
    for x in l:
        if x!=l[1]:
            f.write(x)
    f.close()
    display('abc.txt')


#create()
#f5()


#6. Print lines having a given word.

def f6():
    f=open('abc.txt')
    l=f.readlines()
    c=input("enter the word ")
    for x in l:
        if c.lower() in x.lower():
            print(x)
    f.close()

#create()
#f6()

#7. Delete lines having a word(given by user).

def f7():
    f=open('abc.txt')
    w=input("enter the word ")
    l=f.readlines()
    f.close()
    f=open('abc.txt','w')
    for x in l:
        if w.lower() not in x.lower():
            f.write(x)
    f.close()
    display('abc.txt')

#create()
#f7()


#8. Append a line in a text file.

def f8():
    f=open('abc.txt','a+')
    l=f.readlines()
    c=input("enter the line ")
    f.write(c)
    f.close()
    display('abc.txt')

#create()
#f8()


#9. Display longest line from a text file.

def f9():
    f=open('abc.txt')
    l=f.readlines()
    lo=l[0]
    for x in l:
        if len(x)>len(lo):
            lo=x
    print(x)
    f.close()

#create()
#f9()


#10. Append contents of one file to another.Input both file names from user.

def f10():
    a=input('enter file name 1: ')
    b=input('enter file name 2: ')
    f=open(a)
    f2=open(b,'w')
    l=f.readlines()
    f2.writelines(l)
    f.close()
    f2.close()
    display(a)
    display(b)

#create()
#f10()


#11.Print following statistics:- (i) lines in file

def f111():
    f=open('abc.txt')
    l=f.readlines()
    c=0
    for x in l:
        c+=1
    print(c)
    f.close()


#create()
#f111()


#(ii)empty lines

def f112():
    f=open('abc.txt')
    l=f.readlines()
    c=0
    for x in l:
        if x.isspace():
            c+=1
    print(c)
    f.close()


#create()
#f112()


#(iii) avg characters per line

def f113():
    f=open('abc.txt')
    l=f.readlines()
    c=0
    l1=0
    for x in l:
        c+=len(x)
        l1+=1
    avg=c/l1
    print(avg)
    f.close()


#create()
#f113()


#(iv) avg characters per empty lines.

def f114():
    f=open('abc.txt')
    l=f.readlines()
    c=0
    l1=0
    for x in l:
        c+=len(x)-1
        l1+=1
    avg=c/l1
    print(avg)
    f.close()


create()
f114()



