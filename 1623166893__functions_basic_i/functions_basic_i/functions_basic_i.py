#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#output 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#Not defined because number of days in a week has no arguments

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#returns 4 because it is the first return


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#returns 5 because it terminates function


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#prints out 5 because x is not returned


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#output is 3, 5


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#returns 2 and 5 so 25 becomes the string


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#error because else isn't used in python


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#7, 14, 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#500, 300, 500, 300, 500


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#500 500 300 300

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#500 300 500 300 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#500 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#1, 2, 3


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#1, 10, 3