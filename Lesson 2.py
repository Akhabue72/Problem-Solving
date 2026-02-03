 # 1,2,3
def one_two_three():
    agE = int(input("What is your age? "))
    if agE <= 0:
         print("wow, people start using computers early")
    if agE == 19:
         print("Hey! We're the same age!")
    day = int(input("What day is it? "))
    month = int(input("What month is it? "))
    if (day == 1 ) and (month == 4):
         print("It's April fools day")

# 4
def four():
    age = int(input("What is your age? "))
    if age >= 18:
        print(f"You are old enough to buy alcohol")
    else:
        print(f"You are too young to buy alcohol")


#5,6
def five_six():
    age = int(input("What is your age? "))
    speed = int(input("How fast are you going?"))
    speedLimit = 50
    cap = speed - speedLimit
    if cap <= 10 and speed >= speedLimit:
        print(f"You are {cap} over the speed limit. Slow down")
    elif cap >10:
        print(f"You're speeding! Ticket for you")
    else:
        print("Please continue to drive safely")

# 7
def seven():
    day = int(input("What day is it? "))
    month = int(input("What month is it? "))

    match day , month:
        case s if day == 1 & month == 4:
            print("It's april fools day")
        case s if day == 1 & month == 1:
            print("It's New Year Day")
        case s if day == 18 & month == 2:
            print("Its My birthday!")
        case s if day == 1 & month == 4:
            print("It's Star Wars Day")
        case _:
            print("Mid day icl")

# 8
def eight():
    age = int(input("What is your age? "))
    price = float(4)

    if age <= 4:
         print(f"You pay nothing!")
    elif age <= 16 and age > 4:
        teen_price = price // 2
        print (f"You pay £{teen_price}")
    elif age >= 65:
        olie_price = price * 2/3
        print (f"You pay £{olie_price}")
    else:
        print (f"You pay £{price}")



