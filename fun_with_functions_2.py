# prints numbers 1-2,000 and if its odd or even
def odd_even():
    for i in range(1, 2001):
        if i % 2 == 1:
            print "Number is", i,". This is an odd number"
        else:
            print "Number is",i,". This is an even number"
odd_even()
#Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
#The function should multiply each value in the list by the second argument.
a = [2,4,10,16]
def multiply(my_list, number):
    for i in range(0, len(a)):
        a[i] = a[i] * number
    print a
    return a
multiply(a, 1)
# hacker challange
#Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as 
# a two-dimensional list. Each internal list should contain the 1's times the number in the original list. Here's an example:
def layered_multiples(arr):
    new_array = []
    for i in range(0, len(arr)):
        new_array.append("1" * arr[i])
    return new_array
x = layered_multiples(multiply([2,4,5], 3))
print x