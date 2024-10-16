def leap_year(year):
    if not (1900 <= year <= 10**5):
        return "The year must be between 1900 and 100000."
    
    if year % 4 == 0:
        return True    
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True
    else:
        return False
    pass
print(leap_year(2012))