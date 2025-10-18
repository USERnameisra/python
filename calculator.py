operator = str(input("input operator +, -, /, *,:  "))

num1 = int(input("input first number: "))
num2 = int(input("input second number: "))



if operator == "+":
         result = num1 + num2 
         print(f"result:{result}")
elif operator == "-":
       result = num1 - num2 
       print(f"result:{result}")
elif operator == "*":
        result = num1 * num2 
        print(f"result:{result}")
elif operator == "/":
        result = num1 / num2 
        print(f"result:{result}")
else:
        print("not valid")
        




