# class Car(object):
# 	wheels = 4
# 	fuel = "diesel"

# 	def __init__(self, make, model):
# 		self.make = make
# 		self.model = model

# 	def print(self):
# 		print("Your car is: ", self.make, self.model, self.fuel, self.wheels, "wheels")

# mustang = Car('Ford', 'Mustang')
# print (type(mustang))
# print(mustang.wheels)
# print(mustang.make)
# mustang.print()




class Car(object):
    wheels = 4
    fuel = "diesel"

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def print(self):
        print("Your car is: ", self.make, self.model, self.fuel, self.wheels, "wheels")

mustang = Car('Ford', 'Mustang')
print(type(mustang))
print(mustang.wheels)
print(mustang.make)
mustang.print()
mercedes = Car('Benz', 'Class A')
print(type(mercedes))
print(mercedes.wheels)
mercedes.wheels = 8
print(mercedes.make)
mercedes.print




# class Car(object):
#     wheels = 4
#     fuel = "diesel"
#
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#
#     def print(self):
#         print("Your car is: ", self.make, self.model, self.fuel, self.wheels, "wheels")
#
# class Window(object):
#
#
#     def __init__(self):
#         self.size=40
#         self.type="metal"
#
#
#
#
# mustang= Car('Ford', 'Mustang')
# my_home_window = Window()
# print(mustang.wheels)
# print(mustang.make)
# print(my_home_window.type)