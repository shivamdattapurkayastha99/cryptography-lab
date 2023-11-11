def mpy(x, y):                  # mpy two 8 bit values
    p = 0b100011011             # mpy modulo x^8+x^4+x^3+x+1
    m = 0                       # m will be product
    for i in range(8):
        m = m << 1
        if m & 0b100000000:
            m = m ^ p
        if y & 0b010000000:
            m = m ^ x
        y = y << 1
    return m
x=12
y=2
print(mpy(x,y))