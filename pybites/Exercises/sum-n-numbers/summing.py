NUMBERS = [1, 2, 3, 4, 5]

def sum_numbers(numbers=None):
    if numbers is None:
        return sum(range(1,101))
    else:
        return sum(numbers) if numbers else 0


print(sum_numbers(NUMBERS))
print(sum_numbers())
