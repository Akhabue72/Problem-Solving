#1
def cost1(cost):
    cost = 0
    while cost < 20:
        cost += 1
        print (cost)
    return cost
def cost2(cost):
    cost = 4
    while cost < 15:
        cost += 1
        print (cost)
    return cost
def cost3(cost):
    cost = -1
    while cost < 21:
        cost += 2
        print (cost)
    return cost
def cost4(cost):
    cost = 11
    while cost > 1:
        cost -= 1
        print (cost)
    return cost
# cost1(cost = 1)
# cost2(cost = 2)
# cost3(cost = 3)
# cost4(cost = 4)
#2
def timestable(multiple, answer):
    print("Which timestable would you like to see?")
    answer = int(input())
    multiple = 0
    while multiple < 10:
        multiple += 1
        print(f"{multiple} x {answer} = {multiple * answer}")
    return multiple
# timestable(multiple = 1, answer = 1)
#3
