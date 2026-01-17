# 1)
cars = ["Toyota", "Ford", "Volkswagen", "Honda", "Chevrolet", "BMW", "Mercedes", "Hyundai", "Nissan", "Tesla"]

# 2)
print(cars[5])

# 3)
new_cars = cars[1 : 6]
print(new_cars)
print(new_cars[-1])

# 4)
print(cars[: : 2])

# 5)
print(cars[3 : 8 : 3])

# 6)
new_cars_2 = cars[0 : 6]
print(new_cars_2[: : -1])

# 7)
new_cars_3 = cars
cars[8] = "ferrari"
print(new_cars_3)
print(cars)

# 9)
sia = [2, 3, 4, 5, 6]
for i in sia:
    print(i)