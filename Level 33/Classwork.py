# 1)
names = ["name1", "name2", "name3", "name4", "name5"]
# user = input()
# names.append(user)
print(names)
# 2)
names.insert(3, "Tarieli")
# 3)
names.pop(3)
# 4)
names.remove("name1")
# 5)
username = input()
if username in names:
    print(names.index(username))
else:
    print("not in list")