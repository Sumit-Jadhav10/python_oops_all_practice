# class Person:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print("Name:", self.name)


# class Student(Person):
#     def __init__(self, name, marks):
#         super().__init__(name)   # call parent constructor
#         self.marks = marks

#     def display(self):
#         print("Marks:", self.marks)


# s1 = Student("Sumit", 90)

# s1.show()
# s1.display()

# class person:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print("name:",self.name)    


# class student(person):
#     def __init__(self,name,marks):
#         super().__init__(name)
#         self.marks=marks

#     def display(self):
#         print("marks",self.marks)
# s1=student("sumit",100)
# s1.show()
# s1.display()

# class Animal:
#     def __init__(self,food):
#         self.food=food
    
#     def eat(self):
#         print("the dogs eat meat")

# class Dog(Animal):
#     def __init__(self,food,barks):
#         super().__init__(food)
#         self.barks=barks

#     def bark(self):
#         print("the dog can bark")

# d1=Dog("meal","bhau")
# d1.bark()
# d1.eat()

# class Vehicle:
#     def __init__(self,switch):
#         self.switch=switch
#     def start(self):
#         if self.switch.lower() == "on":
#             print("the vehicle switch is",self.switch)
#             print("the vehicle is start")
#         elif self.switch.lower() == "off":
#             print("the vehicle switch is",self.switch)
#             print("the vehicle is OFF")
#         else:
#             print("Invalid switch value")
# class Car(Vehicle):
#     def drive(self):
#         print("you can drive the car when you have driving lianace")             
# s1=Car("oF")
# s1.start()
# s1.drive()        

# class Person:
#      def __init__(self,name):
#           self.name=name
#      def show(self):
#           print(f"the name of the person is :{self.name}")     

# class Student(Person):
#      def __init__(self,name,marks):
#           super().__init__(name)
#           self.marks=marks
#      def display(self):
#           print(f"the marks is {self.marks}")

#      def average(self):
#           return sum(self.marks)/len(self.marks)
    
# s1=Student("sumit",[12,34,56,78])
# s1.show()
# s1.display()
# print(f"avrage :{s1.average()}")


# class Employee:
#      def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# class Manager(Employee):
#      def __init__(self,name,salary,bonus):
#         super().__init__(name,salary)
#         self.bonus=bonus

#      def total_salary(self):
#         print(f"{self.name} get {self.bonus}% bonus ")
#         print(f"total salary :{self.salary+(self.salary*(self.bonus/100))}")
               
# m1=Manager("sumit",15000000,20)
# m1.total_salary()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# class Manager(Employee):
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)
#         self.bonus = bonus

#     def total_salary(self):
#         total = self.salary + (self.salary * self.bonus / 100)
#         return total


# m1 = Manager("Sumit", 1500000, 20)

# print(f"Name: {m1.name}")
# print(f"Total Salary after bonus: {m1.total_salary()}")         

# class Shape:
#     def __init__(self,length,bredth):
#         self.length=length
#         self.bredth=bredth
#     def area(self):
#         return self.length*self.bredth    
# class Rectangle(Shape):
#     def __init__(self,length,bredth):
#         super().__init__(length,bredth)

# r1=Rectangle(25,35)
# print(f"the total area is:{r1.area()}" )

# class Shape:
#     def area(self):
#         print("Area not defined")


# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):   # overriding
#         return self.length * self.breadth


# r1 = Rectangle(25, 35)
# print(f"Area: {r1.area()}")

# class Account:
#     def __init__(self,balance):
#         self.balance=balance

# class Savingsaccount(Account):
#     def __init__(self, balance,instrust):
#         super().__init__(balance)
#         self.instrust=instrust
#     def add_instrust(self):
#         return self.instrust
        
#     def after_interest(self):
#         return self.balance+(self.balance*(self.instrust/100))
# s1=Savingsaccount(100000,7)
# print(f"Before instrust:{s1.balance}")     
# print(f"Total inctement:{s1.add_instrust()}")
# print(f"After intrust :{s1.after_interest()} ")

# class Account:
#     def __init__(self, balance):
#         self.balance = balance


# class SavingsAccount(Account):
#     def __init__(self, balance, interest):
#         super().__init__(balance)
#         self.interest = interest

#     def add_interest(self):
#         interest_amount = self.balance * self.interest / 100
#         return interest_amount

#     def total_balance(self):
#         return self.balance + self.add_interest()


# s1 = SavingsAccount(100000, 7)

# print(f"Initial Balance: {s1.balance}")
# print(f"Interest Amount: {s1.add_interest()}")
# print(f"Total Balance after Interest: {s1.total_balance()}")

# class Person:
#     def __init__(self,name):
#         self.name=name
# class Employee(Person):
#     def __init__(self, name,salary):
#         super().__init__(name)
#         self.salary=salary
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")    
# e1=Employee("sumit",125000)
# e1.display()     




# Class A
# Class B inherits A
# Class C inherits B
# Show all methods working

# class A:
#     def school(self):
#         print("school have classes")
# class B(A):
#     def classes(self):
#         print("classes have teacher")
# class C(B):
#     def teacher(self):
#         print("teacher teach student")

# c1=C()
# c1.teacher()
# c1.classes()
# c1.school()



# Class Person → name
# Class Student → marks
# Class Teacher → subject
# Show inheritance properly

# class Person:
#     def __init__(self,name):
#         self.name=name

# class Student(Person):
#     def __init__(self, name,marks):
#         super().__init__(name)
#         self.marks=marks

# class Teacher(Student):
#     def __init__(self, name, marks,subject):
#         super().__init__(name, marks)        
#         self.subject=subject

# t1=Teacher("sumit",30,"maths")
# print("name:",t1.name)
# print("marks:",t1.marks)
# print("subject:",t1.subject)




# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, marks):
#         super().__init__(name)
#         self.marks = marks

# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

# s1 = Student("Sumit", 90)
# t1 = Teacher("Rahul", "Maths")

# print("Student Name:", s1.name)
# print("Marks:", s1.marks)

# print("Teacher Name:", t1.name)
# print("Subject:", t1.subject)




# Class Shape → method area()
# Class Circle → override area()
# Class Rectangle → override area()

# import math
# class Shape:
#         def area(self):
#             print("all shape has area")
# class Circle:
#         def __init__(self,radius):
#               self.radius=radius
#         def area(self):
#             return math.pi*self.radius**2
# class Rectangle:
#         def __init__(self,length,breadth):
#             self.length=length      
#             self.breadth=breadth
#         def area(self):
#             return self.length*self.breadth
# s1=Shape()
# c1=Circle(3)
# r1=Rectangle(25,26)
# s1.area()
# print(f"area of circle:{c1.area()}")        
# print(f"area of rectangle:{r1.area()}")


# import math

# class Shape:
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2


# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth


# # Polymorphism in action
# shapes = [Circle(3), Rectangle(25, 26)]

# for shape in shapes:
#     print(f"Area: {shape.area()}")








#     Create Class Account
# Attributes:
# account_no
# balance
# 🔹 Methods:
# 1. deposit(amount)
# Add money
# Print updated balance
# 2. withdraw(amount)
# If balance is enough → deduct
# Else → print "Insufficient balance"
# 3. check_balance()
# Show current balance
# ⭐ Advanced (Optional – for extra learning)
# 🔹 Add Class SavingsAccount (Inheritance)
# Inherit from Account
# Add interest
# Method → add_interest()

# class Account:
#     def __init__(self,account_no,balance):
#         self.account_no=account_no
#         self.balance=balance
#     def deposit(self,amount):
#         self.amount=amount
#         self.balance+=self.amount
#         print(F"diposit money:{self.amount}")
#     def withdraw(self,amount):
#         self.amount=amount
#         if amount>self.balance:
#             print("insuficient balance")
#         else:
#             self.balance-=self.amount
#             print(f"withdrawn money:{self.amount}")
#     def check_balance(self):
#         print(F"total balance{self.balance}")
# class Savingaccount(Account):
#     def __init__(self, account_no,balance,saving_amount):
#         super().__init__(account_no,balance)
#         self.saving_amount=saving_amount
#     def save(self):
#         if self.balance<self.saving_amount:
#             print("insuficient balance")
#         else:
#             self.balance-=self.saving_amount
#         print(f"you save:{self.saving_amount}")
#     # def check_balance(self):
#     #     print(F"total balance{self.balance}")



# a1=Account(1234,100000)
# a1.deposit(2000)
# a1.withdraw(1000)
# a1.check_balance()
# s1=Savingaccount(1234,100000,2000)
# s1.save()
# s1.save()
# s1.save()
# s1.check_balance()


# class Savingaccount(Account):
#     def __init__(self, account_no,saving_amount,balance):
#         super().__init__(account_no,balance)
#         self.saving_amount=saving_amount
#     def save(self):
        
#         self.saving_amount=self.saving_amount

#         print(f"you saved:{self.saving_amount}")
#     def check_balance(self):
#         print(F"total balance{self.balance}")
    # def total_saving(self):
    #     self.balance+=self.saving_amount
    #     print(F"{self.balance}")
    #     pass 


# class Account:
#     def __init__(self, account_no, balance):
#         self.account_no = account_no
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}")

#     def check_balance(self):
#         print(f"Total balance: {self.balance}")


# class SavingAccount(Account):
#     def __init__(self, account_no, balance, saving_amount):
#         super().__init__(account_no, balance)
#         self.saving_amount = saving_amount

#     def save(self):
#         if self.saving_amount > self.balance:
#             print("Not enough balance to save")
#         else:
#             self.balance -= self.saving_amount
#             print(f"You saved: {self.saving_amount}")


# # Testing
# a1 = Account(1234, 100000)
# a1.deposit(2000)
# a1.withdraw(1000)
# a1.check_balance()

# print("-----")

# s1 = SavingAccount(1234, 100000, 2000)
# s1.save()
# s1.save()
# s1.save()
# s1.check_balance()




# class ATM:
#     def __init__(self,account_no,balance,pin):
#         self.account_no=account_no
#         self.balance=balance
#         self.pin=pin

#     def check_pin(self):
#         correct_pin =0
#         mainu=0
#         while True:
#             correct_pin=int(input("enter the pin:"))
#             if correct_pin==self.pin:
#                 print("valid pin ")
                
#                 mainu = int(input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nENTER:"))

#                 return True
#             else:
#                 print("invalid pin ")
    
#     def deposit(self,amount):
#         self.amount=amount
#         self.balance+=self.amount
#         print(F"amount deposited:{self.amount}")

#     def withdraw(self,amount):
#         if self.amount>self.balance:
#            print("invalid amount")
#         else:
#             print(f"amount withdraw:{self.amount}")

#     def check_balance(self):
#         print(f"total balance:{self.balance}")

# a1=ATM(123,10000,1234)
# a1.check_pin() 
# a1.deposit(1000)




# class ATM:
#     def __init__(self, account_no, balance, pin):
#         self.account_no = account_no
#         self.balance = balance
#         self.pin = pin

#     def check_pin(self):
#         while True:
#             entered_pin = int(input("Enter PIN: "))
#             if entered_pin == self.pin:
#                 print("PIN verified ✅")
#                 self.menu()
#                 break
#             else:
#                 print("Invalid PIN ❌ Try again")

#     def menu(self):
#         while True:
#             choice = int(input("\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit\nEnter choice: "))

#             if choice == 1:
#                 amount = int(input("Enter amount: "))
#                 self.deposit(amount)

#             elif choice == 2:
#                 amount = int(input("Enter amount: "))
#                 self.withdraw(amount)

#             elif choice == 3:
#                 self.check_balance()

#             elif choice == 4:
#                 print("Thank you! 👋")
#                 break

#             else:
#                 print("Invalid choice")

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance ❌")
#         else:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}")

#     def check_balance(self):
#         print(f"Current Balance: {self.balance}")


# # Run
# a1 = ATM(123, 10000, 1234)
# a1.check_pin()


# class ATM:
#     def __init__(self, account_no, balance, pin):
#         self.account_no = account_no
#         self.balance = balance
#         self.pin = pin

#     def check_pin(self):
#         count=0
#         while True:
#             if count==3:
#                 print("come after one day")
#                 break
#             entered_pin = int(input("Enter PIN: "))
#             if entered_pin == self.pin:
#                 print("PIN verified ✅")
#                 self.menu()
#                 break
#             else:
#                 count+=1
#                 print("Invalid PIN ❌ Try again")
#                 print(f"your {count} chance is over")
                
                

#     def menu(self):
#         while True:
#             choice = int(input("\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit\nEnter choice: "))

#             if choice == 1:
#                 amount = int(input("Enter amount: "))
#                 self.deposit(amount)

#             elif choice == 2:
#                 amount = int(input("Enter amount: "))
#                 self.withdraw(amount)

#             elif choice == 3:
#                 self.check_balance()

#             elif choice == 4:
#                 print("Thank you! 👋")
#                 break

#             else:
#                 print("Invalid choice")

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance ❌")
#         else:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}")

#     def check_balance(self):
#         print(f"Current Balance: {self.balance}")


# # Run
# a1 = ATM(123, 10000, 1234)
# a1.check_pin()
        

class ATM:
    def __init__(self, account_no, balance, pin):
        self.account_no = account_no
        self.balance = balance
        self.pin = pin
        self.total_withdrawn=0

    def check_pin(self):
        attempts = 0

        while attempts < 3:
            entered_pin = int(input("Enter PIN: "))

            if entered_pin == self.pin:
                print("PIN verified ✅")
                self.menu()
                return
            else:
                attempts += 1
                print("Invalid PIN ❌")
                print(f"{3 - attempts} attempts left")

        print("Too many attempts! Come after one day 🚫")

    def menu(self):
        while True:
            choice = int(input("\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit\nEnter choice: "))

            if choice == 1:
                amount = int(input("Enter amount: "))
                self.deposit(amount)

            elif choice == 2:
                amount = int(input("Enter amount: "))
                success = self.withdraw(amount)

                if success == False:
                    print("No more withdrawals allowed today 🚫")
                    break   # ✅ stops menu after limit reached

            elif choice == 3:
                self.check_balance()

            elif choice == 4:
                print("Thank you! 👋")
                break

            else:
                print("Invalid choice")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance ❌")

        elif self.total_withdrawn + amount > 5000:
            print("₹5000 daily withdrawal limit exceeded ❌")
            return False

        else:
            self.balance -= amount
            self.total_withdrawn += amount   # ✅ update total
            print(f"Withdrawn: {amount}")
            

    def check_balance(self):
        print(f"Current Balance: {self.balance}")


# Run
# a1 = ATM(123, 10000, 1234)
# a1.check_pin()
a2=ATM(1010,100000,1020)
a2.check_pin()