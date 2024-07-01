#1. Write a function in Python to swap the values of two variables
#(i)without using any third variable
def swapval(a,b):
    a,b=b,a
    print(a,b)
  

#(ii) using a third variable.
def swapvar(a,b):
    temp=a
    a=b
    b=temp
    print(a,b)



#2. Write a program in Python to calculate the area of a circle using function.
def cir_area(r):
    area=3.14*(r)**2
    return area



#3. Write a program in Python to check whether a given number is prime or not using function.
def primeno(n):
    x=0
    if n>1:
        for i in range(2,n):
            if n%i==0:
                x+=1
        if x==0:
            print ("prime")
        else:
            print("not prime")
           



#4. Write a FUNCTION in Python to calculate &amp; return the sum of the following series using function:-

#(i) 1-2+3-4+5… n terms
def s1(n):
    s=0
    for i in range(1,n+1):
        s+= ((-1)**(i+1))*i 
    return (s) 



#(ii) 1 + 1/2 + 1/3 + 1/4+…n terms

def s2(n):
    s=0
    for i in range(1,n+1):
        s+=( 1/(i) )
    return (s) 


 

#(iii) x/1! + x 3 /3! + x 5 /5! + x 7 /7! + …n terms

def fact(a):
    f=1
    for i in range(1,a+1):
        f*=i
    return f

def s3(n,x):
    s=0
    for i in range(1,n+1):
        s+=( x/(fact(i)) )
    return (s) 



#9. Make the program to count the no. of students who passed the exam using function.

def passexam(n):
    p=0
    for i in range(1,n+1):
        m=int(input("enter the marks of student out of 100"))
        if m>=50:
            p+=1
    print("no of passing students: ", p)




#11 .Write a function to return the reverse the digits of a number.

def revdig(n):
    rev=0
    while True:
        d=n%10
        rev=rev*10+d
        n=n//10
        if n==0:
            break
    return (rev)



#12 Write a program in Python to find the greatest common divisor of two numbers using function.

def gcd(a,b):
    i=1
    while True:
        if a%i==0 and b%i==0:
            gcd=i
        i+=1
        if i>a or i>b:
            break
    return (gcd)



#13. Write a program to compute the sum of exponential series using function.
#e^x=1+x/1+x^2/2!+x^3/3!+...
def fact(a):
    f=1
    for i in range(1,a+1):
        f*=i
    return f

def series(n,x):
    s=1
    for i in range(1,n):
        s+=( (x**i)/(fact(i)) )
    print("sum = ",s) 



#14 .Write a program to check out whether a given number is an Armstrong number or not using function.

def armstrongno(n):
    s=0
    temp=n
    while True:
        d=n%10
        s+= (d)**3
        n=n//10
        if n==0:
            break
    if s==temp:
        print("armstrong")
    else:
        print("not armstrong")
       


#15. Write a program to find out whether a given number is palindrome or not using function.

def palindromeno(n):
    rev=0
    temp=n
    while True:
        d=n%10
        rev=rev*10+d
        n=n//10
        if n==0:
            break
    if rev==temp:
        print ("palindrome")
    else:
        print("not palindrome")




#16.Write a program to convert binary numbers to decimal numbers using function.

def bin_dec(n):
    temp=n
    dec=0
    i=0
    while (n!=0):
        d=n%10
        dec=dec+d*(2**i)
        n=n//10
        i+=1
    return dec




#17.Write a program to print all prime numbers between 25 to 50 using function.
    
def prime25to50():
    for i in range(25,51):
        p=0
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print (i)
                
#Define a function which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 1000 and 3000 (both included)
def mult():
    for i in range(1000,3001):
        if i%7==0 and i%5!=0:
            print(i,",",end ='')
        else:
            pass     



# Define the same function of prev question where starting and ending number is passed as argument.
def mult(x,y):
    for i in range(x,y+1):
        if i%7==0 and i%5!=0:
            print(i,",",end ='')
        else:
            pass



 # Define a function that accepts a sentence and calculate the number of uppercase letters and lowercase letters.
def up_low(s):
    u = 0
    l = 0
    for i in s:
        if i.isupper()== True:
            u+=1
        else:
            l+=1
    print("No of uppercase characters= ",u)
    print("No of lowercase characters= ",l)
    



# Define a function that can accept two strings as input and concatenate and prints it.
def str(str1,str2):
    x = str1 + str2
    print(x)



# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
def sqno():
    for i in range(1,21):
        i = i*i
        print(i)


#With a given tuple (1,2,3,4,5,6,7,8,9,10)define a function to print the first half values in one line and the last half values in one line.
def tup(t):
    t1 = t[:5]
    t2 = t[5:]
    print(t1)
    print(t2)
    
t = (1,2,3,4,5,6,7,8,9,10)



#Write a function called my_buzz that takes a number. If the number is divisible by 3, it should return “Fizz”. If it is divisible by 5, it should return“Buzz”.
#If it is divisible by both 3 and 5, it should return “FizzBuzz”.Otherwise, same no.
def my_buzz(a):
    if a%3==0 and a%5==0:
        print("FizzBuzz")
    elif a%3 == 0:
        print("Fizz")
    elif a%5 == 0:
        print("Buzz")
    else:
        print (a)
        


#Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter)

def sum(n):
    s = 0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            s+=i
    print("sum: ",s)
    


#Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

def primenos(n):
   primeno=[] 
   for i in range (2, n+1):
       for j in range(2, i):
           if i%j == 0:
               break
       else:
           primeno.append(i)
   print(primeno)
   


# WAP in python to delete all duplicate elements in a list.
def dele(l):
    finlist = []
    for i in l:
        if i not in finlist:
            finlist.append(i)
    return finlist
     
l = [2,3,4,5,5,4,8,9,2]
print(dele(l))




