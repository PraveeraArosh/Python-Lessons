# f = open('sample1.txt',"r")
# print(type(f),f)
# lines = f.readlines()
# print(lines)
#
#
# print(lines[5])
# for line in lines:
#     if line !=" ":
#         print(line)

# f = open('sample1.txt',"r")
# text = f.read()
# print(text)

with open("sample1.txt") as my_file:
    print(my_file.read())
