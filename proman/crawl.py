from .models import UserProfile, Deg, Publication
from django.contrib.auth.models import User
import re
def promoter(user):
    userprofile = user.userprofile
    pub = Publication.objects.create()
    my_str = user.username + '_' + 'mail.txt'
    with open(my_str) as file:
        content = file.readlines()
        chk1 = 0
        chk2 = 0
        index = 0
        new_position = ""
        for line in content:
            words = line.split()
            for word in words:
                if "promot" in word:
                    chk1 = 1
                if chk1 == 1:
                    if "assistant" in word or "Assistant" in word or "Associate" in word or "associate" in word:
                        new_position += word
                        new_position += " "
                    if "professor" in word or "Professor" in word:
                        new_position += word
                    if "HOD" in word or "hod" in word or "Head of Department" in word or "Head" in word or "head" in word or "Head" in word or "HoD" in word or "hOd" in word:
                        new_position += word
                    if "Dean" in word or "dean" in word:
                        new_position += word
                    if "Director" in word or "director" in word:
                        new_position += word

                # if "publication" in word or "Publication" in word:
                #     chk2 = 2
                #     continue
                # if chk2 == 2:
                #     if "accept" in word:
                #         chk2 = 3
                #         continue
                # if chk2 == 3:
                #     if ':' is word:
                #         chk2 = 4
                #         continue
                # if chk2 == 4:
                #     publi=""
                #     # new_position += re.findall(r'"([^"]*)"', words)
                #     index = word.index(word)
                #     while word[index] is not "":
                #         publi += word + " "
                #     pub.descrip = publi.split(':')[1]
                #     pub.user = userprofile
                #     pub.save()
                #     return userprofile
    print(new_position)
    userprofile.desig = new_position
    userprofile.save()
    return userprofile

# promoter()