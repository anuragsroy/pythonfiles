a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
choice=input("Enter the operation to be performed(*,+,/,%,-): ")

if choice=="*":
    result=a*b
    print("The product is: ",result)
elif choice=="/":
    result = a / b
    print("The quotient is: ", result)
elif choice=="%":
    result = a % b
    print("The remainder is: ", result)
elif choice=="+":
    result = a + b
    print("The sum is: ", result)
elif choice=="-":
    result = a - b
    print("The difference is: ", result)
else:
    print("Wrong choice")
