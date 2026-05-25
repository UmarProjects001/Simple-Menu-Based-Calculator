A=int(input("Enter your first number:"))
B=int(input("Enter your second number:"))
print("Choose your arithmetic operation by entering the number before your preffered operator")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Floor division")
print("6.Modulus")
print("7.Exponents")
int(input("Enter your operation:"))
if input==1:
    print(A+B)
elif input==2:
    print(A-B)
elif input==3:
    print(A*B)
elif input==4:
    print(A/B)
elif input==5:
    print(A//B)
elif input==6:
    print(A%B)
elif input==7:
    print(A**B)
else:
    print("Please enter a working operator given above")
