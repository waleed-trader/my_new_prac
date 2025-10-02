mobiles=['m1','m2','m3']

def showMobile(mob):
    A1 = mob.copy()
    A1.append('m5')
    return A1

res = showMobile(mobiles)
res.append("m6")
print(res)
a = showMobile(mobiles)
print (a)

# print("con",mobiles)


'''
x=10
y=x
print(x)
print(y)

y=x
x=12
print(x)
print(y)
'''