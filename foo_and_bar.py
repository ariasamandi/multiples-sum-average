#For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square.
# If it is a prime number, print "Foo". If it is a perfect square, print "Bar". If it is neither, print "FooBar". 
def foo_and_bar():
    for i in range(100, 200):
        for j in range(2, 100):
            if j * j == i:
                print i, "Bar"
            if i % j != 0:
                prime_number = "Foo"
            else:
                prime_number = "FooBar"
                break
        print i, prime_number
    
foo_and_bar()