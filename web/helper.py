def calculate_percentage(numerator, denominator):
    return (__to_int(numerator)/__to_int(denominator)) * 100

def __to_int(number):
    n = number.replace(',', '')

    return int(n)