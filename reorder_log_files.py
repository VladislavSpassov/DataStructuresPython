def reorderLogFiles(logs: [str]) ->[str]:


    result = []
    words = []
    digits = []
    for log in logs:
        current = log.split(' ')

        if current[1].isdigit() :
            digits.append(current)
        else:
            words.append(current)

    
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            print(i,j)
            if words[i][1] > words[j][1]:
                words[i], words[j] = words[j],words[i]
                continue
            if words[i][1] == words[j][1]:
                counter = 2

                while words[i][counter] == words[j][counter] and counter + 1 < min(len(words[i]),len(words[j])):

                    counter += 1
                
                if words[i][counter] > words[j][counter]:
                    words[i], words[j] = words[j],words[i]

                # if len(words[i]) == len(words[j]) == counter + 1:
                #     if words [i][0] > words[j][0]:
                #         words[i], words[j] = words[j],words[i]
        print(words)
    result_words = []

    for x in words:
        result_words.append(' '.join([str(elem) for elem in x]))
    
    for x in digits:
        result_words.append(' '.join([str(elem) for elem in x]))
    
    print(result_words)
    return result_words

#reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])