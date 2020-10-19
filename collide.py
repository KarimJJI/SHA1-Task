import hashlib
import os
#from colorama import Fore

def my24sha():

    """Finds hash collisions of the first 24 bits for a given wordlist"""

    txt_file = open("rockyou-65.txt", "r", encoding = 'latin-1')
    words = txt_file.read()
    word_lst = words.split("\n")
    txt_file.close()

    hash_lst = []
    unique = {}
    match = []

    word_hash = open("MY24SHA.txt", "w")

    for i in word_lst:
        hash_object = hashlib.sha1((bytes(i, encoding = 'utf-8')))
        hex_dig = hash_object.hexdigest()
        hash_lst.append(str(hex_dig)[: 6])
        word_hash.write(i +" [" + str(hex_dig)[: 6] + "]\n")
    word_hash.close()

    for i in hash_lst:
        if i not in unique:
            unique[i] = 1
        else :
            if unique[i] == 1:
                match.append(i)
                unique[i] += 1

    print("\n24-BIT HASH COLLISIONS:\n")

    for i in match:
        if i == "da39a3":
            match.remove(i)
        else :
            os.system('grep ' + i + ' MY24SHA.txt')
    os.system('rm MY24SHA.txt')

def my60sha():

    """Finds hash collisions of the first 60 bits for a given wordlist"""

    txt_file = open("rockyou-65.txt", "r", encoding = 'latin-1')
    words = txt_file.read()
    word_lst = words.split("\n")
    txt_file.close()

    hash_lst = []
    unique = {}
    match = []

    word_hash = open("MY60SHA.txt", "w")

    for i in word_lst:
        hash_object = hashlib.sha1((bytes(i, encoding = 'utf-8')))
        hex_dig = hash_object.hexdigest()
        hash_lst.append(str(hex_dig)[: 15])
        word_hash.write(i +" [" + str(hex_dig)[: 15] + "]\n")
    word_hash.close()

    for i in hash_lst:
        if i not in unique:
            unique[i] = 1
        else :
            if unique[i] == 1:
                match.append(i)
                unique[i] += 1

    print("\n60-BIT HASH COLLISIONS:\n")

    for i in match:
        if i == "da39a3ee5e6b":
            match.remove(i)
        else :
            os.system('grep ' + i + ' MY60SHA.txt')
    os.system('rm MY60SHA.txt')

def menu(choice):
    
    if choice == "1":
        my24sha()
    elif choice == "2":
        my60sha()
    elif choice == "q" or choice == "Q":
        quit()
    else:
        menu(input("\n(1) - MY24SHA\n(2) - MY60SHA\n(Q) - QUIT\n"))

print("\n24-BIT & 60-BIT HASH COLLISION FUNCTIONS\n")
menu(input("(1) - MY24SHA\n(2) - MY60SHA\n(Q) - QUIT\n\n[ENTER AN OPTION]: "))




