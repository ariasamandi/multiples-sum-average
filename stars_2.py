# part 1 
# takes in a list and produces an amount of stars depending on the value.
#part 2 
# modify function to print the first letter for how many letters there are in a string.
x = [4, 6, 1, "aria", "samandi", 7, 25]
def stars(arr):
    for i in range(0, len(arr)):
        if isinstance(arr[i], str):
            string = arr[i]
            for i in range(0, len(string)):
                char = string[0]
            print char * len(string)
        else:
            print "*" * arr[i]
stars(x)
