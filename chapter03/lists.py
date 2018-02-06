motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(1, 'ducati')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

last = motorcycles.pop()
print(motorcycles)
print(last)

first = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first.title() + '.')


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)

print(len(cars))

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])
# IndexError: list index out of range

print(motorcycles[-1])

# empty = []
# print(empty[-1])
# IndexError: list index out of range
