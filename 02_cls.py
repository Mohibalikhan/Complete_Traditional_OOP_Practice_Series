'''
2. Using cls
Create a class Counter that keeps track of how many objects have been created.
Use a class variable and a class method with cls to manage and display the count.
'''
class Counter:
    counter=0

    def __init__(self):
        Counter.counter+=1 # count when object create

    @classmethod
    def show_count(cls):
        print(f"Number of objects created: {cls.counter}")

obj1=Counter()
obj2=Counter()
obj3=Counter()

Counter.show_count()

