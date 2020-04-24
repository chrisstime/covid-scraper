def calculate_percentage(numerator, denominator):
    percentage = (_to_int(numerator)/_to_int(denominator)) * 100
    
    return '{0:.2f}%'.format(percentage)

def _to_int(number):
    n = number.replace(',', '')

    return int(n)