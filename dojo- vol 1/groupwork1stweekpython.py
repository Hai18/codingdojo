#1st task group work 7/6/17

def multi (num, factor):
    for idx in range(len(num)):
        num[idx] *= factor
    return num

myvar = multi ([10,20,30],50)
print myvar


#2nd task group work 7/6/17

def print_dict (my_dict):
    for idx in my_dict:
            print idx, ":", my_dict[idx]
print_dict ({'name': 'Gabriela', 'age': '21', 'state':'TX'})


#3rd taske group work 7/6/17

def fizzbuzz (myval):
    if(myval % 3 == 0 and myval % 5 is 0):
        print "Fizzbuzz"
    elif (myval % 3 is 0):
        print "Fizz"

    elif (myval % 5 is 0):
        print "Buzz"

fizzbuzz (30)
