def type_list(my_list):
    string = ""
    sum = 0
    for i in range(0, len(my_list)):
        if isinstance(my_list[i], str):
            string += my_list[i] 
        elif isinstance(my_list[i], int):
            sum += my_list[i]
        elif isinstance(my_list[i], float):
            sum += my_list[i]
    if string != "" and sum != 0:
        print "The list you entered is of mixed type"
        print "String: " + string
        print "Sum:", sum
    elif string != "":
        print "The list you entered consist of string type"
        print "String: " + string
    elif sum != 0:
        print "The list you entered consist of integer type"
        print "Sum:", sum

   
    
type_list(["hello", "my", "name", 12.4, 10, "Is", "aria"])