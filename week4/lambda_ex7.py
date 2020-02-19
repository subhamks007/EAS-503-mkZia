

# lambda_ex7.py
# Create a dictionary where the key is year and value is True/False if the year is a leap year

years = range(1970, 2000)

def is_leap_year(year):
    # does not work for century year
    if year % 4 == 0:
        return True
    else:
        return False

my_dict = {}
leap_years = []
for year in years:
    my_dict.update({year: is_leap_year(year)})
    if is_leap_year(year):
        leap_years.append(year)

import pprint
pprint.pprint(my_dict)
print(leap_years)