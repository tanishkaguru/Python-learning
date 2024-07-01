
def create():
        f=open('abc.txt','w')
        while True:
                str1=input('enter any string')
                f.write(str1)
                ch=input('want to repeat? yY/nN ')
                if ch in 'nN':
                        break
        f.close()


def display(f):
        f=open('abc.txt')
        str1=f.read()
        print(str1)
        f.close()



#1 count uppercase characters
def upper():
        t=open('abc.txt')
        f=t.read()
        c=0
        for ch in f:
                if ch.isupper():
                        c+=1
        return c
#create()
#print(upper())

#2 count occurences of a given character
def occur():
        t=open('abc.txt')
        f=t.read()
        a=input("enter to count occurence:")
        c=0
        for ch in f:
                if ch.lower()==a.lower():
                        c+=1
        return c
#create()
#print(occur())                


#3 Copy one file to another,input file names from user
def copy():
        a=input("enter file name to copy")
        b=input("enter file name to copy to")
        f=open(a)
        str1=f.read()
        f.close()
        f=open(b,'w')
        f.write(str1)
        f.close()
        display(a)
        display(b)
#copy()        


#4 Read characters from keyboard one by one.All lowercase characters to be copied into file Lower,all uppercase characters copied
#  into Upper and all other characters get stored in Others.
def display(x):
        f=open(x)
        str1=f.read()
        print(str1)
        f.close()
def cha():
        l=open("lower.txt",'w')
        u=open("upper.txt",'w')
        o=open("other.txt",'w')
        while True:
                f=input("enter character to sort into upper, lower and others(enter # to terminate): ")
                if f.islower():
                        l.write(f)
                elif f.isupper():
                        u.write(f)
                else:
                        o.write(f)
                if f=='#':
                        break
        l.close()
        u.close()
        o.close()
        display('lower.txt')
        display('upper.txt')
        display('other.txt')
        
#cha()
   


#5 Count only digits.
def dig():
        t=open('abc.txt')
        f=t.read()
        c=0
        for ch in f:
                if ch.isdigit():
                        c+=1
        return c
#create()
#print(dig())  


#6. Count spaces-(i) only blanks
def f61():
        t=open('abc.txt')
        f=t.read()
        c=0
        for char in f:
                if char==" ":
                        c+=1
        return c
#create()
#print(f61())


# (ii)spaces and blanks
def create():
        f=open('abc.txt','w')
        str1=input("enter any string ")
        f.write(str1+"\n"+"\t")
        f.close()
def f62():
        f=open('abc.txt')
        t=f.read()
        c=0
        for x in t:
                if x.isspace():
                        c+=1
        f.close()                
        return c
#create()        
#print(f62())


#7 Find size of file in bytes.
def create():
        f=open('abc.txt','w')
        str1=input("enter any string ")
        f.write(str1)
        f.close()
def f7():
        t=open('abc.txt')
        f=t.read()
        c=len(f)
        print("size of file in bytes is",c)
        return c
#create()        
#f7() 

#8 Find size of file in bytes without spaces.
def create():
        f=open('abc.txt','w')
        str1=input("enter any string ")
        f.write(str1)
        f.close()
def f8():
        t=open('abc.txt')
        f=t.read()
        c=len(f)
        for x in f:
                if x==' ':
                        c=c-1
        print("size of file in bytes is",c)
#create()        
#f8() 


#9. Using loop_over method, display contents.
def create():
        f=open('abc.txt','w')
        while True:
                str1=input('enter any string')
                f.write(str1)
                ch=input('want to repeat? yY/nN ')
                if ch in 'nN':
                        break
        f.close()
def f9():
        f=open('abc.txt')
        l=f.read()
        for x in l:
                print (x)
#create()        
#f9() 


#10. Using utf feature input wishes in various languages to create a text file,display the contents.

def save():
        f=open('wishes.txt','w', encoding='utf-16')
        while True:
                str1=input("enter line ")
                f.write(str1+'\n')
                f.flush()
                ans=input("want to continue?yY/nN ")
                if ans in 'Nn':
                        break
def f9():
        f=open('wishes.txt',encoding='utf-16')
        L=f.read()
        for x in L:
                print (x,end='')
#save()        
#f9() 


#11. Count words.

def create():
        f=open('abc.txt','w')
        str1=input("enter any string ")
        f.write(str1)
        f.close()
def f10():
        c=0
        t=open('abc.txt')
        f=t.read()
        f=(f.lstrip()+' ')
        for x in f:
                if x==' ':
                        c+=1 
        print (c)                
create()        
f10() 