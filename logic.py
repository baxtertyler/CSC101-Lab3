# Name: Tyler Baxter
# Section: 03

# This function returns True if the parameter is odd, and False otherwise
# int -> bool
def is_odd(num):
    return num % 2 == 1


# This function returns True if the parameter is within a specified interval, and False otherwise
# int -> bool
def in_an_interval(num):
    return (-10 <= num < -4) or (-2 <= num <= 8) or (27 < num < 52) or (10 < num <= 22) or (110 <= num <= 237)


# This function returns True if the parameters are in the intervals and divisible within each other, and False otherwise
# int, int -> bool
def is_divisible_in_interval(num1, num2):
    return (75 <= num1 <= 140) and (30 < num2 <= 200) and (num1 % num2 == 0)

