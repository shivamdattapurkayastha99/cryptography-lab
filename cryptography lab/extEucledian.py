def gcdExtended(a, b):
 
    
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y
x=3
y=6
gcd,x,y=gcdExtended(x,y)
print(gcd)