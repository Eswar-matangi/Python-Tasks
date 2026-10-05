# print("---MENU---")
# print("1.Biryani")
# print("2.Chicken 65")
# print("3.Veg pulav")
# print("4.Butter chicken")
# print("5.Panner Tikka")

# choice = int(input("Enter your choice : "))
# match choice :
#     case 1 :
#         print("Item : Biryani")
#         print("Price : ₹250")
#         print("Description : Fragnant Basmati rice cooked with spices and chicken")
#     case 2 :
#             print("Item : Chicken 65")
#             print("Price : ₹180")
#             print("Description : Crispy and spicy deep-fried chicken pieces ")
#     case 3 :
#             print("Item : Veg Pulav")
#             print("Price : ₹220")
#             print("Description : Crispy and spicy deep-fried chicken pieces ")

#     case 4 :
#             print("Item : Butter chicken")
#             print("Price : ₹180")
#             print("Description : Yummy and Chef's special")
#     case 5 :
#             print("Item : Panner Tikka")
#             print("Price : ₹180")
#             print("Description : Grilled panner cubes marinated with spices and yogurt")
#     case _:
#               print("Sorry not Available  😔!!!")


print("---ATM MENU---")
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

current_bal = 10000

choice = int(input("Enter your choice : "))
match choice :
    case 1 :
        print("Current Balance : 10000")
    case 2 :
            deposit = int(input("Enter deposit amount : "))
            Updated_bal = current_bal + deposit
            print("Updated balance : ",Updated_bal)
            
    case 3 :
            withdraw_amt  = int(input("enter withdrawal amount : "))
            remaining_bal = current_bal - withdraw_amt
            print("Remaining balance : ",remaining_bal) 
            
    case 4 :
            print("Exit")
    case _:
            print("Invalid Try again!!")

