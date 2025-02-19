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

# class Employ:
#     def __init__(self,name,designation):
#         self.name = name 
#         self.designation = designation
    
#     def identity(self):
#         print("Hello, my name is " + self.name)

# e1 = Employ("Joshua", 73)ww
# e1.identity()

class Book:
    def __init__(self,title,genre,price):
        self.title=title
        self.genre=genre
        self.price=price
    # def __str__(self):
    #     return f"Title:{self.title},Genre:{self.genre},Price:{self.price}"
    def sample(self):
        print("The name of the book is " + self.title)

book1 = Book("Randonm sock","Horror",21)
book1.price=30
book1.title = "Random soccer ball"
print(book1.title)
print(book1.price)
del book1.genre
# print(book1.genre)

del book1
print(book1)
# print(book1)
book1.sample()
