outfile = open(r"word2_outfile.txt")
with open("jatin@iitg.ernet.in_mail.txt") as file:
    email = ""
    sender_name=[]
    email_index = -1
    type = -1
    new_position = []
    member_name= []
    paper_name=[]
    volume = []
    volume_number = 0
    issue_number = 0
    issue_name = []
    page=[]
    month = "month"
    year = "year"
    content = file.readlines()
    for line in content:
        words = line.split()
        start_counter = 0
        end_counter = 0
        for word in words:
            #print(word)
            if "<" in word and ">" in word and ("@iitg" in word or "@gmail" in word or "@yahoo" in word):
                email = word
                email_index = words.index(email)
                for int in range(0,email_index):
                    sender_name.append(words[int])
            if "To" in word:
                print("word found as", word)
                found = word
                found_index = words.index(word)
                member_name.append(words[found_index + 2])
                member_name.append(words[found_index + 3])
            if "promot" in word:#promoting, promoted for both of these
                #print("found promote")
                type = 1
            if type == 1:
                #print(word)
                if "assistant" in word or "Assistant" in word or "Associate" in word or "associate" in word:
                    new_position.append(word)
                if "professor" in word or "Professor" in word:
                   new_position.append(word)
                if "HOD" in word or "hod" in word or "Head of Department" in word or "Head" in word or "head" in word or "Head" in word or "HoD" in word or "hOd" in word:
                    new_position.append(word)
                if "Dean" in word or "dean" in word:
                    new_position.append(word)
                if "Director" in word or "director" in word:
                    new_position.append(word)
                if "To" in word:
                    print("inside to search")
                    index = words.index(word)
                    print(words[index])
                    member_name.append(words[index + 1])
                    member_name.append(words[index + 2])
            if "accept" in word:
                start_counter = words.index(word)
                print("start counter found as: ",words[start_counter])
                type = 2
                print("type found of :",type)
            if type == 2 and (word == "by" or word == "in") and words.index(word) == start_counter + 1:
                    start_counter = words.index(word)
                    print("index found is :",words[start_counter])
            if type == 2 and start_counter > 0 and "." in word:
                print("inside here")
                end_counter = words.index(word)
                for i in range(start_counter+1,end_counter+1):
                    paper_name.append(words[i])
            if type == 2:
                if "volum" in word or "Volum" in word:
                    volume_number = words[words.index(word)+1]
            if type == 2 and word == "issue" or word == "Issue":
                word_temp1 = word
                issue_number = words.index(word_temp1)+1
                issue_name.append(words[issue_number])
            if "page" in word or "Page" in word:
                index = words.index(word)+1
                page.append(words[index])
            if "publish" in word:
                index = words.index(word)+2
                month = words[index]
                index = index + 1
                year = words[index]
    print(sender_name)
    print(member_name)#prints them as a list without any problem
    #outfile.write(*sender_name)
    # print("email is :",word)
    print("type is:",type)
    if type == 1:
        print (" ".join(member_name),"has been promoted by"," ".join(sender_name))
        print ("Their new position is"," ".join(new_position))
        print (email)
    if type == 2:
        print(paper_name)
        print(volume_number)
        print(issue_name)
        print(issue_number)#not really of much difference
        print(page)
        print(month)
        print(year)