#File Handling

#Zero Division Error
try:
  x=int(input('Enter 1st no.:'))
  y=int(input('Enter 2nd no.:'))
  div=x/y
  print(div)
except:
  if(y==0):
    print('Zero Division Error')
  else:
    print('Wrong Input')    


#read() function
demofile.txt= ["Do As You Like It"]
f = open("demofile.txt", "r")
print(f.read())
f.seek(0)
print(f.readline())
print(f.readline())
f.seek(0)
print(f.read(5))
f.seek(0)
for x in f:
  print(x)
f.close()

#appending file
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


#read() after append
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())


import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#adding content to the existing file
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
   f.close()


#check new file
file.text:
  Hello How are you
        with open("file.text", "r") as file: 
            data = file.readlines() 
            for line in data: 
                word = line.split() 
                print(word) 
        file.close()

words=0
with open(“words.txt”,’r’) as f:
       for line in f:
          w=line.split()
          words+=len(words)
max_len=len(max(w,key=len))
print(words)

myfile2.txt:
    Hi!!!How are you doing!!!

#Contents of reversed file
f1=open("file2_rev.txt","w")
f2=open("myfile2.txt","r")
r=f2.read()
f1.write(r[::-1])
f1.close()
print("Content of actual file:{0}\n".format(r))
f1=open("file2_rev.txt","r")
print("Content of reversed file:{0}\n".format(f1.read()))
f1.close()


#New File content
f1=open("myfile.txt","a")
f2=open("myfile.txt","r")
f1.write("\nNew File contents:\n")
f1.write(f2.read())
f1.close()
f2.close()
f1=open("myfile.txt","r")
print(f1.read())
f1.close()