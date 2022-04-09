import math
def flip_bits(num):
    for i in range(int(math.log2(num)+1)):
        num = (num ^ (1 << i))
    return num

def subtract(x, y):
    negative = False
    if y > x:
        x,y = y,x
        negative = True

    while y != 0:
        b_not_a  = flip_bits(x) & y
        x = x^y
        y = b_not_a << 1
    

    print(x if not negative else x * -1)   
