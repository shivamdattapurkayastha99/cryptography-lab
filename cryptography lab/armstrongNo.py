def isArmstrong(n):
    l=len(n)
    num=int(n)
    num1=num
    s=0
    while num!=0:
        d=num%10
        s+=pow(d,l)
        num//=10
    if s==num1:
        return 1
    else:
        return 0
n=input("Enter the number")
if isArmstrong(n):
    print(f"{n} is armstrong")
else:
    print(f"not armstrong")
