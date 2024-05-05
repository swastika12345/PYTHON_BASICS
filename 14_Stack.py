#Stack
#IsEmpty() operation
def isEmpty(S):
if len(S)==0:
return True
else:
return False

#push() operation
def push(S,item):
S.append(item)
top=len(S)-1

#pop() operation
def pop(S):
if isEmpty(S):
return "“UNDERFLOW"
else:
val=S.pop()
if(len(S)==0):
top=None
else:
top=len(S)-1
return val

#peek() funtion
def peek(S):
if isEmpty(s):
return "UNDERFLOW"
else:
top=len(S)-1
return S[top]

#display() operation
def display(S):
if isEmpty(s):
print('Stack is empty‘)
else:
top=len(S)-1
print("(top)",end="_")
while(top>=0):
print(S[top],end="_")
top=top-1
print()


#main starts
S=[]#stack
top=None
while True:
print("****Stack Demonstration****")
print("1.PUSH")
print("2.POP")
print("3.PEEK")
print("4.DISPLAY")
print("@.EXIT")
ch=int(input(‘Enter your choice:'))
if ch==1:
val=int(input('Enter item to be pushed:'))
push(S, val)
elif ch==2:
val=pop(S)
if (val=="UNDERFLOW"):
print('Stack is empty.')
else:
print('\nPopped item is',val)
elif ch==3:
val=peek(S)
if (val=="UNDERFLOW"):
print('Stack is empty.')
else:
print('Top item value is',val)
elif ch==4:
display(S)
elif ch==0:
print("exit")
break



