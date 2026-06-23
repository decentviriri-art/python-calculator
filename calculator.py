#Student calculator beginner project

operator = input("Enter operator(+,-,/,*,%):")

num1= float(input("Enter first digit:"))
num2 =float(input("Enter second digit:"))

if operator =="+":
    result =num1+num2
    print(result)
elif operator =="-":
    result =num1-num2
    print(result)
elif operator =="/":
    if num2==0:
        print("Zero can not divide")
    else:
        result =num1/num2
        print(result)
elif operator =="*":
    result =num1*num2
    print(result)
elif operator =="%":
    if num2==0:
        print("Zero cant divide")
    else:
        result =num1%num2
        print(result)
else:
    print(f"{operator} does not exist")
