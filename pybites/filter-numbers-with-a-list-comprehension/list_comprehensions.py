NUMBERS = [1, 2, -3, 4, 5,-6, 7, 8, 9, 10] 
def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    result_list = [x for x in numbers if x > 0 and x % 2 == 0]
    return result_list

print(filter_positive_even_numbers(NUMBERS))
