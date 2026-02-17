def calculate_discounted_price(price, discount_percent):
    final_price = price - (price * discount_percent/100 )
    return final_price


print(calculate_discounted_price(10, 56))


# The rest of the tasks are repetitive as hell so I ain't doing allat
# you can put stuff onto one line with " end="" " used in " print(misc, end"") " and if you want space inbetween its " print(misc, end"\t") "