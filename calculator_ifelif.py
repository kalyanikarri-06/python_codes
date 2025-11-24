num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
operator = input("enter the operator: ")
if operator == "+":
    print(f"Addition is:{num1+num2}")
elif operator == "-":
    print(f"Substration is:{num1-num2}")
elif operator == "*":
    print(f"Multiplication is:{num1*num2}")
elif operator == "/":
    if num2>num1:
       print(f"Division is:{num2/num1}")
    else:
       print(f"not valid")
elif operator == "%":
    if num2>num1:
        print(f"Modular is:{num2%num1}")
    else :
        print(f"not valid")
else:
    print(f"enter the valid operator")

