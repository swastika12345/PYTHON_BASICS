#Conditional Statement
#Question-1
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if(a==b):
	print("Both the values are equal.")
elif(a>b):
	print("Value of a is greater than b.")
else:
	print("Value of a is less than b.")


#Question-2
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if(a==b):
	print("Both the values are equal.")
elif(a>b):
	print("Value of a is greater than b.")
else:
	print("Value of a is less than b.")


#Question-3
hrs=float(input("Enter hour:"))
r=float(input("Enter rate:"))
if(hrs>40):
	print("Pay computation is Rs", (r*hrs*1.5))
elif (hrs<=46):
	print("Pay computation is Rs",(r*hrs))




#Question-4
score=float(input("Enter score:"))
if(0.0<score and score<=1.00):
	if(score>=.9):
		print ("GRADE A")
	elif(score>=.8 and score<.9):
		print ("GRADE B")
	elif(score>=.7 and score<.8):
		print ("GRADE C")
	elif(score>=.6 and score<.7):
		print ("GRADE D")
	elif(score<.6):
		print ("GRADE F")
	else:
		print("Beyond range")
	else:
		print("Wrong input")


#Question-5
temp=float(input("Enter temperature:"))
ch=input("1.Temperature in Centigrade\n2.Temperature in Fahrenheit\nEnter choice:")
if (ch == '1'):
	print("Temperature:”, (((9/5)*temp)+32) )
else:
	print("Temperature:”, ((5/9)*(temp-32) ))



#Question-6
a=int(input("Enter a number:"))
if(a<0):
	print("Number is negative")
else:
	print("Number is positive")



#Question-7
a=int(input("Enter a number:"))
if (a%2==0):
	print("Given number is even")
else:
	print("Given number is odd")



#Question-8
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if(a>b and a>c):
	print("a is largest")
elif(b>a and b>c):
	print("b is largest")
else:
	print("c is largest")
if(a<b and a<c):
	print("a is smallest")
elif(b<a and b<c):
	print("b is smallest")
else:
	print("c is smallest")


#Question-9
basic=int(input("Enter basic salary:"))
if (basic<=10000) :
	DA=(basic*80) /100
	HRA=(basic*20)/100
elif (basic<=20000) :
	DA=(basic*90)/100
	HRA=(basic*25)/100
else:
	DA=(basic*95)/100
	HRA=(basic*30) /100
gross=basic+DA+HRA
print(gross)


#Question-10
import math
a=float(input("Enter first coefficient :"))
b=float(input("Enter second coefficient :"))
c=float(input("Enter third coefficient :"))
d=((b**2) -(4*a*c))
print("The discriminant value is ",(d))

if(d<0):
	print("Roots are imaginary.")
elif(d>=0):
	print("Roots are real.")
else:
	print("Not apllicable.")
r1=(-b+(d**(1/2))/(2*a))
r2=(-b-(d**(1/2))/(2*a))
print("The roots of the Quadratic equation are", (r1,r2))

#Question-11
p=float(input("Enter 1st side of triangle :"))
q=float(input("Enter 2nd side of triangle :"))
r=float(input("Enter 3rd side of triangle :"))
if((p+q>r) and (q+r>p) and (r+p>q)):
	if(p==q and p==r):
		print("Triangle is Equilateral.")
	elif(p==r or p==q or q==r):
		print("Triangle is Isosceles.")
	elif((p**2+q**2==r**2) or (q**2+r**2==p**2) or (r**2+p**2==q**2)):
		print("Triangle is Right angled triangle.")
	elif(p!=q and q!=r and rl=p):
		print("Triangle is scalene.”)
	else:
		print("Triangle not possible.")

#Question-12
yr=int(input('Enter a year :"))
if (yr%400==0 and yr%4==0):
	print("Leap year")
elif (yr%100==0) :
	print("Not a leap year.")
else:
	print("Not a leap year.")


#Question-13
a=int(input("Enter first number” ))
b=int(input("Enter second number" ))
c=a+b
print("The sum of the two numbers is",c)



#Question-14
c=int(input("Enter cost price :"))
s=int(input("Enter selling price :"))
if(cos):
	print("The loss is ",(c-s))
elif(s>c):
	print("The profit is",(s-c))
else:
	print("No profit and loss.")
