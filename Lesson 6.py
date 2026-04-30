numbers = []

print("=" * 50)
print("NUMBER LIST MANAGER".center(50))
print("=" * 50)

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
            num = int(input(f"Enter number {i + 1}: ")) #Struggled for a while before I added this
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

    else:
        print("Invalid! Please enter A, B, C, or D.")
        continue

    # Ask to continue
    again = input("Keep going? (yes/no): ").lower()
    if again != "yes" and again != "y":
        print("Goodbye!")
        break