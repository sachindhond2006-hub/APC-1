a=int(input("Enter number A: "))
b=int(input("Enter number B: "))
c=int(input("Enter number C: "))

if a>b and a>c:
    print("a is largerst")
elif b>a and b>c:
    print("b is largerst")
else:
    print("c is largerst")

if a<b and a<c:
    print("a is smallest")
elif b<a and b<c:
    print("b is smallest")
else:
    print("c is smallest")