#Functions 

#Question 1
#Factorial number or not
n = int(input("Enter number:"))
def fact(n):
	if(n==1):
		return n
else:
	return n*fact(n-1)
print('The factorial of the number:',n,"is",fact(n))
def rec_fact(n):
	result=1
	if(n==1):
		return n
		result=result*n
	return result
result=r1ec_fact(n)
print(result)


#Question 2
#Root number
x = float(input("Enter a number:"))
def root(x):
	return (x ** 0.5)
print(root(x))



#Question 3
#LCM of two numbers
def find_lcm(x,y):
	if(x>y):
		greater=x
else:
	greater=y
	while(True):
		if((greater % x==0)and(greater % y==0)):
			lcm=greater
			break
			greater+=1
		return lcm
n1=int(input('Enter a number:'))
n2=int(input('Enter another number:'))
print('The LCM of',n1,'and',n2,'is',find_lcm(n1,n2))


#Question 4
#Factors of given number
x = int(input("Enter number:"))
def factors(x):
	for i in range(1, (x//2 + 1)):
		if x%i == 0:
			print(i,end=" ")
	factors(x)


#Question 5
n=int(input('Enter number of terms:'))
def recur_fibo(n):
	if n <= 1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n-2))
nterms=int(input('Enter number of terms:'))
if nterms <= 0:
	print("Plese enter a positive integer")
else:
	print("Fibonacci sequence:")
for i in range(nterms):
	print(recur_fibo(i),end=" ")
def fib(n):
	a=0
	b=1
	for i in range(0,n):
		c=a+b
		a=b
		b=c
	print(a,end=" ")
print('Fibonacci series is :')
fib(n)


#Question 6
n=int(input("Enter number of rows: "))
def pascal(n):
a=[]
for i in range(n):
a.append([])
a[i].append(1)
for j in range(1,i):
a[i].append(a[i-1][j-1]+a[i-1][j])
if(n!=0):
a[i].append(1)
for i in range(n):
print("
"*(n-i),end=" ",sep=" ")
for j in range(0,i+1):
print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
print()
pascal(n)


#Question 7
a=10 #global variable
def func(a):
	a=5 #local variable
	print(a)
	func(a)


#Question 8
#GCD of two numbers
def gcd(n1,n2):
if(n1%n2==0):
return n2
else:
return gcd(n2,n1%n2)
num1=int(input('Enter one number:'))
num2=int(input('Enter another number:'))
print('The GCD of two',num1,'and',num2,'is',gcd(num1,num2))


#Question 9
def add():
	x=int(input())
	y=int(input())
	print(x+y)
def sub():
	x=int(input())
	y=int(input())
	print(x-y)
def mult():
	x=int(input())
	y=int(input())
	print(x*y)
def div():
	x=int(input())
	y=int(input())
	print(x/y)
def exp():
	x=int(input())
	y=int(input())
	print(x**y)
while(1):
	c=int(input('Enter choice:1:add,2:subtract,3:multiply,4:divide,5:Exponent,6:exit :'))
	if(c==1):
		add()
	elif(c==2):
		sub()
	elif(c==3):
		mult()
	elif(c==4):
		div()
	elif(c==5):
		exp()
	elif(c==6):
		break
	else:
		print('Wrong choice.')
		

#Question 10
def box_volume(length=1,width=1,height=1):
	return length*width*height
print('The default box volume is',box_volume())
print("The volume of a box with length 10,")
print("width 1 and height 1 is:", box_volume( 10 ))
print("The volume of a box with length 10,")
print("width 5 and height 1 is:", box_volume( 10, 5 ))
print("The volume of a box with length 10,")
print("width 5 and height 2 is:", box_volume( 10, 5, 2 ))


#Question 11
def func(name, *fav):
	print(name, "likes to read")
	for subject in fav:
		print(subject)
func("Swastika","C Programming")
func("Swastika", "C Programming", "Data Structures", "Maths")
func("Swastika", "C Programming", "Data Structures", "Maths", "Operating Systems", "Networks")



#Question 12
import sys
prog_name=sys.argv[0]
args=sys.argv[1:]
count=len(args)
print(prog_name)
print(count)
for i in args:
	print(i)


#Question 13
def interest(p,y,s):
	if(s=='y'):
		SI=float((p*y*12)/100)
	else:
		SI=float((p*y*10)/100)
return SI
p=float(input('Enter Principle is :'))
y=float(input('Enter number of years:'))
senior=str(input("Is customer senior citizen (y/n):"))
print("Interest :",interest(p,y,senior))


#Question 14
def fact(x):
	pro = 1
	for i in range(1, x+1):
		pro *= i
		return pro
def perm(n, r):
	return (fact(n)/(fact(n - r) * fact(r)))
n = int(input("n = "))
r = int(input("r = "))
print(perm(n, r))


#Question 15
def fact(x):
	pro = 1
	for i in range(1,x+1):
		pro *= i
		return pro
def comb(n, r):
	return (fact(n)/fact(n - r))
n = int(input("n = "))
r = int(input("r = "))
print(comb(n, r))


#Question 17
def leap(y):
	if ((y%400 == 0) or (y%4 == 0) and (y%100 != 0)):
		print("Leap Year")
	else:
		print("Not a Leap Year")
y = int(input("Year:"))
leap(y)


#Question 18
def max(a,b,c):
	if(a>b and a>c):
		print(a)
	elif(b>a and b>c):
		print(b)
	else:
		print(c)
def min(a,b,c):
	if(a<b and a<c):
		print(a)
	elif(b<a and b<c):
		print(b)
	else:
		print(c)
a=int(input('Enter 1st number:'))
b=int(input('Enter 1st number:'))
c=int(input('Enter 1st number:'))
print('The maximum number is:')
max(a,b,c)
print('The minimum number is:')
min(a,b,c)


#Question 19
mult=lambda a,b:(a*b)
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
mult(a,b)


#Question 20
def prime(n):
	s=0
	for i in range(2,n//2+1,2):
		if (n%i==0):
		s+=i
if(s==0):
print('It is a Prime number')
else:
print('Composite number')
n=int(input('Enter number:'))
prime(n)


