#Single inheritance - Polymorphism Ex :1
# class Ticket:
#     def entry(self):
#         print("You need a ticket to get entry")

# class Movie(Ticket):
#     def entry(self):
#         print("You need a ticket to get entry to Movie")

# m1 = Movie()
# m1.entry()
# t1 = Ticket()
# t1.entry()

#Single inheritance - Polymorphism Ex :2
# class Message:
#     def msg(self):
#         print("Sending Message............")

# class Whatsapp:
#     def msg(self):
#         print("Sending Message through Whatsapp")

# w1 = Whatsapp()
# w1.msg()
# w1 = Message()
# w1.msg()

#multi-level inheritance - polymorphism Ex-1

# class Content():
#     def show(self):
#         print("Showing content")

# class Video():
#     def show(self):
#         print("Showing Video content")

# class Youtube():
#     def show(self):
#         print("Showing Youtube content")

# y1 = Youtube()
# y1.show()
# v1 = Video()
# v1.show()
# c1 = Content()
# c1.show()


#multi-level inheritance - polymorphism Ex-2

# class Product():
#     def details(self):
#         print("This is your ordered Product")

# class Electronics(Product):
#     def details(self):
#         print("You ordered item is an Electronic gadget")

# class Watch(Electronics):
#     def details(self):
#         print("Your order was a Smart Watch")

# w1 = Watch()
# w1.details()
# e1 = Electronics()
# e1.details()
# p1 = Product()
# p1.details()


#hierarchical - inheritance -polymorphism Ex-2
# class Notification():
#     def Notify(self):
#         print("Got a Notifictaion")

# class Linkedin(Notification):
#     def Notify(self):
#         print("Notification from LinkedIn")

# class facebook(Notification):
#     def Notify(self):
#         print("Notification from Facebook")

# f1 = facebook()
# f1.Notify()
# l1 = Linkedin()
# l1.Notify()
# n1 = Notification()
# n1.Notify()

#multiple inheritance - polymorphism Ex-1
# class Gps():
#     def track(self):
#         print("Feature - GPS")

# class Camera():
#     def track(self):
#         print("Feature - Camera")

# class Drone(Gps, Camera):
#     def track(self):
#         print("Drone have both GPS and Cam feature")
# d1 = Drone()
# d1.track()
# c1 = Camera()
# c1.track()
# g1 = Gps()
# g1.track()



#multiple inheritance - polymorphism Ex-2
# class Plus():
#     def cell(self):
#         print("Positive End = + ")

# class Minus():
#     def cell(self):
#         print("Negative End = - ")

# class Battery(Plus, Minus):
#     def cell(self):
#         print("Battery have both +ve and -ve Ends")
# b1 = Battery()
# b1.cell()
# m1 = Minus()
# m1.cell()
# p1 = Plus()
# p1.cell()