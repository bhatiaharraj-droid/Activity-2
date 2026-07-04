#data types
#it tells python what kind of information we are storing
age = 25
name="harraj"
print(type(age))
#type casting
#it means changing one data type into another 
marks =95
marks =str(marks)
print(type(marks))

#user input
#it means taking information from the user
name=input("enter ur name")
print("the name is",name)

#String
#it is collection of charecter
#indexing
#it means accessing one charecter from a string using its position
#p y t h o n

# 0 1 2 3 4 5-----positive Indexing or position

# P Y T H O N

# -6-5-4-3-2-1
name="harraj"
print(name[0])
print(name[-2])


#slicing
#it means taking a part of a string
name="harraj"
print(name[2:4])

#concatination
#it means joinging two or more strings using the + opretor
first = "hello"
second = "world"
print(first+" "+second)


text=input("enter ur name")
revtext=text[::-1]
print("the reversed string is",revtext)