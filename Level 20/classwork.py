# 1)
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
jami = num1 + num2 + num3 + num4 + num5
if jami % 2 == 0:
    print(jami, "aris luwi")
else:
    print(jami, "aris kenti")

# 2)
num = int(input())
while num % 5 != 0 or num % 7 != 0:
    num = int(input())
print(num)

# 3)
balance = int(input())
if balance >= 1500:
    print("ლეპტოპი")
elif balance >= 1000:
    print("ტელეფონი")
elif balance >= 100:
    print("ფეხსაცმელი")
elif balance >= 50:
    print("პერანგი")
elif balance >= 5:
    print("რვეული")
else:
    print("you cant afford anything")

# 4)
number = int(input())
if number == 0:
    print(number, "aris nuli")
elif number > 0:
    print(number, "aris dadebiti")
elif number < 0:
    print(number, "aris uaryofiti")