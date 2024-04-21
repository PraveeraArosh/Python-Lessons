# x="python{}"
# y= '\nHello world ---'
# z= """\nHello word....""" #Doc Strings 
# # print(type(x),x)
# # checked the type
# # print(x,y,z)

# q= "Elephant"
# p=0
# print(type(p))
# print(x.format(p))
# print (x+q+str(p))

# print(f"Praveera Arosh{q}")

# b=0.0
# print(type(b))

# print("Git upload")

# print("New")

# l1=[1,2,3,"arosh",0.0]
# print(l1[3])
# print(l1[0:4])

# print(len(l1))

# Tuple
tuple1=(1,2,3,4,5)
# print(tuple1)

is_created = False
is_failed = True

# print(is_created,type(is_created))

# if 2>0:
#     is_created=True # convert False value as True
# print(is_created)

# set1=set("Arosh","Arosh","Arosh")
# list1=["Arosh","Arosh","Arosh"]

dic={
    "Name":"Arosh",
    "mobile":1900,
    "Age":19
}
dic2={
    "Name":"Arosh",
    "mobile":1900,
    "Age":19
}
print(dic["Name"])
list=[]
# add 2 dicts into 1 list

list.append(dic)
list.append(dic2)
print(list)

import pandas as pd

dataframe= pd.DataFrame(list)
print(dataframe.head())
print(dataframe.tail())
print(type(dataframe))


