# password-creator
# Author: Brscn0

import random
while True:
    what_do_you_want_to_do = int(input("""
    ---------------------------
    1-)Create a password
    2-)List my password
    3-)Add password
    4-)Exit
    ---------------------------
    [*]Select: """))

    def listing():
        f = open("passwordlist.txt","r")
        list_read = f.read()
        print(list_read)
        f.close()
        

    def add():
        f = open("passwordlist.txt","a+")
        write = input("Plartform,Username,Password: ")
        f.write(write+"\n"+"\n")
        f.close()


    if what_do_you_want_to_do == 1:
        char_set = "qwertyuıopasdfghjklizxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789,+-*/?=/&%+^'!£#${[]}\.,:<>"

        vur = int(input("[*]Number of Characters: "))
        password = ""

        for i in range(vur):
            password_char = random.choice(char_set)
            password += password_char

        print("Your Password: ",password)
    if what_do_you_want_to_do == 2:
        listing()

    if what_do_you_want_to_do == 3:
        add()

    if what_do_you_want_to_do == 4:
        break