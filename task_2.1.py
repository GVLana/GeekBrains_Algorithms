
def calculations():
    oper = input("Choose the operation: '+', '-', '*', '/'. Enter 0 to stop: ")
    if oper == "0":
        return "The process has been stopped."
    elif oper in "+-*/":
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if oper == '+':
                res = num1 + num2
                print(f"The sum of {num1} and {num2} is: {res}")
                return calculations()
            elif oper == '-':
                res = num1 - num2
                print(f"The difference of {num1} and {num2} is: {res}")
                return calculations()
            elif oper == '*':
                res = num1 * num2
                print(f"The multiplication of {num1} and {num2} is: {res}")
                return calculations()
            elif oper == '/':
                if num2 == 0:
                    print("Can't divided by zero. Choose another second number. ")
                    return calculations()
                else:
                    res = num1 / num2
                    print(f"The division of {num1} and {num2} is: {res}")
                    return calculations()
        except ValueError():
            print("Enter digits not strings. ")
            return calculations()
    else:
        print("The operation sign is not valid. Try again.")
        return calculations()


calculations()
