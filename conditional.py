# Name: Tyler Baxter
# Section: 03

# This function returns the smaller value of the two
# int, int -> int
def min_of_2(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2


# This function returns the smaller value of the three, using min_of_2
# int, int, int -> int
def min_of_3(num1, num2, num3):
    return min_of_2(num1, min_of_2(num2, num3))


# This function returns the rental fee, based on the days late an item is returned
# int -> int
def rental_late_fee(days):
    if days <= 2:
        return 0
    elif days <= 5:
        return 10
    elif days <= 12:
        return 15
    elif days <= 22:
        return 30
    else:
        return 100
