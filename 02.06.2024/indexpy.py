# def GetCount(valuelist):
#     return valuelist.count(0)
#
# input_list = [0,1,2,0,5]
# zero = GetCount(input_list)
# print(zero)

# first code
def check_zero(values:list)->int:
    count = 0
    for value in values:
        if value == 0:
            count +=1
    return count

print(check_zero([0,1,2,0,1,0]))

