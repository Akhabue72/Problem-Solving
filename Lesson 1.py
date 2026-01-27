#20/01/2026


# print ("My name is Abu")

# print("_______")
# print("| o o |")
# print("|-----| < Hello!")
# print("-------")

# age = 19
# print(f"I am {age} years old")

# first_number = 8
# second_number = 7
# print(f"{first_number} + {second_number} = {first_number + second_number}")

# price = 5.96
# quantity = 6
# total_price = price * quantity
# print(f"You bought {quantity} things for £{price}. That costs: £{total_price}")

# yob = 2006
# cy = 2026
# print(f"You were born in {yob}, it's now {cy} - That means you'll turn {cy - yob} this year!")

# name = input("What is your name? ")
# Height = int(input("How tall are you? (cm) "))
# print(f"Hi {name}. You are {Height}cm tall")

seconds = int(input("Enter seconds: "))
minutes = seconds // 60
secs = seconds % 60

if minutes >= 60:
    hours = minutes // 60
    mins = minutes % 60
    print(f"That is {hours} hours, {mins} minutes and {secs} seconds.")
else:
    print(f"That is {minutes} minutes and {secs} seconds.")

#23/01/26
