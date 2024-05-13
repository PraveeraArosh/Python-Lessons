# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# odd_numbers = [num for num in numbers if num % 2 != 0]
#
# even_numbers = [num for num in numbers if num % 2 == 0]
#
# print("Odd Numbers:", odd_numbers)

# print("Even Numbers:", even_numbers)

start_no = input("Enter start no ")
end_no = input("Enter start no ")
numbers = [i for i in range(int(start_no),int(end_no),1)]
print(numbers)

def checked_odd_or_even(numbers: list)-> dict:
    odd_list = []
    even_list = []
    for number in numbers:
        if float(number)%2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    return {
        "odd_list ": odd_list,
        "even_list": even_list
    }

print(checked_odd_or_even(numbers))
