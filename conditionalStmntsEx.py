# if False :
#     print("If block ~ Executed")
# print("If block ended")

# #write a prgrm to neck weather it is = 10

# n = 10
# if(n==10):
#     print("If block satisfied and o/p is true")

# #write a prgm whin gives 15% discount on bill if its >5000 cal total_bill after discount0.

# bill = int(input("enter bill : "))


# if (bill>5000):
#     discount = (15/100)*bill

#     total_bill = bill - discount
#     print(total_bill)

#if - else 
# if True:
#     print("True : If block is executed")
# else:
#     print("False : Else block is executed")

#Write a prgm to neck given num = 10 
# n = int(input("enter your number : "))
# if(n==10):
#     print("True : n is equal to 10")
# else:
#     print("False : n is not equal to 10")

#neck weather the given num is +ve or -ve

# n = 10
# if(n<0):
#     print("negative")
# else:
#     print("Positive")

#write a prgm to find the biggest number amg 2 vals

# a = int(input("enter a val : "))
# b = int(input("enter b val : "))

# if(a>b):
#     print("a is greater than b")
# else:
#     print("b is greater than a")

#neck the given number is even or odd
# n = int(input("enter a number : "))
# if(n%2!=0):
#     print(n," is Odd number")
# else:
#     print(n," is Even number")

#write a code to neck given value is ovel or not

# n = input("enter a letter : ")
# if(n == "a" or n =="e" or n=="i" or n=="o" or n=="u" or n == "A" or n =="E" or n=="I" or n=="O" or n=="U"):
#     print(n , " is Ovel letter")
# else:
#     print("not Ovel")

#write a prgm to neck given value is alphabet or not

# n = input("enter a letter: ")
# if(n>= "A" and n<="Z") or (n>="a" and n<="z"):
#     print("given letter is a valid alphabet")
# else:
#     print("Invalid!!!")

#write a program to neck given value is digit or not

# n = "2"
# if(n>="0" and n<"10"):
#     print(n, " is a digit")
# else:
#     print("not a digit")

#write a prgm login

# name = input("enter your name : ")
# password = input("enter your password : ")
# if(name == "Hero" and password =="Hero@123"):
#     print("Loginn Sucessful")
# else:
#     print("Ivnalid Credentials!!!")

#falsy value neck

# if(set()):
#     print("True ~ execute if block")
# else:
#     print("False ~ executes else block")

#elif usage

# if(False):
#     print("cnondition 1 is True : Executes if block")
# elif(True):
#     print("cnondition 1 is false & 2 is True : Executes if block")
# elif(True):
#     print("cnondition 1&2 is false & 3 is True : Executes if block")
# else:
#     print("cnondition 1,2,3 is False & 4 is True  : Executes if block")







# amt = 0
# if(amt>= 500):
#     print("go to cake neloufer")
# elif(amt>100 and amt<=300):
#     print("go to local cafe")
# elif(amt>0 and amt<100):
#     print("go to gully shop")
# else:
#     print("nai is injurious to health!!!")

#neck for a number is positive,negative anad zero
 
# n = int(input("enter a number : "))
# if(n<0):
#     print("negative")
# elif(n>0):
#     print("Positive")
# else:
#     print("zero")


#neck given vallue is alphabet ,digit,or symbol

# n = "10"
# if(n>="a" and n<="z" or n>="A" and n<="Z"):
#     print("the entered value is an Alphabet")
# elif(n>="0" and n<"10"):
#     print("the entered value is a Digit")
# else:
#     print("the entered value is a Symbol")

# marks = int(input("enter marks : "))
# if(marks>90 and marks<=100):
#     print("Outstanding")
# elif(marks>70 and marks<=90):
#     print("A")
# elif(marks>50 and marks<=70):
#     print("B")
# elif(marks>35 and marks<=50):
#     print("C")
# else:
#     print("Fail")

#nested - if block 

# if(False):
#     print("outer if executes")
#     if(True):
#         print("inner if executes")
#     else:
#         print("inner else executes")
# else:
#     print(" only outer else executes")


#check a num is even or odd only if positive

# num = int(input("enter a num : "))
# if(num>0):
#     if(num%2==0):
#         print(num, "is positive and even")
#     else:
#         print(num, "is positive and Odd")
# else:
#     print(num, "  is negative number")

# display the smallest amng 2 num only if they are not equal

# n1 = 10
# n2 = 10
# if(n1!=n2):
#     if(n1<n2):
#         print(n1, " is smaller than ", n2)
#     else:
#         print(n2, " is smaller than ",n1)
# else:
#     print(n1,n1 ," are equal")

#multiple if

# if(True):
#     print("1st if is executed")
# if(False):
#     print("2nd if is executed")
# if(False):
#     print("3rd if is executed")

# Match case--switch case

# ch = 4
# match ch:
#     case 1 : 
#         print("Case1 will be executed")
#     case 2:
#         print("Case2 will be executed")
#     case 3 :
#         print("Case3 will be executed")
#     case 4:
#         print("Case4 will be executed")
#     case _:
#         print("Default case will be executed")


# write a progm on traffic light red-stop orange-ready green-go

# color = "red"
# match color :
#     case "red" :
#         print("Stop the vehicle and relax boss !!!🤚")
#     case "orange" :
#         print(" start your bike and Ready to go ~💥")
#     case "green" : 
#         print("you can Gooooooooo, have a safe journey😊")
#     case _:
#         print("Traffic light error !!!!🚫")

# sides = 3
# match sides :
#     case 1 :
#         print("Line")
#     case 2:
#         print("less than or greater than shape")
#     case 3:
#         print("triangle")
#     case 4 :
#         print("rectangle or square ")
#     case 5:
#         print("Pentagon")
#     case 6 :
#         print("Hexagon")
#     case _:
#         print("invalid!!!!!!!!!!!!")


# day = 0
# match day:
#     case 0 :
#         print("Monday")
#     case 1 :
#         print("Tuesday")
#     case 2 :
#             print("Wednesday")
#     case 3 :
#             print("Thursday")
#     case 4 :
#             print("Friday")
#     case 5 :
#             print("saturday")
#     case 6:
#             print("Monday")
#     case _:
#             print("Invalid - day ")



#Match-case 
# print("Enter 2 numbers")
# n1 =  int(input("Enter num 1  : "))
# n2 =  int(input("Enter num 2 : "))

# print("1.Add")
# print ("2.Sub")
# print("3.Div")
# print("4.Mul")
# print("5.Remainder")

# op = (input("Select an option from the given choices : "))

# match op:
#     case "1":
#         print("Add = ",(n1+n2))
#     case "2":
#         print("Sub = ",(n1-n2))
#     case "3":
#         print("Div = ", (n1/n2))
#     case "4":
#         print("Mul = ",(n1*n2))
#     case "5":
#             print("Remainder = ",(n1%n2))
#     case _:
#         print("No operation performed")


# f_name = "Innomatics"
# m_name = "Research"
# l_name = "Labs"
# full_name = f_name +" "+ m_name +" "+ l_name
# print(full_name)

name ="Eswar"
age = 21
salary = 50000
gender = "m"

print("Without : My name is "+name+" My age is "+str(age)+" My gender is "+gender+" My salary is "+str(salary))
print(f"My name is {name} My age is {age} My gender is {gender} My salary is {salary}")
print(f"{10+20}")