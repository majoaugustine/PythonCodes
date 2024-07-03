num1=float(input("first number:"))
operator = input("enter operator(+,-,/,*):")
num2=float(input("second number:"))
if(operator =="+"):
    print(num1+num2)
elif(operator=="-"):
    print(num1-num2)
elif(operator=="*"):
    print(num1*num2)
elif(operator=="/"):
    print(num1/num2)
else:
    print("error")