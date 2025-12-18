count = 0

while True:
    num = int(input("sheiyvanet ricxvi (sheiyvanet 0 gacherebistvis): "))
    if num == 0:
        print("programa shecherebulia")
        break
    elif num > 0:
        print("dadebiti ricxvi")
        for i in range(1, num + 1):
            print(i)
    else:
        print("uaryofiti ricxvi")

    count += 1
print("sheyvanili ricxvebis raodenoba:", count)