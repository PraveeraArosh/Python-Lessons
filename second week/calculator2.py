
num1= float(input("Input number 1 : "))
num2= float(input("Input number 2 : "))


def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2



print("Select operation.")


print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:

    choice = input("Enter your input number as 1 2 3 4 : ")

    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print(add(num1, num2))

        elif choice == '2':
            print(subtract(num1, num2))

        elif choice == '3':
            print(multiply(num1, num2))

        elif choice == '4':
            print(divide(num1, num2))
        break
    else:
        print("Invalid Input")