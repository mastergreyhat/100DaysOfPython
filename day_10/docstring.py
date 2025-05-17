def is_leap_year(year):
    """This function accepts an integer value and returns 'True' if its a leap year and 
    'False' if its not a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Hover over the function 'is_leap_year' below to see the docstring.
# Docstrings are to be passed just after the function definition as """<DOCSTRING>"""     
leap_or_not = is_leap_year(int(input("Enter a year: ")))
print(leap_or_not)