# class calculator:
#     def plus(x,y):
#         return x+y
    
#     def minus(x,y):
#         return x-y
    
#     def multiply(x,y):
#         return x*y
    
#     def divide(x,y):
#         return (x/y)
    
# a= input("enter the value")
# b= input("enter the value")

# print(plus(a,b))

class calculator:
    a=0
    b=0
    def setvalue(self,x,y):
        self.a=x
        self.b=y
    def add(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
    
p1= calculator()
p1.setvalue(5,5)
print(p1.add())
print(p1.minus())
print(p1.multiply())
print(p1.divide())