#Loops & Iteration

#SUM
n=int(input('Enter number of terms: '))
x=float(input('Enter the number: '))
sum=8
for i in range(0,n+1):
	sum+=x**i
print (sum)

#Digit extraction
n=int(input('Enter number of terms:'))
x=int(input('Enter the number:"))
sum=0
for i in range(1,n+1):
	sum=sum+(+1)**i*((x**i)/i)
print (sum)


#Check Prime Numbers or not
num=int(input("Enter a number :"))
flag=0
for i in range(2,num):
	if(num % i == 6):
		flag=1
		break
if (flag==1):
	print("Is not a prime number”)
else:
	print("Is a prime number")


#Find sum of all odd numbers and even nos. in a range
sum_odd=0
sum_even=0
low=int(input("Enter low range :"))
high=int(input("Enter high range :"))
for i in range(low,high+1):
	if (i%2==0):
		sum_even=sum_even+i
	else:
		sum_odd=sum_odd+i
print("The sum of all even numbers is", (sum_even))
print("The sum of all odd numbers is", (sum_odd))


#Program o sum upto n numbers
sum=98
n=int(input("Enter number upto which sum is done:"))
for i in range(1,n+1):
	sum+=i
print("Sum=", sum)


#Whether the number is Prime or not
counter=0
n=int(input("Enter a number:"))
for i in range(2,(n//2)+1):
	if (n%i==0):
		counter+=1
if (counter==0):
	print(n,"is a prime number")
else:
	print(n,"is not a prime number")



#Print all prime numbers from 1 to 100
lower_value=int(input("Enter lower level:"))
upper_value=int(input("Enter upper level:"))
print("Prime numbers between are:")
for num in range(lower_value, upper_value+1) :
	if(num>1):
	for i in range(2,num):
		if (num%i==0) :
			break
		else:
			print(num)

#Check whether a number is armstrong or not
num=int(input("Enter a number:"))
sum=0
temp=num
while(num>0):
	digit=num%1e
	sum+=digit*digit*digit
	num//=1
if (temp==sum) :
	print(temp,"is an Armstrong number”)
else:
	print(temp,"is not an Armstrong number” )



#Print all armstrong numbers between given range
lower=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
print("Armstrong numbers between 1 to 100 are:")
for num in range(lower,upper+1):
sum=0
temp=num
while(num>0):
	digit=num%10
	sum+=digit*digit*digit
	num//=10
if (temp==sum) :
	print (temp)



#Print all fibonnaci numbers upto n terms
#Question 6:Dislay terms in Fibonacci series
n = int(input (‘Enter number of terms:'))
n1 = 0
n2=1
count = 0
if (n <= 0):
	print ("Please enter a positive integer, the given number is not valid")
elif (n == 1):
	print ("The Fibonacci sequence of the numbers up to", n, ": ")
	print(n1)
else:
	print ("The fibonacci sequence of the numbers is:")
	while (count < n):
	 	print(n1)
		n3 = nl + n2	
		n1 = n2
		n2 = n3

count += 1


#print all natural nos. between range
low=int(input("Enter low range :"))
high=int(input("Enter high range :"))
for i in range(low,high+1):
	print(i,end="_: ")
	
#Check whether the number is pallindrome or not
num=int(input("Enter number:"))
sum=0
temp=num
while(num>0):
	digit=num%10
	sum=(sum*10)+digit
	num//=1
if (temp==sum):
	print(temp,"is a pallindrome number")
else:
	print(temp,"is not a pallindrome number”)


#Check whether the number is Armstrong or not
num=int(input("Enter number:"))
sum=0
temp=num
while(temp>0):
	digit=temp%10
	sum+=digit**3
	temp//=10
if (num==sum) :
	print("Given number is Armstrong number”)
else:
	print("Given number is not Armstrong number”)

