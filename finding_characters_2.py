def finding_characters(word_list, char):
    new_list = []
    for i in range(0, len(word_list)):
        string = word_list[i]
        for j in range(0, len(string)):
            if char == string[j]:
                new_list.append(string)
            else:
                continue
    print new_list
finding_characters(['hello','world','my','name','is','Anna'], "o")