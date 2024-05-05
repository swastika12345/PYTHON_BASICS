#String

#by nature immutable

#collection of characters

#Define :mutable, immutabLe, buffer, builder
#Question-1
stri='Swastika'
print(len(str1))
n=len( ‘Swastika’ )
print(n)


#Question-2
stri='swastika kayal'
str2=str1.capitalize()
print(str2)
str3=stri.title()
print(str3)
str4=str1.isupper()
print(str4)
str5=str1.islower()
print(str5)


#Question-3
stri='abcdabef'
print(str1.count(‘ab',3))
stri='abcdabef'
print(str1.count('ab',3,5))
stri='abcdabef'
print(str1.count('‘ab'))


#Question-4
stri=' '
print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str1.isspace())

#Question-5
stri=' swastika kayal'
print(str1.1strip())
print(str1.rstrip())
print(stri.strip())


#Question-6
stri='swastika'
str2='*"
str3=str2.join(str1)
print(str3)

#Question-7
stri='swastika'
str2=str1.upper()
print(str2)


#Difference between partition and split
#Question-8
stri='Swastika is going to invatation’
str2=stri1.split('a')
print(str2)
str3=stri1.partition('a')
print(str3)


