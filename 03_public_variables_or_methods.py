'''
3. Public Variables and Methods
Create a class Car with a public variable brand and a public method start().
Instantiate the class and access both from outside the class.'''

class Car:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print(f"{self.brand} is starting") # public method

car1=Car("Mercedes") # create object
car1.start() #call method

print(car1.brand)  # access variable
