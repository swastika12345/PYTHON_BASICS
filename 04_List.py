#Question-1
list1=[1,2,4,6,8,9,13,15,18]
print("The Original ist is:",list1)

@Question-2
list1=[1,2,4,6,8,9,13,15,18]
print("The Original ist is:",list1)
n=int(input("Enter index which is to be deleted:"))
del list1[n]
print("List after deletion is:",list1)

#Question-3
list1=[1,2,4,6,8,9,13,15,18]
list2=[3,4,5,67,89,90,130]
list3=list1+list2
print("The concatenated list is:",list3)


#Question-4
list1=[]
for i in range(3,10):
	list1.append(i)
print("The Original list is:",list1)


#Question-5
list1=[1,2,4,6,8,9,13,15,18]
print("ith to jth item in a list is:",list1[1:4])


#Question-6
#Convert List to tuple
list1=[1,2,4,6,8,9,13,15,18]
print("The Original list is:",list1)
list1=tuple(list1)
print("List after converting it to Tuple is:",list1)


#Question-7
list1=[1,2,4,6,8,9,13,15,18]
print("The Original list is:",list1)
print("The Length of the list is:",len(list1))
print("The maximum element in the list is:",max(list1))
print("The minimum element in the list is:",min(list1))


#Question-8
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[11,12,13,14,15,16,17,18,19, 20]
list1.append("big")
print("List after appending an item to list1:",list1)
for i in range(22,24):
list2.append(i)
print("List after appending a tuple to list2:",list2)
list3=listi+list2
print("List after concatenation is:",list3)
n=int(input("Enter item:"))
print("The index of n item is:",list3.index(n))
index=int(input("Enter index:"))
list3.insert(index, 30)
print(list3)
m=int(input("Enter index where the element is to be deleted:"))
del list3[m]
print("After deletion list becomes:",list3)
list3.remove(6)
print("List after removing 6 is:",list3)
list4=list3[::-1]
print("After Reversing the list becomes:",list4)


#Question-9
list1=[1,2,4,6,8,9,13,15,18]
print("The Original list is:",list1)
n=int(input("Enter element to be searched:"))
print(n in list1)


#Question-10
list1=[]
for i in range(1,11):
	list1.append(i**3)

print("List is:",list1)


#Question-11
list1=[1,2,4,6,8,9,13,15,18]
print("The Original list is:",list1)
n=int(input("Enter element to be searched:"))
print(n in list1)


#Question-12
str1=input("Enter a sentence")
str2=" "
List=[]
List=str1.split()
List1=[]
List1=List[::-1]
for i in List1:
  str2=str2+" "+i
print(" ")
print(str2)  


#Question-13
str=input("Enter word")
List=[]
for i in str:
  List.append(i)
c=0
for i in List:
   ch=i
   for j in List:
     ch1=j
     if(ch1 == ch):
       c=c+1
   print("Frequency of",ch,"is",c)
   c=0      
