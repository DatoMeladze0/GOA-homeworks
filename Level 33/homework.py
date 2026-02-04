# 1)

# .append() ამატებს ახალ ელემენტს სიის ბოლოში. .insert() ამატებს მითითებულ ელემენტს, მითითებულ index-ზე. .pop() ამოიშლის სიიდან მითითებულ ელემენტს.

# 2)

list = ["item1", "item2", "item3"]
print(len(list))

# # 3)

list1 = []
user_input = input()
list1.append(user_input)

# # 4)

colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop(-1)
print(colors)

# # 5)

animals = ["dog", "cat", "elephant", "lion"]
animals.insert(2, "monkey")
print(animals)

# 6)

students = []
for i in range(3):
    user_student = input()
    students.append(user_student)
students.insert(0, "Teacher")
students.pop(-1)
print(len(students))
print(students)

# 7)

#Custom ფუნქციები არის ფუნქციები, რომლებსაც პროგრამისტი თავად ქმნის კონკრეტული დავალების შესასრულებლად. ისინი გამოიყენება იმისთვის, რომ ერთი და იგივე კოდი ბევრჯერ არ 
# დავწეროთ, ფუნქციის შექმნისთვის იწერება def, შემდეგ ფუნქციის სახელი, ფრჩხილებში პარამეტრები (საჭიროების შემთხვევაში), შემდეგ : და ქვემოთ იწერება ფუნქციის კოდი. პარამეტრები 
# არის ცვლადები, რომლებიც ფუნქციის შექმნის დროს იწერება მონაცემის მისაღებად, ხოლო არგუმენტები არის რეალური მნიშვნელობები, რომლებსაც ფუნქციას ვაწვდით მისი გამოძახების დროს.

# 8)

def jami(number1, number2):
    print(number1 + number2)
jami(3, 4)

# 9)

def luwi_or_not(number):
    if number % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")
luwi_or_not(214)

# 10)

def kvadrati(number):
    print(number * number)
kvadrati(5)

# 11)

def upper(word):
    print(word.upper())
upper("monke")

# 12)

def namestuff(name, last_name):
    print(name + last_name)
namestuff("davit", " meladze")