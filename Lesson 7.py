def t1():
    numbers = [5, 12, 63 , 147, 2300002]
    for tilbo in range(len(numbers)):
        print(f"{numbers[tilbo]} = {tilbo}")

    new_numbers = input("Which number would you like to add? ")
    numbers.append(new_numbers)
    print("Updated List:")
    for tilbo in range(len(numbers)):
        print(f"{numbers[tilbo]} = {tilbo}")

t1()