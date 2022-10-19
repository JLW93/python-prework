# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of the code has been defined as below.

def hello_name(user_name):
    print(f'hello_{user_name}!')

hello_name('USERNAME')

# Question 2
# Write a Python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    odd_numbers = []
    for number in range(1,101):
        if number % 2 == 1:
            odd_numbers.append(number)
        else:
            continue
    

print(first_odds())

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    largest_number = 0
    for number in a_list:
        if number > largest_number:
            largest_number = number
        else:
            continue
    return largest_number

numbers = [14, 55, 6, 10, 67, 32, 101, 137, 50, 3, 89]

print(max_num_in_list(numbers))

#---OR---#

def max_num_in_list_2(a_list):
    return max(a_list)

numbers = [14, 55, 6, 10, 67, 113, 32, 101, 50, 3, 89]

print(max_num_in_list_2(numbers))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not
# divisible by 100, unless it is also divisible by 400.
# The return should be a boolean type (true/false)

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 400 == 0:
            return True
        elif a_year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

print(is_leap_year(2045))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# for example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not
# consecutive numbers. The return should be boolean type.

def is_consecutive(a_list):
    if max(a_list) - min(a_list) == len(a_list) - 1:
        return True
    else:
        return False

numbers_1 = [1, 2, 3, 4, 5, 6, 7]
numbers_2 = [1, 3, 2, 5, 4, 7, 6]
numbers_3 = [1, 3, 5, 7, 9]

print(is_consecutive(numbers_3))
