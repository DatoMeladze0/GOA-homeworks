# 1)

# number = int(input())
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print(factorial)

# 2)

#% გაყოფის ოპერატორი გვაძლევს მიღებულ ნაშთს გაყოფის შემდეგ. იგი გვეხმარება ლუწი/კენტი რიცხვების გარჩევაში. მაგალითად:
# 10 % 3 = 1
# 8 % 2 = 0
# 7 % 2 = 1

# 3)

number1 = int(input())
for i in range(1, number1 + 1):
    if number1 % i == 0:
        print(i)