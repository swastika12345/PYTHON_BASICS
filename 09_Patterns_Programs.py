#Pattern Programs
#Question-1
n=5
for i in range(1,n):
for j in range(1,i+1):
print(j,end=" ")
print()

#Question-2
n=6
for i in range(1,n+1):
for j in range(1,i+1):
print("*",end=" ")
print()

#Question-3
n=5
for i in range(1,n+1):
for j in range(1,i+1):
print(i,end=" ")
print()


#Question-4
n=5
for i in range(n,0,-1):
for j in range(1,i+1):
print(j,end="_ ")
print()


#Question-5
n=3
for i in range(0,n):
for k in range(1,n-i+1):
print(" ",end=" ")
for j in range(1,2*i+1+1):
print("*",end="_ ")
print()


#Question-6
def histogram(item):
  for n in item:
    output=''
    times=n
    while(times>0):
      output+='*'
      times=times-1
    print(output)

histogram([1,2,3,4,5,4,3,2,1 ])
