# x = lambda y:y+10
# print(x(4))

# a = lambda x,y:x*y
# print(a(4,8))

# c =lambda a,b,x:a**b+x
# print(c(4,2,7))

# def product(n):
#     return lambda a:a*n

# result = product(10)
# result1 = product(3)
# print(result(4))
# print(result1(4))

# class Number:
#     a = 10
# value = Number()
# print(value.a)

# class Student:
#     def __init__(self,name,age,grade,marks):
#         self.name = name
#         self.age= age
#         self.grade = grade
#         self.marks = marks

#     def __str__(self):
#         return f"{self.name}({self.age})({self.grade})"
# n=Student("Alexander",17,11,100)
# print(n.name)
# print(n.age)
# print(n.grade)
# print(n.marks)
#print(n)

class Employ:
    def __init__(self,name,designation):
        self.name = name 
        self.designation = designation
    
    def identity(self):
        print("Hello, my name is " + self.name)

e1 = Employ("Joshua", 73)
e1.identity()
