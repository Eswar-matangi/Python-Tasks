#1check wheater the given num is a 3 digit number or not
# n = int(input("Enter a number  : "))
# if(n >99 and n<1000):
#     print(f"Yes {n} is a 3 digit number")
# else:
#     print(f"{n} is not a 3 digit number")


#2.check weather the given number is div by both 3 qnd 5
# n = int(input("Enter a number  : "))
# if(n%3==0 and n%5==0):
#     print(f"{n} is divisible by bot-h 3 and 5")
# else:
#     print("not divisible")


#3.check weather the given triangle is a valid traiangle or not
# s1 = int(input("Enter length of first side : "))
# s2 = int(input("Enter length of Second side: "))
# s3 = int(input("Enter length of Third side : "))

# if(s1+s2>s3 and s1+s3>s2 and s2+s3>s1):
#     print(f"Yes {s1,s2,s3} forms a Traingle")
# else:
#     print(f"{s1,s2,s3} do not form a Traingle")


#4.check weather the given number is multiple of 10 or not
# n = int(input("Enter a number : "))
# if(n%10 == 0):
#     print(f"Yes {n} is multiple of 10")
# else:
#     print(f"{n} is not a multiple of 10")


#if-elif-else:

#1.Check the type of triangle based on its type
# s1 = int(input("Enter length of first side : "))
# s2 = int(input("Enter length of Second side: "))
# s3 = int(input("Enter length of Third side : "))

# if(s1==s2==s3):
#     print(f"{s1,s2,s3} form a equilateral triangle")
# elif(s1==s2!=s3 or s1==s3!=s2 or s2==s3!=s1):
#     print(f"{s1,s2,s3} form a Isosceles triangle")
# else:
#     print(f"{s1,s2,s3} form a Scalen triangle")



#2.Cal of electricity bill
# units = int(input("Enter no of units consumed : "))
# if(units>=0 and units<=100):
#     print(f"Total bill is Rupees : {units*2}")
# elif(units>100 and units<=200):
#     print(f"Total bill is Rupees : {units*3}")
# elif(units>200 and units<=300):
#     print(f"Total bill is Rupees : {units*5}")
# elif(units>300):
#     print(f"Total bill is Rupees : {units*7}")


#3.Display age category

# age = int(input("Enter the age : "))
# if(age<13):
#     print("Child")
# elif(age>=13 and age<=19):
#     print("Teenager")
# elif(age>=20 and age<60):
#     print("Adult")
# elif(age>=60):
#     print("Senior citizen")

#4.cal discount based on bill
# bill = int(input("Enter your bill anount : "))
# if(bill<1000):
#     print("No discount")
# elif(bill>=1000 and bill <=4999):
#     print(f"Final bill after discount is: {bill - bill*0.10}")
# elif(bill>=5000 and bill<10000):
#     print(f"Final bill after discount is: {bill - bill*0.20}")
# elif(bill>=10000):
#     print(f"Final bill after discount is: {bill - bill*0.30}")


#5.Display the season based on month number
# month = int(input("Enter a number : "))
# if(month>=3 and month<6):
#     print("Spring")
# elif(month>=9 and month<12):
#     print("Autumn")
# elif(month == 12 or month == 1 or month == 2):
#     print("Winter")

#6.check weather the given number is leap year or not
# year = int(input("Enter a year : " ))
# if(year%400 == 0):
#     print(f"{year} is a leap year")
# elif(year %4==0 and year%100!=0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

#Nested if :
#1.check whether a person is eligible to donate blood
# age = int(input("Enter your age : "))
# weight = int(input("Enter your weight : "))
# if(age>=18 and age<=60):
#     if(weight >50):
#         print("Eligible to donate blood")
#     else:
#         print("Not eligible by weight")
# else:
#     print("Not eligible by age")

#2.Display grades only if student passed in all 4 subjects

# maths_marks = 35
# science_marks = 35
# english_marks = 35
# social_marks = 35

# avg = (maths_marks + science_marks + english_marks + social_marks )/4

# if(maths_marks>=35 and science_marks>=35 and english_marks>=35 and social_marks>=35):
#     if(avg>90 and avg<=100):
#         print("A")
#     elif(avg>80 and avg<=90):
#         print("B")
#     elif(avg>70 and avg<=80):
#         print("C")
#     elif(avg>60 and avg<=70):
#         print("D")
#     else:
#         print("E")
# else:
#     print("Fail")


#Check whether the student is eligible for scolarship or not 1)age>18 2)score>86

# age = int(input("Enter student age : "))
# score = int(input("Enter Student score : "))

# if(age>18):
#     if(score>86):
#         print("Eligible for scholorship")
#     else:
#         print("Not eligible by score")
# else:
#     print("Not eligible by age")