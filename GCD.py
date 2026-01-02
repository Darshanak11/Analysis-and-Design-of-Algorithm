a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
while b!=0:
    r=a%b
    a=b
    b=r
print("GCD :",a)