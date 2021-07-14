import math

N = int(input())
num_boxes = input()

def Log2(x):
    return (math.log10(x) /
            math.log10(2));

def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)));

if len(num_boxes) == N:
    sum = 0
    for num in num_boxes:
        if (isPowerOfTwo(num)):
            num = int(num)
            sum += num

#sum = b + c

if (isPowerOfTwo(b)) and (isPowerOfTwo(c)):
    print("Y");
else:
    print("N");






