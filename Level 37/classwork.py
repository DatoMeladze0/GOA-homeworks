#1)

# def sigrdze(list):
#     index = 0
#     for element in list:
#         index += 1
#     return index
# print(sigrdze([1, 3, 4, 5, 6,]))

#2)

# def ipove(text, symbol,):
#     index = 0
#     for i in text:
#         if i == symbol:
#             return index
#         index += 1
# print(ipove("blabla", "a"))

#3)

def insertit(list, index, value):
    list1 = []
    stop = len(list) - index
    for i in range(stop):
        list1.append(value)
insertit([1, 3, 4, 5, 6, 7], 4, 'bre')