#index ელემენტებზე წვდომას თანმიმდევრობის დასაწყისიდან იწყებს (0-დან), ხოლო უარყოფითი index ელემენტებზე წვდომას ბოლოდან იწყებს (-1-დან).
list = ["0d", "1d", "2d", "3d", "4d", "5d"]
print(list)
print(list[3])
print(list[2])
list[5] = "Dato"
print(list)
list[2], list[3] = list[3], list[2]
print(list)
print(list[-2])
numbers = [0, 1, 2, 3, 4, 5, 6,]
print(len(numbers))
name = input()
print(len(name))

