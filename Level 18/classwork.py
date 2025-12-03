# 1)

number = int(input())
if number > 50:
    print(number * 5)
else:
    print(number * number)

# 2)

password = input()
if password == "goa123":
    print("Password is correct!")
else:
    print("incorrect password!")

# 3)

number1 = int(input())
jami = 0
for i in range(1, number1 + 1):
    jami += i
print(jami)