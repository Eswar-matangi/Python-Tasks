print("================1.Refridgerator - class==================")


class Fridge:
    deepFreezer = True
    WillConsumeElectricity = True
    def __init__(self,brand,rating,no_of_doors,warranty,price):
        self.brand = brand
        self.rating = rating
        self.no_of_doors = no_of_doors
        self.warranty = warranty
        self.price = price
    def displayDetails(self):
        print("------------------------------------------")
        print("Brand Name of fridge : ",self.brand)
        print("Rating  : ",self.rating)
        print("No of doors fridge have: ",self.no_of_doors)
        print("Years of warrenty providing: ",self.warranty)
        print("Deep-Freezer Available : ",Fridge.deepFreezer)
        print("Will consume Electricity : ",Fridge.WillConsumeElectricity)
        print("Price : ",self.price)

        print("------------------------------------------")

f1 = Fridge("LG","5-Star",1,"10",40000)
f1.displayDetails()

f2 =  Fridge("Samsung","4-Star",2,"8",30000)
f2.displayDetails()

f3 = Fridge("WhirlPool","5-Star",2,"15",50000)
f3.displayDetails()

print("================2.Food - class==================")

class Food:
    haveSomeTaste = "Good"
    chef_special = "Chicken Pulav"

    def __init__(self,name,type,spiceLevel,price):
        self.name = name
        self.type = type
        self.spiceLevel = spiceLevel
        self.price = price
    def showitems(self):
        print("------------------------------------------")
        print("Was the food good here ? :",Food.haveSomeTaste)
        print("Whats Special dish here? : ",Food.chef_special)
        print("Name of the food item : ",self.name)
        print("Type of food : ",self.type)
        print("spiceLevel of food : ",self.spiceLevel)
        print("Price :",self.price)
        print("------------------------------------------")

f1 = Food("Biryani","Amma Chethi Vanta","Spicy","Free")
f1.showitems()

f2 = Food("Pizza","Junk_food","Moderate spicy",600)
f2.showitems()

f3 = Food("Fruit-Bowl","Healthy","NO-spice",250)
f3.showitems()

print("================3.Bank - class==================")


class Bank():
    wasBankGovtApproved = True
    working_hours = 6

    def __init__(self,bank_name,branch,pincode,deposit,withdraw):
        self.bank_name = bank_name
        self.branch = branch
        self.pincode = pincode
        self.deposit = deposit
        self.withdraw = withdraw

    def show(self):
        print("------------------------------------------")
        print("Was the bannk approved by Government : ",Bank.wasBankGovtApproved)
        print("Bank Name : ",self.bank_name)
        print("Which Branch : ",self.branch)
        print("pincode : ",self.pincode)
        print("deposit amt : ",self.deposit)
        print("NO of working hours : ",Bank.working_hours)
        print("Withdrawal amt : ",self.withdraw)
        print("------------------------------------------")
b1 = Bank("Karur Vysya","Vijayawada",521137,5000,500000)
b1.show()

b2 = Bank("Andhra bank","Hyderabad",523601,2000,1000)
b2.show()

b3 = Bank("SBI","CHennai",652014,80000,0)
b3.show()