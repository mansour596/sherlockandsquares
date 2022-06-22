import math

def sns(x, y):

    a = math.ceil(math.sqrt(x))
    b = math.floor(math.sqrt(y))
    result = b - a + 1

    return result

print(sns(3, 9))
print(sns(17, 24))
print(sns(1, 1000000000))