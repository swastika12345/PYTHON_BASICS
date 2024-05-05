#Dictionary

#Queston 1
dict={'1':'tom','2':'jerry','3':'cat','4':'dog','5':'bat'}
print(dict.values())                                                                                        
dict['1']='jack'
print("The updated dictionary is :")
print(dict.values())
dict['6']='rose'
print(dict.values())
del dict['3']
print(dict.values())
dict.pop(list(dict.keys())[0])
print(dict)
dict.clear()
print(dict)
del (dict)
print(dict)
number = int(input("Please enter the Maximum Number : "))
myDict = {x:x ** 2 for x in range(1, number + 1)}
print( myDict)
dict1={1,2,3,4,5,6,7,8,9}
myDict = {x:x ** 2 for x in dict1 if x%2!=0}
print( myDict)
dict2={'1':'tom','2':'jerry','3':'cat','4':'dog','5':'bat'}
print(dict2)
l=len(dict1)
print('The length of the dictionary is',l)
dict3={33,45,67,89,90,105}
from collections import OrderedDict
dict4= {'ravi': '10', 'rajnish': '9','sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict5= OrderedDict(sorted(dict4.items()))
print(dict5)
dict6=(dict1 | dict3)
print(dict6)
dict={'1':'ram','2':'shyam','3':'jadu','4':'madhu','5':'joy'}
dict.pop('6',None)
print(dict)
print('The sorted dictionary in frozen set is ',sorted(frozenset(list(dict2.values()))))


#Question 2
dict1={'value1':3,'value2':4,'value3':2,'value4':1}
print(dict1)
a=int(input('Enter a value:'))
print(a in dict1.values())

#Question 3
dict1={'value1':3,'value2':4,'value3':2,'value4':1}
for k in dict1.keys():
  print(k,':',dict1[k])


#Question 4
colours=['Violet','Indigo','Blue','Green','Yellow','Orange','Red']
codes=['R7','R6','R5','R4','R3','R2','R1']
comb={colours[i]:codes[i] for i in range(len(colours))}
print(comb)

#Question 5
dict1={'value1':3,'value2':4,'value3':-13,'value4':1}
print('Maximum value is :',max(dict1.values()))
print('Minimum value is :',min(dict1.values()))

#Question 6
student_data = {
'id1':{'name': ['Sara'],'class': ['V'],'subject_integration':['english, math, science']},
'id2':{'name': ['David'],'class': ['V'],'subject_integration':['english, math, science']},
'id3':{'name': ['Sara'],'class': ['V'],'subject_integration':['english, math, science']},
'id4':{'name':['Surya'],'class':['V'],'subject_integration':['english, math, science']},
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)

#Question 7
d1={'A':1,'B':2}
d2={'C':3,'D':13}
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)


#Question 7(i)
d1={'1':'tom','2':'jerry','3':'cat','4':'dog','5':'bat'}
d2={'6':'ram','7':'shyam'}
d3=d1
for k,v in d2.items():
  if k in d3:
    if type(d3[k]) is list:
      d3[k].append(v)
    else:
      d3[k]=[d3[k]]=[v]
  else:
    d3[k]=v
print(d3)        

#Question 8
dict1={'value1':3,'value2':4,'value3':2,'value4':1}
answer=1
val=list(dict1.values())
for i in val:
  answer=answer*i
print(answer)  

#Question 9
d =  {'value1': 5,'value2': 4,'value3': 3,'value4': 2,'value5': 1,}
answer = 0
val=list(d.values())
for i in val:
    answer = answer+i
print(answer)


#Question 10
from collections import OrderedDict
dict4= {'Ravi': '10', 'Rajnish': '9','Sanjeev': '15', 'Yash': '13', 'Suraj': '32'}
dict5= OrderedDict(sorted(dict4.items()))
print(dict5)


#Question11
d =  {'value1': 5,'value2': 4,'value3': 3,'value4': 2,'value5': 1,}
if (len(d)==0):
  print('Dictionary is empty ')
else:
  print('Dictionary is not empty')  


#Question12
odd=set([x*2+1 for x in range(0,5)])
primes=set()
for i in range(2,10):
  j=2
  f=0
  while (j<=(i/2)):
    if (i%j==0):
      f=1
    j=j+1
  if(f==0):
    primes.add(i)
print('odd set is',odd)
print('prime set is',primes)
print("Union value is",odd.union(primes))
print('Intersection value is',odd.intersection(primes))
print('Difference is',odd.difference(primes))
print('Symmetric difference is',odd.symmetric_difference(primes))

#Question13
mt={2,4,6,8,5}
m2cm={k*100 :k for k in mt}
cm1={100,200,300,400,500}
cm2m={k/100 :k for k in cm1}
print('Conversion from meter to centimeter is',m2cm)
print('Conversion from centimeter to meter is',cm2m)

#Question14
ar=([0,0,2,3],[3,0,0,1],[1,0,2,0],[1,0,2,2])
dic={}
for i in range(len(ar)):
  for j in range(len(ar[i])):
    dic[i,j]=ar[i][j]
print('Sparse matrix is')
print(dic)

#Question 15
dic={i:i**3 for i in range(1,10,2)}
print(dic)

#Queston 16
d={'value1':5,'value2': 4,'value3': 3,'value4': 2,'value5': 1,}
d1={v:k for k,v in d.items()}
print(d1)

#Question 17
student={}
for i in range(3):
    bprint={'name':0,'marks':0}
    bprint['name']=input("Enter name of student {0}:".format(i+1))
    print("enter marks")
    l=list(map(float,input().split()))
    bprint['marks']=l
    total=sum(l)
    student[bprint['name']]=total
    
print(student)
stack=max(zip(student.values(),student.keys()))
print(stack)


#Question 18
d = {}
d2 = {}
for i in range(3):
    x = input('Enter name:')
    y = input('Enter ID:')
    z = list(map(str,input('Enter products sold:').split()))
    d['name'] = x
    d['ID'] = y
    d['Products'] = z
    d2[i+1] = d
print(d2)


#Question 19
d = {'jam':'23','butter':'50','sauce':'43','jelly':'87'}
sum=0
for k,l in d.items():
  sum+=int(l)
print(sum)  

#Question 20
d = {}
for i in range(3):
    x = input('Enter name:')
    y = input('Enter DOB:')
    d[x] = y
x = input('Enter name to search:')
if x in d:
    print('Found')
else:
    y = input('Enter DOB:')
    d[x] = y
print(d)
