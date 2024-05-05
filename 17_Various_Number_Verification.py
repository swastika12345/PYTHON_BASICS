#Various_Number_Verification_Code

#Check whether the no. is Automorphic or not
num = int(input("Enter a number: \n"))
n = len(str(num))
sqr = num**2
last = sqr%pow(10,n)
if(last == num):
  print("Automorphic Number")
else:
  print("Not an Automorphic Number")


#Check whether the no. is Automorphic or not
num = int(input("Enter a number: \n"))
n = len(str(num))
sqr = num**2
last = sqr%pow(10,n)
if(last == num):
  print("Automorphic Number")
else:
  print("Not an Automorphic Number")


#Check whether the no. is Pronic or not
num = int(input("Enter a number:"))
flag=0
for i in range(1,num):
  if(i*(i+1)==num):
    flag=1
    break
if(flag==0):
  print("Not a Pronic number") 
else:
  print(" Pronic number")     


#Check whether the no. is Pronic or not
num = int(input("Enter a number:"))
flag=0
for i in range(1,num):
  if(i*(i+1)==num):
    flag=1
    break
if(flag==0):
  print("Not a Pronic number") 
else:
  print("Pronic number") 


#Check whether the no. is Duck or not
def ducknumber(num):
    while num>0:
        d=num%10
        if d==0:
            return 1
        num=num//10
    return 0
n=int(input('Enter a number '))
if ducknumber(n)==1:
    print('Duck Number')
else:
    print('Not Duck Number')


#Check whether the no. is Abundant or not
num = int(input("Enter a number:"))
sum=0
for i in range(1,num):
  if(num%i==0):
    sum+=i
if(sum>num):
  print("Abundant number")
else:
  print("Not an Abundant number") 


#Check whether the no. is Spy number or not
def Isspy(num):
  n=len(str(num))
  temp=num
  sum=0
  product=1
  while(temp>0):
    digit=temp%10
    sum+=digit
    product*=digit
    temp//=10
  if(sum==product):
    return True
  else:
    return False    
num=int(input("Enter number:"))
if(Isspy(num)==1):
  print("Spy Number")
else:
  print("Not Spy number")        


#Check whether the no. is Harshad number or not
def harshad(num):
  temp=num
  sum=0
  while(temp>0):
    digit=temp%10
    sum+=digit
    temp//=10
  if(num%sum==0):
    return True
  else:
    return False
num=int(input("Enter number:"))
if(harshad(num)==1):
    print("Harshad Number")
else:
    print("Not a Harshad Number")


#Check whether the no. is Krishnamurthy number or not
n=int(input("Enter a number"))
sum=0
fact=1
temp=n
while(n>0):
    r=n%10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact 
    n=n//10
if(sum==temp):
    print("The number is Krishnamurthy number")
else:
    print("The number is not a krishnamurthy number")

#Chech Armstrong number or not
sum=0
count=0
order=num
while(order>0):
	count=count+1
	order=order//10
	temp=num
while(temp>0):
	digit=temp % 10
	sum+=digit**count
	temp=temp//10
num=int(input("Enter a number”))
if(num == sum):
	print("Is a armstrong number”)
else:
	print("Is not an armstrong number")

