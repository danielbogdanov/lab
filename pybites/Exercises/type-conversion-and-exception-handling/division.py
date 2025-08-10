def divide_numbers(numerator, denominator):
    """
    For this exercise you can assume numerator and denominator are of type int/str/float.
    Try to convert numerator and denominator to int types, if that raises a
    ValueError reraise it with the message "Can only divide two numbers".
    Following do the division and return the result.
    However if denominator is 0 catch the corresponding Python exception that
    is thrown and return 0.                                                                                                                                                                                                                
    """
    quotient = 0
    try:
        quotient = int(numerator) / int(denominator)
    except ZeroDivisionError:
        return 0
    except ValueError:
        raise ValueError('Can only divide two numbers')
    except TypeError:
        raise  TypeError
    return quotient
# ZeroDivisionError: division by zero
# TypeError: divide_numbers() takes 2 positional arguments but 3 were given
# ValueError: invalid literal for int() with base 10: 's'
