# Multiples Part 1
# This function prints all the odd numbers from 1 to 1000. 
def multiples1():
    for i in range(1, 1001):
        if i % 2 == 1:
           print (i)
multiples1()
# Multiples Part 2
# This function prints all the multiples of 5 from 5 to 1,000,000. 
def multiples_2():
    for i in range(5, 1000001):
        if i % 5 == 0:
            print i
multiples_2()
# Sum List
# This function prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
def sum_list():
    a = [1, 2, 5, 10, 255, 3]
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    print sum
sum_list()
# Average List
# this function prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
def average_list():
    a = [1, 2, 5, 10, 255, 3]
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    average = sum/(len(a))
    print average
average_list()