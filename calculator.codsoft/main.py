def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        return "No division"
    return x / y


def multiply(x, y):
    return x * y


print("select an operation")
print("1. add")
print("2. subtract")
print("3. divide")
print("4. multiply")

picked_operation = input("Enter your choice: ")
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))

if picked_operation == '1':
    result = add(num1, num2)
    print(result)
elif picked_operation == '2':
    result = subtract(num1, num2)
    print(result)
elif picked_operation == "3":
    result = divide(num1, num2)
    print(result)
elif picked_operation == "4":
    result = multiply(num1, num2)
    print(result)
else:
    print("invalid")
