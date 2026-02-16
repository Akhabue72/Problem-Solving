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

