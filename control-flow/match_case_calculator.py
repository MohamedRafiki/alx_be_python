#prompt user to enter the first number
num1 = float(input("Enter the first number: "))
#prompt user to enter the second number
num2 = float(input("Enter the second number: "))
#prompt user to choose the operation 
operation = input("choose the operation (+, -, *, /): ")
match operation:
    case "+":
        result = num1 + num2
        print(f"The result of addition is: {result}")
    case "-":
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    case "/":
        if num2 != 0:
            result = num1/ num2
            print(f"The result of division is: {result}")
        else:
            print("Error:cannot divide by zero")
    case _:
        print("Eroor: Invalid operation")


