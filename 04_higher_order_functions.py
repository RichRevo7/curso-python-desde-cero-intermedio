### highr order functions ###

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_one(5, 2, sum_one))
print(sum_two_values_and_one(5, 2, sum_five))

### closures ###

def sum_ten(origunal_value):
    def add(value):
        return value + 10 + origunal_value
    return add
    
add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# map

def multiply_by_two(number):
    return number * 2

print(list(map(multiply_by_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False
    # return number > 10 - Este funciona con lambda.

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))