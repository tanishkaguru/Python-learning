#1.Count the word “the”/”The”/”THE” from a given file.
def create():
        f=open('abc.txt','w')
        while True:
                str1=input('enter any string ')
                f.write(str1)
                ch=input('want to repeat? yY/nN ')
                if ch in 'nN':
                        break
        f.close()

def display(f):
        x=open(f)
        str1=x.read()
        print(str1)
        x.close()

def the():
        f=open('abc.txt')
        x=f.read()
        x=x.split()
        c=0
        for a in x:
                if a.lower()=='the':
                        c+=1
        print("count =",c)
        f.close()
#create()
#the()



#2. Count the occurrences of a given word in a text file.
def count():
        f=open('abc.txt')
        x=f.read()
        x=x.split()
        b=input("enter to count:")
        c=0
        for a in x:
                if a==b:
                        c+=1
        print("count =",c)
        f.close()

#create()
#count()




#3. Count number of “to”(both embedded and non-embedded)

def to():
        f=open('abc.txt')
        x=f.read()
        x=x.split()
        c=0
        for a in x:
                b=a.count('to')
                c+=b
        print("count =",c)
        f.close()
#create()
#to()

#4. Count words beginning from “w”.

def w():
        f=open('abc.txt')
        x=f.read()
        x=x.split()
        c=0
        for a in x:
                if a[0] in 'wW':
                        c+=1
        print("count =",c)
        f.close()
#create()
#w()


#5. Copy words beginning from uppercase alphabet to another file.

def up():
        f=open('abc.txt')
        t=open('xyz.txt','w')
        x=f.read()
        x=x.split()
        for a in x:
                if a[0].isupper():
                        t.write(a+" ")
        f.close()
        t.close()
        display('xyz.txt')

#create()
#up()


#6. Count no of words in a file

def words():
        f=open('abc.txt')
        x=f.read()
        x=x.split()
        c=0
        for a in x:
                c+=1
        print("count =",c)
        f.close()

#create()
#words()

#7.Replace all occurrences of “is” by “was”.

def iswas():
        f=open('abc.txt')
        x=f.read()
        x=x.replace(' is ',' was ')
        print(x)       
        f.close()

#create()
#iswas()


#8. Capitalize every word’s first character.

def first():
        f=open('abc.txt')
        l=f.read()
        l=l.title()
        print(l)       
        f.close()

#create()
#first()

#9. Reverse every word in the file.

def rev():
        f=open('abc.txt')
        l=f.read()
        l=l[::-1]
        print(l)        
        f.close()

#create()
#rev()

#10. Find frequency table of each word present in text file.

def table():
        f=open('abc.txt')
        f2=[]
        l=f.read()
        l=l.split()
        for x in l:
                if x not in f2:
                        f2.append(x)
        for x in f2:
                print('count of',x,'=',l.count(x))

#create()
#table()

#11. Print words containing vowels,also copy them in another file.

def vowels():
        f=open('abc.txt')
        f2=open('xyz.txt','w')
        l=f.read()
        l=l.split()
        for x in l:
                for i in x:
                        if i in 'aeiou':
                                print(x)
                                f2.write(x)
                                f2.write(' ')
                                break
        f.close()
        f2.close()
        display("xyz.txt")

#create()
#vowels()


#12. Display words having length specified by user.

def words():
        f=open('abc.txt')
        l=f.read()
        l=l.split()
        w=int(input("enter the length of word to print: "))
        for x in l:
                if len(x)==w:
                        print(x)
        f.close()

#create()
#words()

#13. Find word having maximum length

def maxl():
        f=open('abc.txt')
        l=f.read()
        l=l.split()
        mc=l[0]
        for x in l:
                if len(x)>len(mc):
                        mc=x
        print(x)

#create()
#maxl()


#14. Replace multiple spaces by single space and copy in new file.

def spaces():
        f=open('abc.txt')
        f1=open('xyz.txt','w')
        l=f.read()
        l=l.split()
        f1.write(' '.join(l))
        f1.close()
        display('xyz.txt')
        f.close()
        

#create()
#spaces()


#15. Append contents of one file to another .Input file names from user.

def create(a):
        f=open(a,'w')
        while True:
                str1=input('enter any string ')
                f.write(str1)
                ch=input('want to repeat? yY/nN ')
                if ch in 'nN':
                        break
        f.close()
def f15():
        b=input("enter name for the 2nd file: ")
        f=open(a)
        f2=open(b,'w')
        l=f.read()
        f2.write(l)
        f.close()
        f2.close()
        display(a)
        display(b)

a=input("enter name of first file: ")
create(a)
f15()









        

