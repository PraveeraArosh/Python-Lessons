str = "Hello little one"

# for i in str:
#     x=str[0]
#     x=x+1
#     if x == "l":
#         count += 1
# print(count)

count = 0
for letter in str:
    if letter == "l":
        count=count+1

print(f"L count is {count}")
print(str.count('l'))

print(str.upper())