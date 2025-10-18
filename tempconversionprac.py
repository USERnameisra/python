symbol = str(input("enter celcius for C and Fahrenheit for F: "))
num =float(input("input num: "))



if symbol == "c":
    RESULTf =  (num * 9/5) + 32
    print(f"Fahrenheit: {round(RESULTf,2)} f")
elif symbol == "f":
    RESULTc = (num - 32) * 5/9
    print(f"Fahrenheit: {round(RESULTc,2)} c")
else:
    print("invalid symbol")
