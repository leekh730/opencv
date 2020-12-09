a = int(input("first num : "))
b = int(input("second num : "))

def sum():
    result = a + b
    return result

print(sum())

first, second = input("Input Two num : ").split(',')

def sum1(a, b):
    resulta = int (a)
    resultb = int (b)
    result = resulta + resultb
    return result, resulta, resultb

print(sum1(first, second))
