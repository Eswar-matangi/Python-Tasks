# print("----------Named-fn without input & without return----")
# def swapTwo():
#     a=10
#     b=20
#     a=a+b
#     b=a-b
#     a=a-b
#     print(f"a after swap : {a}")
#     print(f"b after swap : {b}")
# swapTwo()

# def posOrNeg():
#     a=20
#     if(a>0):
#         print(f"{a} is positive")
#     elif(a<0):
#         print(f"{a} is negative")
# posOrNeg()


# def singleDigit():
#     n=1
#     if(n>=0 and n<10):
#         print(f"{n} is single digit num")
#     else:
#         print("NO")
# singleDigit()


# def leapYear():
#     y=2001
#     if(y%400==0):
#         print(y, "is leap year")
#     elif(y%100!=0 and y%4==0):
#         print(y, "is not a leap year")
#     else:
#         print(y, "is Not a leap year")
# leapYear()


# def hello5():
#     n=5
#     for i in range(1,n+1,1):
#         print("Hello")
# hello5()


# def sumNum():
#     n=3
#     sum=0
#     for i in range(1,n+1,1):
#         sum+=i
#     print(sum)
# sumNum()


# def revNum():
#     n=12345
#     rev=0
#     while(n!=0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     print(rev)
# revNum()


# def primeNum():
#     print("prime numbers between range[1-10]")
#     for j in range(1,11,1):
#         n=j
#         count=0

#         for i in range(1,n+1,1):
#             if(n%i==0):
#                 count+=1

#         if(count==2):
#             print(n)
# primeNum()


# def eligible():
#     age=18
#     if(age>=18):
#         print("Eligible to vote")
#     else:
#         print("not eligible")
# eligible()



# def factors():
#     n=10
#     print(f"factors of {n} are")
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             print(i)
# factors()

# #-----------------------------------------------------------------------------
# print("---Named-fn with input & without return---")


# def swapTwo(a,b):

#     a=a+b
#     b=a-b
#     a=a-b
#     print(f"a after swap : {a}")
#     print(f"b after swap : {b}")
# swapTwo(10,20)

# def posOrNeg(a):
  
#     if(a>0):
#         print(f"{a} is positive")
#     elif(a<0):
#         print(f"{a} is negative")
# posOrNeg(20)


# def singleDigit(n):

#     if(n>=0 and n<10):
#         print(f"{n} is single digit num")
#     else:
#         print("NO")
# singleDigit(1)


# def leapYear(y):
    
#     if(y%400==0):
#         print(y, "is leap year")
#     elif(y%100!=0 and y%4==0):
#         print(y, "is not a leap year")
#     else:
#         print(y, "is Not a leap year")
# leapYear(2000)


# def hello5(n):
#     for i in range(1,n+1,1):
#         print("Hello")
# hello5(5)


# def sumNum(n):
#     sum=0
#     for i in range(1,n+1,1):
#         sum+=i
#     print(sum)
# sumNum(3)


# def revNum(n):
#     rev=0
#     while(n!=0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     print(rev)
# revNum(1234)


# def primeNum(n):
#     print("prime numbers between range[1-10]")

#     for j in range(1,n+1,1):
#         n=j
#         count=0

#         for i in range(1,n+1,1):
#             if(n%i==0):
#                 count+=1

#         if(count==2):
#             print(n)
# primeNum(10)


# def eligible(age):
#     if(age>=18):
#         print("Eligible to vote")
#     else:
#         print("not eligible")
# eligible(20)



# def factors(n):
#     print(f"factors of {n} are")
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             print(i)
# factors(10)

# #-----------------------------------------------------------------------------
# print("---Named-fn without input & with return---")

# def swapTwo():
#     a=10
#     b=20
#     a=a+b
#     b=a-b
#     a=a-b
#     return a,b
# print(swapTwo())

# def posOrNeg():
#     a=20
#     if(a>0):
#         return f"{a}-positive"
#     elif(a<0):
#         return f"{a}-negative"
# print(posOrNeg())


# def singleDigit():
#     n=1
#     if(n>=0 and n<10):
#         return f"{n} is single digit num"
#     else:
#         return "NO"
# print(singleDigit())


# def leapYear():
#     y=2001
#     if(y%400==0):
#         return f"{y} is leap year"
#     elif(y%100!=0 and y%4==0):
#         return f"{y} is not leap year"
#     else:
#         return f"{y} is not leap year"
# print(leapYear())

# def hello5():
#     n = 5
#     result = ""
#     for i in range(1, n+1, 1):
#         result += "hello\n"
#     return result
# print(hello5())

# def sumNum():
#     n=3
#     sum=0
#     for i in range(1,n+1,1):
#         sum+=i
#     return sum
# print(sumNum())


# def revNum():
#     rev=0
#     n=12345
#     while(n!=0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     return rev
# print(revNum())


# def primeNum():
#     print("prime numbers between range[1-10]")
#     res = ""
#     for j in range(1,11,1):
#         n=j
#         count=0

#         for i in range(1,n+1,1):
#             if(n%i==0):
#                 count+=1

#         if(count==2):
#             res +=str(n) + " "
#     return res
# print(primeNum())


# def eligible():
#     age=18
#     if(age>=18):
#         return "Eligible"
#     else:
#         return "Not eligible"
# print(eligible())



# def factors():
#     res = ""
#     n=10
#     print(f"factors of {n} are")
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             res = res + str (i) + "\n"
#     return res
# print(factors())

# #-----------------------------------------------------------------------------
# print("---Named-fn with input & with return---")

# def swapTwo(a,b):
  
#     a=a+b
#     b=a-b
#     a=a-b
#     return a,b
# print(swapTwo(10,20))


# def posOrNeg(a):
#     if(a>0):
#         return f"{a}-positive"
#     elif(a<0):
#         return f"{a}-negative"
# print(posOrNeg(20))


# def singleDigit(n):
#     if(n>=0 and n<10):
#         return f"{n} is single digit num"
#     else:
#         return "NO"
# print(singleDigit(1))


# def leapYear(y):
#     if(y%400==0):
#         return f"{y} is leap year"
#     elif(y%100!=0 and y%4==0):
#         return f"{y} is not leap year"
#     else:
#         return f"{y} is not leap year"
# print(leapYear(2001))

# def hello5(n):
#     result = ""
#     for i in range(1, n+1, 1):
#         result += "hello\n"
#     return result
# print(hello5(5))

# def sumNum(n):
#     sum=0
#     for i in range(1,n+1,1):
#         sum+=i
#     return sum
# print(sumNum(3))


# def revNum(n):
#     rev=0
#     while(n!=0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     return rev
# print(revNum(12345))


# def primeNum(n):
#     print("prime numbers between range[1-10]")
#     res = ""
#     for j in range(1,n+1,1):
#         n=j
#         count=0

#         for i in range(1,n+1,1):
#             if(n%i==0):
#                 count+=1

#         if(count==2):
#             res +=str(n) + " "
#     return res
# print(primeNum(10))


# def eligible(age):
#     if(age>=18):
#         return "Eligible"
#     else:
#         return "Not eligible"
# print(eligible(18))



# def factors(n):
#     res = ""
#     print(f"factors of {n} are")
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             res = res + str (i) + "\n"
#     return res
# print(factors(10))


