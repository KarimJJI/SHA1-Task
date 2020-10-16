import hashlib
import os
from colorama import Fore

def my24sha():

    """Finds hash collisions of the first 24 bits for a given wordlist"""

    txt_file = open("rockyou-65.txt", "r", encoding = 'latin-1')
    words = txt_file.read()
    words_lst = words.split("\n")
    txt_file.close()

    newlst = []
    dupItems = []
    uniqItems = {}

    hashed = open("MY24SHA.txt", "w")

    for i in words_lst:
        hash_object = hashlib.sha1((bytes(i, encoding = 'utf-8')))
        hex_dig = hash_object.hexdigest()
        newlst.append(str(hex_dig)[: 6])
        hashed.write(Fore.WHITE + i + Fore.RED + "[" + str(hex_dig)[: 6] + "]\n")
    hashed.close()

    for i in newlst:
        if i not in uniqItems:
            uniqItems[i] = 1
        else :
            if uniqItems[i] == 1:
                dupItems.append(i)
                uniqItems[i] += 1

    print("\n24-BIT HASH COLLISIONS:\n")

    for i in dupItems:
        if i == "da39a3":
            dupItems.remove(i)
        else :
            os.system('grep ' + i + ' MY24SHA.txt')

def my60sha():

    """Finds hash collisions of the first 24 bits for a given wordlist"""

    txt_file = open("rockyou.txt", "r", encoding = 'latin-1')
    words = txt_file.read()
    words_lst = words.split("\n")
    txt_file.close()

    newlst = []
    dupItems = []
    uniqItems = {}

    hashed = open("MY60SHA.txt", "w")

    for i in words_lst:
        hash_object = hashlib.sha1((bytes(i, encoding = 'utf-8')))
        hex_dig = hash_object.hexdigest()
        newlst.append(str(hex_dig)[: 12])
        hashed.write(Fore.WHITE + i + Fore.RED + "[" + str(hex_dig)[: 12] + "]\n")
    hashed.close()

    for i in newlst:
        if i not in uniqItems:
            uniqItems[i] = 1
        else :
            if uniqItems[i] == 1:
                dupItems.append(i)
                uniqItems[i] += 1
    
    print("\n60-BIT HASH COLLISIONS:\n")

    for i in dupItems:
        if i == "da39a3ee5e6b4b0":
            dupItems.remove(i)
        else :
            os.system('grep ' + i + ' MY60SHA.txt')

def menu(choice):
    
    if choice == "1":
        my24sha()
    elif choice == "2":
        print("\nWorking... This may take a moment.")
        my60sha()
    elif choice == "q" or choice == "Q":
        quit()
    else:
        menu(input("\n(1) - MY24SHA\n(2) - MY60SHA\n(Q) - QUIT\n"))

print("\n24-BIT & 60-BIT HASH COLLISION FUNCTIONS\n")
menu(input("(1) - MY24SHA\n(2) - MY60SHA\n(Q) - QUIT\n\n[ENTER AN OPTION]: "))




