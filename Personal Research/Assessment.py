#For assessments:
#40-49% screenshots of you testing the code
# 50-59% Comments in the code saying what it does
# 60-69% Justification
# 70% Provide an alternative approach
from Character import player
def idkwhattheseareicl():
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

def ass1():
    def delivery_fee(distance,order_value):

        #questions
        print("How far away are you?")
        distance = int(input())
        print(f"You are {distance} miles away")

        #distance calc
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
#main
    print ("How much was the product cost?")
    cost = int(input())
    print(f"You paid £{cost}.")
    print(f"The total cost is £{cost + delivery_fee(distance = 0, order_value = 0)}")

def ass2():
    #input
    answer = int(input("Please input a number between 1 and 20: "))
    result = ""
    #Calc
    for i in range(20):
        if i == answer - 1:
            result += "X"
        else:
            result += "-"
    print(result)

def ass3():
# Rectangle area calc
    def rectangle():
        length = float(input("Please enter the length of the rectangle: ")) #input 1
        width = float(input("Please enter the width of the rectangle: ")) #input 2
        area = length * width #calc
        print(f"The area of the rectangle is: {area} cm squared") #display
        return area

#Circle area calc
    def circle():
        import math
        radius = float(input("Enter the radius of the circle: ")) #input
        area = math.pi * radius ** 2 #calc
        print(f"The area of the circle is: {area:.2f} cm squared") #display
        return area

#Multi table
    def table():
        number = int(input("Enter a number to show its multiplication table: ")) #input
        print(f"Multiplication Table for {number}:")
        for i in range(1, 13):#calc
            result = number * i
            print(f"{number} x {i:2} = {result:3}")#display

#Mean calc
    def mean():
        print("Enter three numbers:")
        num1 = float(input("First number: "))#input
        num2 = float(input("Second number: "))#input
        num3 = float(input("Third number: "))#input
        mean = (num1 + num2 + num3) / 3 #calc
        print(f"The numbers are: {num1}, {num2}, {num3}")#display]
        print(f"The mean is: {mean:.2f}")#display

#Main menu
    def menu():
        while True:
            #The menu that the user sees
            print("""
            Please enter the letter which corresponds with your choice:
            a - Calculate the area of a rectangle
            b - Calculate the area of a circle
            c - Display a multiplication table
            d – Find the mean of three numbers """)
            answer = input("Please input the letter which corresponds with your choice: ").lower()

            #The different answers
            if answer == "a":
                rectangle()
            elif answer == "b":
                circle()
            elif answer == "c":
                table()
            elif answer == "d":
                mean()
            #Error check
            else:
                print("Input is invalid, please try again.")
                continue

    menu()

def ass4():
    # X coordinate
    x = int(input("Enter X coordinate between 1 and 10: "))

    # Y coordinate
    y = int(input("Enter Y coordinate between 1 and 10: "))

    # Display grid
    print("10x10 Grid:")
    for row in range(1, 11):
        for col in range(1, 11):
            if row == y and col == x:
                print("X", end=" ")
            else:
                print("-", end=" ")
        print()

def ass5():
    numbers = []

    print("=-" * 50)
    print("Number stuff".center(50))
    print("=-" * 50)

    # Main loop
    while True:
        # Menu
        print("Please enter your choice from the following menu:")
        print("A - Add numbers")
        print("B - Display all values")
        print("C - Replace one number")
        print("D - Calculate the mean")

        Answer = input("Enter your choice: ").lower()

        # A - Add numbers
        if Answer == "a":
            how_many = int(input("How many numbers do you want to add? "))
            for i in range(how_many):
                num = int(input(f"Enter number {i + 1}: "))  # Struggled for a while before I added this
                numbers.append(num)
            print(f"Added {how_many} number(s)!")

        # B - Display all values
        elif Answer == "b":
            if len(numbers) == 0:
                print("The list is empty. Maybe try adding some numbers.")
            else:
                print("All values in the list:")
                for i, value in enumerate(numbers):
                    print(f"  [{i}] = {value}")

        # C - Replace one number
        elif Answer == "c":
            if len(numbers) == 0:
                print("The list is empty. Nothing to replace.")
            else:
                print(f"List has positions 0 to {len(numbers) - 1}")
                position = int(input("Which position do you want to replace? "))
                if 0 <= position < len(numbers):
                    new_value = int(input("Enter the new number: "))
                    numbers[position] = new_value
                    print(f"Position {position} updated to {new_value}")
                else:
                    print(f"Invalid! Use 0 to {len(numbers) - 1}")

        # D - Calculate the mean
        elif Answer == "d":
            if len(numbers) == 0:
                print("Cannot calculate mean - list is empty!")
            else:
                mean = sum(numbers) / len(numbers)
                print(f"Mean (average) of all numbers: {mean:.2f}")
        # error check
        else:
            print("Invalid! Please enter A, B, C, or D.")
            continue

        # Ask to continue
        again = input("Keep going? (yes/no): ").lower()
        if again != "yes" and again != "y":
            print("Goodbye!")
            break
def ass6():
    #Quite frankly, this task really confuses me, but i'll get there
    # Array
    numbers = [6, 5, 3, 1, 2]
    # Loop
    for i in range(len(numbers)):
        current_value = numbers[i]
        first_value = numbers[0]
        print(f"Current element value: {current_value} | Element 0: {first_value}")

def ass7():
    p1 = player()
    p2 = player()
    print(f"Player 1 is {p1.name}")
    p1.describe()
    player.Heal(self=p1)
    p1.describe()
    p2.name = "Lucy"
    p2.health = 60
    p2.attack = 130
    p2.defence = 65
    print(f"Player 2 is {p2.name}")
    p2.describe()
    player.Damage(self=p2)
    p2.describe()
ass5()
