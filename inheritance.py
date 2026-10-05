# print("1. single - inheritance with out constructor")

# class Art:
#     print("I'm an artist")
# class Painter(Art):
#     print("I'm a painter")
# p = Painter()


# print(" 2.single inheritance with a constructor")
# class Sport:
#     def __init__(self,name,no_of_players):
#         self.name = name
#         self.no_of_players = no_of_players
#     def show(self):
#         print("Sport Name : ",self.name)
#         print("No.of Players/Tuoo n eam : ",self.no_of_players)

# class Cricket(Sport):
#     def play(self):
#         pass
# c1 = Cricket("Cricket",11)
# c1.show()


# # 3.single inheritance with constructor + super()
# class Bank:
#     def __init__(self, bank_name):
#         self.bank_name = bank_name

#     def show_bank(self):
#         print("Bank Name:", self.bank_name)


# class Hyd(Bank):
#     def __init__(self, bank_name, branch):
#         super().__init__(bank_name)
#         self.branch = branch

#     def show_branch(self):
#         print("Branch:", self.branch)


# h1 = Hyd("Andhra Bank", "Hyderabad")

# h1.show_bank()
# h1.show_branch()

# 4.single inheritance with constructor + super() Real-World-Ex

# class Student:
#     def __init__(self,name,age,marks,result):
#         self.name = name
#         self.age = age
#         self.marks = marks
#         self.result = result

#     def show(self):
#         print("Student name : ",self.name)
#         print("Student age : ",self.age)
#         print("Student marks : ",self.marks)
#         print("Student result : ",self.result)

# class Topper(Student):
#     def __init__(self, name, age, marks, result,rank):
#         super().__init__(name, age, marks, result)
#         self.rank = rank

#     def info(self):
#         super().show()
#         print("Rank : ",self.rank)
#         print("====================")

# t1 = Topper("Eswar",21,98,"Pass",1)
# t1.info()
# t1.show()


# 5.multiple inheritance with out constructor

# class Animal:
#     def anim(self):
#         print("This is Animal")
# class Mammel(Animal):
#     def mamm(self):
#         print("This is mammel")
# class Whale(Mammel):
#     def wha(self):
#         print("This is Whale")
# w = Whale()
# w.anim()
# w.mamm()
# w.wha()

# 6.Multiple level- constructor

# class Employee:
#     def __init__(self,name):
#         self.name = name
#         print("I'm an employeee")
#     def show(self):
#         print("Employee name : ",self.name)
#         print("====================")
# e1 = Employee("Eswar")
# e1.show()
# class Manager(Employee):
#     def __init__(self, name , exp):
#         self.name = name
#         self.exp = exp
#     def showw(self):
#         print("I'm a Manager")
#         print("Employee name :",self.name)
#         print("Employee Experience : ",self.exp)
#         print("===================")
# m1 = Manager("Eswar","2Yrs")
# m1.showw()

# class GeneralManager(Manager):
#     def __init__(self, name, exp ,role):
#         self.name = name
#         self.exp = exp
#         self.role = role
#     def showww(self):
#         print("Im General Manager")
#         print("Employee name :",self.name)
#         print("Employee Experience : ",self.exp)
#         print("Employee Roles : ",self.role)
# gm = GeneralManager("Eswar","2Yrs","Managing Processes")
# gm.showww()




# 7.Multiple - level inherit + constructor+Super()
# class abcd:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print("Hiiiiiiiiiiiiii This is Eswar")

# class efgh(abcd):
#     def __init__(self, name , age ):
#         super().__init__(name)
#         self.age = age
#     def details(self):
#         super().show()
#         print("Age : ",self.age)

# class ijkl(efgh):
#     def __init__(self, name, age , role):
#         super().__init__(name, age)
#         self.role = role
#     def info(self):
#         super().details()
#         print("Role : ",self.role)
# i = ijkl("Eswar",22,"Developer")
# i.info()
# i.details()
# i.show()



# 8..multiple - inherit with constructor + super (Real - world EX)

# class Product():
#     def __init__(self,name):
#         self.name = name
#     def info(self):
#         print("Product name : ",self.name)

# class Electronics(Product):
#     def __init__(self, name,type):
#         super().__init__(name)
#         self.type = type
#     def infoo(self):
#         super().info()
#         print("Product Type : ",self.type)

# class Mobile(Electronics):
#     def __init__(self, name, type , price):
#         super().__init__(name, type)
#         self.price = price
#     def infooo(self):
#         super().infoo()
#         print("Product Price : ",self.price)

# m1 = Mobile("OppoA3 Pro","Electronic gadget",30000)
# m1.infooo()
# print("============")
# m1.infoo()
# print("==============")
# m1.info()