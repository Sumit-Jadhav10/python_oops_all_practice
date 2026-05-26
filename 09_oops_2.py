# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def avrage(self):  
#         sum =0  
#         for i in range(0,3):
#             sum+=self.marks[i]
#         avrages=sum/3  
#         return avrages  

# s=student("sumit",[23,34,56])
# print(s.name)
# print(s.avrage())


# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         total = 0
#         for i in range(len(self.marks)):
#             total += self.marks[i]
#         avg = total / len(self.marks)
#         return avg


# s = student("sumit", [23, 34, 56])

# print(s.name)
# print(s.average())

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         return sum(self.marks) / len(self.marks)


# class account():
#     def __init__(self,balance,account_no):
#         self.balance=balance
#         self.account_no=account_no

# acc =account(125000000,1251130011)
# print(acc.balance)        
# print(acc.account_no)        

# class Account:
#     def __init__(self, account_no, balance):
#         self.account_no = account_no
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient Balance")

#     def show_balance(self):
#         print("Current Balance:", self.balance)


# # Object
# acc1 = Account(12345, 5000)

# acc1.deposit(1000)
# acc1.withdraw(2000)
# acc1.show_balance()

# class student:
#     def __init__(self,name,age,roll_no):
#         self.name=name
#         self.age=age
#         self.roll_no=roll_no
#     def desplay(self):
#         print(f"name:{self.name}")    
#         print(f"age:{self.age}")
#         print(f"roll_no:{self.roll_no}")

# s1=student("sumit",19,19)        
# s1.desplay()

# s2=student("amit",20,67)
# s2.desplay()      


# class car:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def desplay(self):
#         print("brand of the car:",self.brand)    
#         print("price  of the car:",self.price)    

# c1=car("BMW",12500000)
# c2=car("AUDI",10000000)
# c1.desplay()
# c2.desplay()

# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         print( f"the area of the rectangle is :{self.length*self.breadth}")
# a1=rectangle(25,35)
# a2=rectangle(19,34)
# a1.area()
# a2.area() 

# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length*self.breadth
# a1=rectangle(25,35)
# a2=rectangle(19,34)
# print( f"the area of the rectangle 1 is :{a1.area()}")
# print( f"the area of the rectangle 2 is :{a2.area()}")

# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return math.pi*self.radius**2
# a1=Circle(3)        
# a2=Circle(3.14)        

# print( f"the area of the circle 1 is :{a1.area()}")
# print( f"the area of the cirlce 2 is :{a2.area()}")

# class Account:
#     def __init__(self,balance,account_no):
#         self.balance=balance
#         self.account_no=account_no
#     def withdrawn(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print(f"{amount} has been withdrow from your account.")
#             print(f"{self.balance} has been left in  your account.")
#         else:
#             print("insufficient balance")    
#             return self.balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"{amount} has been deposited from your account.")
#         print(f" total balance {self.balance} you  have in   your account.")
#         return self.balance
# a1=Account(25000,1234)        
# a1.withdrawn(10000)
# a1.deposit(1000000)
# a2=Account(1000000,12345)
# a2.withdrawn(125000)

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def increase_salary(self):
#         self.salary+=self.salary/10
#         return self.salary
# e1=Employee("sumit",125000)
# print(f"{e1.name} has salary: {e1.salary}")
# print(f"After 10% increase, new salary is: {e1.increase_salary()}")        


# class Student:
#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks=marks
#     def average(self):
#         total = 0
#         for i in range(len(self.marks)):
#             total += self.marks[i]
#         return total / len(self.marks)


# s1 = Student("Sumit", [29, 31, 30])

# print(f"Average marks: {s1.average()}")


# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def display(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
# b1=Book("alpha","sumit")        
# b1.display()

# class Laptop:
#     def __init__(self,brand,ram):
#         self.brand=brand
#         self.ram=ram
#     def display(self):
#         print(f"brand:{self.brand}")    
#         print(f"ram:{self.ram}")    
# l1=Laptop("lanovo","16gb")
# l1.display()

# class Counter:
#     def __init__(self):
#         self.count = 0

#     def increase(self):
#         self.count += 1

#     def display(self):
#         print("Current Count:", self.count)


# c1 = Counter()

# c1.increase()
# c1.increase()

# c1.display()

# class User:
#     def __init__(self, password):
#         self.password = password

#     def check_password(self, input_password):
#         if input_password == self.password:
#             print("Correct Password")
#         else:
#             print("Wrong Password")


# u1 = User("1234")

# u1.check_password("1234")
# u1.check_password("abcd")

# class Number :
#     def __init__(self,num):
#         self.num=num
#     def even_or_odd(self):
#         if self.num%2==0:
#             print(f"the number {self.num} is even")
#         else:
#             print(f"the number {self.num} is odd")        
# n1=Number(23)
# n1.even_or_odd()

# class Number:
#     def __init__(self, num):
#         self.num = num

#     def even_or_odd(self):
#         if self.num % 2 == 0:
#             return "Even"
#         else:
#             return "Odd"
# n1 = Number(23)
# print(f"The number {n1.num} is {n1.even_or_odd()}")


# class Account:
#     def __init__(self,balance,account_no):
#         self.balance=balance
#         self.account_no=account_no
#     def withdrawn(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print(f"{amount} has been withdrow from your account.")
#         else:
#             print("insufficient balance")    
#             return self.balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"{amount} has been deposited from your account.")
#         return self.balance
#     def check_balance(self):
#          print(f"{self.balance} has been left in  your account.")
#          print(f" total balance {self.balance} you  have in   your account.")
# a1=Account(25000,1234)        
# a1.withdrawn(10000)
# a1.deposit(1000000)
# a2=Account(1000000,12345)
# a2.withdrawn(125000)
# a1.check_balance()
# a2.check_balance()

    # this one is wrong down one
# class Account:
#     def __init__(self,balance,account_no):
#         self.balance=balance
#         self.account_no=account_no
#     def withdrawn(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print(f"{amount} has been withdrow from your account.")
#             return self.balance
#         else:
#             print("insufficient balance")    
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"{amount} has been deposited from your account.")
#         return self.balance
#     def check_balance(self):
#          print(f" total balance {self.balance} you  have in   your account.")
# a1=Account(25000,1234)        
   
# print(f"{a1.withdrawn(1000)} has been left  from your bank")
# print(f"{a1.deposit(100000)} has been left  in  your bank")
# a1.check_balance()

# a1.withdrawn(10000)
# a1.deposit(1000000)
# a2=Account(1000000,12345)
# a2.withdrawn(125000)
# a1.check_balance()
# a2.check_balance()
#          tis is wrong , up one 
# 
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} has been withdrawn from your account.")
            return self.balance
        else:
            print("Insufficient balance!")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited into your account.")
        return self.balance

    def check_balance(self):
        print(f"Total balance: {self.balance}")


a1 = Account(25000, 1234)

a1.withdraw(1000)
a1.deposit(100000)
a1.check_balance()  
