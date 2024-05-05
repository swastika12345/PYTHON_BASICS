#TUPLE PROGRAMS
#Question-1
tuple=(1,2,3,4,5)
print(tuple)
del(tuple)
print(tuple)


#Question-2
tuple1=(1,2,3,4,5)
tuple2=(6,7,8,9,10)
addTuple=tuple1i+tuple2
print("Concatenated tuple is:",addTuple)


#Question-3
tuple=(1,5)
print("Original tuple is:",tuple)
n=int(input("Enter no. of times:"))
res=tuple*n
print("Tuple after repeating same for more than once:",res)


#Question-4
tuple=(1,2,3,4,5)
tuple=tuple[1:3]
print (tuple)

#Question-5
tuple=(1,2,3,4,5)
print (tuple)
print("The length of tuple is:",len(tuple))
print("The maximum item present in a tuple is:",max(tuple))
print("The minimum item present in a tuple is:",min(tuple))

#Question-6
tuple1=(1,2,3,4,5)
print("Original tuple is:",tuple1)
tuple1=tuple1[::-1]
print("Tuple after reversing it:",tuple1)

#Question-7
tuple1=(1,2,3,4,5)
print("Original tuple is:",tuple1)
print("The tuple in string format is ",format(tuple1))

Original tuple is: (1, 2, 3, 4, 5)
The tuple in string format is (1, 2, 3, 4, 5)
