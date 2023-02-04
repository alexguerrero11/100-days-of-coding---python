def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)


add(3, 4, 5)


def calculate(n, **kwargs):
    # prints a dictionary
    print(kwargs)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)


calculate(3, add=3, multiply=5)

# class Car:
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
