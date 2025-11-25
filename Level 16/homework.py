# 1)

# i = 10
# while i >= -10:
#     print(i)
#     i -=1

# 2)

# for i in range(1, 101, 2):
#     print(i)

# 3)

password = "goa123"
attempts = 3
user_password = input("Please enter your password (3 attempts): ")
while user_password != password and attempts != 1:
    print("Password is incorrect! Try again!")
    attempts -= 1
    print(str(attempts) + " attempt remaining.")
    user_password = input()