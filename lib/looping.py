#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")
    

    # code goes here!
    pass

def square_integers(int_list):
    sqrnum = [num **2 for num in int_list]
    return(sqrnum)
    # code goes here!
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
    pass
