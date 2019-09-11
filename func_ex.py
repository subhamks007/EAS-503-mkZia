print('Happy birthday to you!')
print('Happy birthday to you!')
print('Happy birthday, dear John')
print('Happy birthday to you!')
print('Happy birthday to you!')



print('Happy birthday to you!')
print('Happy birthday to you!')
print('Happy birthday, dear Jane')
print('Happy birthday to you!')
print('Happy birthday to you!')


def print_happy_birthday():
    print('Happy birthday to you!')
    print('Happy birthday to you!')


print('-'*40)


print_happy_birthday()
print('Happy birthday, dear John')
print_happy_birthday()

print_happy_birthday()
print('Happy birthday, dear Jane')
print_happy_birthday()

def print_happy_birthday_name(name):
    print(f'Happy birthday, dear {name}')


print('-'*40)

print_happy_birthday()
print_happy_birthday_name('John')
print_happy_birthday()

print_happy_birthday()
print_happy_birthday_name('Jane')
print_happy_birthday()


def print_happy_birthday2(count):
    for i in range(count):
        print('Happy birthday to you!')



print('-'*40)

print_happy_birthday2(2)
print_happy_birthday_name('John')
print_happy_birthday2(3)

def print_happy_birthday3(count=4):
    for i in range(count):
        print('Happy birthday to you!')



print('-'*40)

print_happy_birthday3(2)
print_happy_birthday_name('John')
print_happy_birthday3()


def happy_birthday(name, count=2):
    print_happy_birthday3(count)
    print_happy_birthday_name(name)
    print_happy_birthday3(count)

print('-'*40)
happy_birthday('John', 6)
happy_birthday('Jane', 6)



def squares(n):

    square_list = []
    for i in range(1, n+1):
        square_list.append(i*i)

    return square_list

def square2(n):

    return [i*i for i in range(1, n+1)]

print(squares(10))
print(square2(10))


def calculate_distance(x1,y1,x2,y2):
    import math
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return distance

print(calculate_distance(4, 6, 28, 13))

point1 = (4,6)
point2 = (28,13)

def calculate_distance2(point1, point2):
    import math
    distance = math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)
    return distance

print(calculate_distance2(point1, point2))


def modify_point(point):
    point[0] = 10
    point[1] = 20

    # return point

# print(modify_point(point1))

point_list = [4,6]
modify_point(point_list)
print(point_list)