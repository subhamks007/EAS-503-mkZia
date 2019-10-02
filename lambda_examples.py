def square(num):
	return num * num


square2 = lambda num: num * num
# lambda a function without a name; 
# anonymous functions; 
# one line only; 
# single expression only 
# stored in a variable
# When do you use it? Pass a function into another function as a parameter
# lambda variables (comma separated): expression
add = lambda a,b: a + b

print(square(9))

print(square2(9))

print(add(3,10))


func = lambda a, b: a * b
def lambda_test(func, number1, number2):
	return func(number1, number2)


print(lambda_test(func, 3, 4))

# lambda functions are used with other functions. Usually with map, filter, sort

my_list = [2, 3, 4]

# double this list


# method 1 - define a square function

def square_list(my_list):
	new_list = []
	for ele in my_list:
		new_list.append(ele * ele)

	return new_list

print(square_list(my_list))

# method 2 - list comprehension

print([ele*ele for ele in my_list])

# method 3 - use lambda with map
# map(lambda variables (comma separated): expression)

print(map(lambda ele: ele*ele, my_list))

# map objects are a generator. How many times can you iterate over them?



students = ['john', 'jane', 'doe']

# make upper case


# method 1 create new list and loop
new_list = []
for student in students:
    tmp = student
    new_list.append(student.title())

print(new_list)

# method 2 -- use list comprehension

print([student[0].upper()+student[1:] for student in students])

# method 3 -- use lambda 

print(map(lambda student: student.title(), students))


# covert each value to float

my_dict = [{'value': '34.4'}, {'value': '45.3'}, {'value': '73.4'}]

print(map(lambda ele: {'value': float(ele['value'])}, my_dict))


# Filter -- basically, combining conditional and lambda. Will return all values
# that have a Truth value 
# filter(lambda variables (comma seperated): expression (that will evaluate to True or False/None), list))


years = range(1970, 2000)

def is_leap_year(year):
	if year % 4 == 0:
		return True
	else:
		return False

my_dict = {}
leap_years = []
for ele in years:
	my_dict.update({ele: is_leap_year(ele)})
	if is_leap_year(ele):
		leap_years.append(ele)

import pprint
pprint.pprint(my_dict)
print(leap_years)


print(list(filter(lambda year: year % 4 == 0, range(1970, 2000))))


# combining map with filter

print(list(map(lambda year: f'{year} is a leap year!', filter(lambda year: year % 4 == 0, range(1970, 2000)) )))


# list comprehension

print()
print([f'{year} is a leap year' for year in range(1970, 2000) if year % 4 == 0])




# any and all

print(any((True, True, False)))
print(any((True, True, True)))
print(all((True, True, True)))
print(all((True, True, False)))

x = (('efg', 1), ('abc', 3), ('hij', 2))

#print(sorted(x)) # will not work

print(sorted(x, key=lambda ele: ele[1]))


students = [
	{'username': 'john', 'grade': 50},
	{'username': 'jane', 'grade': 80},
	{'username': 'doe', 'grade': 35}
]

print(sorted(students, key=lambda student: student['username']))
print(sorted(students, key=lambda student: student['username'], reverse=True))
print(sorted(students, key=lambda student: student['grade']))
print(sorted(students, key=lambda student: student['grade'], reverse=True))



students = ['john', 'Janette', 'doe']

print(min(students))

students = ['john', 'Janette', 'Doe']
print(min(students))


print(min(students, key=lambda student: len(student)))

print(max(students, key=lambda student: len(student)))


my_dict = [{'value': '34.4'}, {'value': '45.3'}, {'value': '73.4'}]


print(max(my_dict, key=lambda ele: float(ele['value'])))

