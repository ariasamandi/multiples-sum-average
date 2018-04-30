# randomly generates 5,000 coin tosses attempts and displays attemps/how many heads and tails were landed
import random
random_num = random.randint(1, 2)
def coin_tosses():
    print "strating the program..."
    heads = 0
    tails = 0
    for i in range(1, 5001):
        random_num = random.randint(1, 2)
        if random_num == 1:
            attempt = "heads"
            heads += 1
            print "attempt #", i, "Throwing a coin... It's", attempt, "... Got", heads, "head(s) so far and", tails, "tail(s) so far"
        else:
            attempt = "tails"
            tails += 1
            print "attempt #", i, "Throwing a coin... It's", attempt, "... Got", heads, "head(s) so far and", tails, "tail(s) so far"
    print "Ending the program, thank you!"
coin_tosses()