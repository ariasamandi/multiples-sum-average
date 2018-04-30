def comparing_lists(list_one, list_two):
    for i in range(0, len(list_one)):
        for i in range(0, len(list_two)):
            if len(list_one) > len(list_two) or len(list_two) > len(list_one):
                compare = False
            else:
                if list_one[i] == list_two[i]:
                    compare = True
                else: compare = False
    if compare == True:
        print "They are the same"
    else:
        print "They are not the same"
comparing_lists(['celery','carrots','bread','milk'], ['celery','carrots','bread','milk'])
    