#For asessments:
#40-49% screenshots of you testing the code
# 50-59% Comments in the code saying what it does
# 60-69% Justification
# 70% Provide an alternative approach
def ass1():
    def delivery_fee(distance,order_value):
        print("How far away are you?")
        distance = int(input())
        print(f"You are {distance} miles away")
        match distance, order_value:
            case (distance, _) if distance <= 10:
                order_value = 0
            case (distance, _) if distance > 10 and distance <= 20:
                order_value = 10
            case (distance, _) if distance > 20 and distance <= 30:
                order_value = 15
            case (distance, _) if distance > 30:
                order_value = 20
        print (f"The delivery fee is £{order_value}")
        return order_value

    print ("How much was the product cost?")
    cost = int(input())
    print(f"You paid £{cost}.")
    print(f"The total cost is £{cost + delivery_fee(distance = 0, order_value = 0)}")

def task1():
    ast = 1
    while ast < 3 :
        ast = ast + 1
    print("*" * ast)

def task2():
    def loopsub(number):
        for i in range (1,4):
            answer = "*"
            print(answer, end="\t")

    def loopmain():
        for row in range (1,4):
            loopsub(row)
            print()

    loopmain()

def task3():


    def loopmain():
        num = int(input("Please input the rows: ")) + 1
        num2 = int(input("Please input the columns: ")) + 1
        for row in range (1,num):
            for i in range(1, num2):
                answer = "*"
                print(answer, end="\t")
            print()

    loopmain()

def task4():
    # stair = 1
    # while stair < 5 :
    #     print("*" * stair)
    #     stair = stair + 1
    # for stair in range(1,5):
    #     print("*" * stair)
    #     stair = stair + 1
    for stair in range(1,5):
        for i in range(1, stair):
            answer = "*"
            print(answer, end="")
        print()
    #I DID IT HOLY SHIT

def task5():
    row = int(input("Please input the rows: "))
    for stair in range(1, row + 1):
        for i in range(stair):
            answer = "*"
            print(answer, end=" ")
        print()

def task6():
    # for i in range(1,4):
    #     print("*" * i + " " + "*" * (4 - i))

    # for row in range(1, 4):
    #     for col in range(row):
    #         print("*", end="")
    #     print(" ", end="")
    #     for col in range(4 - row):
    #         print("*", end="")
    #     print()

    # the right way
    for row in range(1,4):
        for column in range(1,6):
            if column == row +1:
                print(" ",end="")
            else:
                print("*", end="")
        print()

task6()
