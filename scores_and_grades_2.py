#randomly generates 10 scores and displays the grade given according to score
import random
def scores_and_grades(): 
    print "Scores and Grades"
    for i in range(0, 10):
        random_num = random.randint(60, 100)
        if random_num > 90:
            print "Score:", random_num, "Your grade is A"
        elif random_num > 80:
            print "Score:", random_num, "Your grade is B"
        elif random_num > 70:
            print "Score:", random_num, "Your grade is C"
        else:
            print "Score:", random_num, "Your grade is D"
    print "End of the program. Bye!"
scores_and_grades()