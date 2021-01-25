def add(*nums):
    suma = 0
    for i in nums:
        suma += i
    return suma
suma = add(1,2,3,4,5,6,7,8,9,10)
print(suma)


def calculate(n, **kwargs):
    kwargs['multiply'] = 1
    n += kwargs['add']
    n *= kwargs['multiply']
    return n
print(calculate(2, add=8))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get('model')

my_car = Car(make='Nissan')
print(my_car.make)
print(my_car.model)
