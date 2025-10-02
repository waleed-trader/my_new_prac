# def cube(num):
#     result=num*num
#     print(result)
#     squre


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
value= 4
print(factorial(value))