'''
number = [1,2,3,4,5]

def takeasquare(x):
    c= x*x
    return c

def takeeven(x):
     if x%2 ==0
     return x
result= map(takesquare,number)
result1=filter(takeeven,number)

print(list(result))
print(list(result1))
'''
A = [1,2,3]
B = [4,5,6]

result = list(map(lambda x,y: x+y, A,B))
print (result)
    