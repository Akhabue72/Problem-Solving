# Example for nested statements (it's pretty cool)
def do_times_table(number):
    for i in range (1,13):
        answer = number * i
        print(answer, end="\t")

def times_table_grid():
    for row in range (1,13):
        do_times_table(row)
        print()

times_table_grid()

