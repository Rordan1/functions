class Car:
    """assigning properties"""
    def __init__(self, name):
        self.name = name
    #   self.price = price

    def display(self):
        print("this vehicle is a", self.name)

c1 = Car('Toyota')
c2 = Car('Mustang')
c3 = Car('Ferrari')

c1.display()
c2.display()
c3.display()



"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def monthly_payment(x, y):
        divide = x / y
        return divide
    print(monthly_payment(20, 10))"""