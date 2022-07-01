import math
from random import *
def format1(code,key,extra = True):
    code = code.lower()
    key = key.lower()
    code1 = ""
    if extra: 
        if len(code) < len(key):
            key = key[0:len(code)]
        elif len(code) > len(key):
            code = code[0:len(key)]
    for g in range(len(code)):
        if code[g] != " ":
            code1 = code1 + code[g]
    return code1,key
while True:
    print("Advanced Substitution cipher: Like a cipher wheel where a = the letter in the key. Then, each letter in the message is encrypted according to that setting.")
    print("Phrase cipher: Takes a phrase and takes first letters, or random amount of letters in each word. Also, it can change some of the letters to symbols.")
    print("Columnar cipher: Arranges the code by rows based on the length of the key and reads it by column.")
    print("Trifid cipher: Uses the key to create 3, 3x3 sqaures which turn each letter in the message into 3 numbers, the square number, the column number, and the row number.")
    print("It is then grouped according to the period and read horizontally in each group and converted back through the squares into letters.")
    print("Vigenere cipher: Takes the key's letter number and the code's letter number per letter and adds them together and subtracting 1(subtracts 26 more if greater than 26) and converts the number back into a letter.")
    typecode = str(input("Advanced substitution cipher, phrase cipher, columunar, trifid, or vignere cipher? (Type sub, phrase, column, tri, or vig) "))
    typecode = typecode.lower()
    alpha1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if typecode == "sub":
        alpha2 = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
        code = str(input("Input your message: "))
        key = str(input('Input your key: '))
        code,key = format1(code,key)
        keylist = []
        ques = str(input("Decrypt or encrypt? "))
        ques = ques.lower()
        if ques == "encrypt":
            for e in range(len(key)):
                for d in range(len(alpha2)):
                    if alpha2[d] == key[e]:
                        keylist.append(d)
            final = ""
            for c in range(len(keylist)):
                alpha2 = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
                if code[c] == " ":
                    final = final + "_"
                for d in range(keylist[c]):
                    alpha2.append(alpha2[0])
                    alpha2.remove(alpha2[0])
                for x in range(len(alpha1)):
                    if alpha1[x] == code[c]:
                        final = final + alpha2[x]
                if code[c] not in alpha1:
                    final = final + code[c]
            print ("Your encrypted message is " + final)
        elif ques == "decrypt":
            for e in range(len(key)):
                for d in range(len(alpha2)):
                    if alpha2[d] == key[e]:
                        keylist.append(d)
            final = ""
            for c in range(len(keylist)):
                alpha2 = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
                if code[c] == "_":
                    final = final + " "
                for d in range(keylist[c]):
                    alpha2.append(alpha2[0])
                    alpha2.remove(alpha2[0])
                for x in range(len(alpha1)):
                    if alpha2[x] == code[c]:
                        final = final + alpha1[x]
            print("Your decrypted message is " + final)
    elif typecode == "phrase":
        boolean = True
        code = str(input("Input your phrase(with spaces) It is reccomended to use words that are longer than 6 letters for most of the phrase: "))
        code = code.lower()
        firstletters = [0]
        lastletters = []
        final = []
        actualfinal = ""
        choice = str(input("First letters or random amount of letters in each word(Won't create any words in the code. Also, type first or random)"))
        choice = choice.lower()
        extra = str(input("Would like us to replace the characters in your code with symbols?(Yes or No)"))
        extra = extra.lower()
        for f in range(0,len(code)):
            if code[f] == " ":
                firstletters.append(f+1)
                lastletters.append(f-1)
        lastletters.append(len(code))
        if choice == "first":
            for x in range(0,len(firstletters)):
                final.append(code[firstletters[x]])
        elif choice == "random":
            for x in range(0,len(firstletters)):
                if firstletters[x] == lastletters[x]:
                    final.append(code[firstletters[x]])
                else:
                    for y in range(firstletters[x],randint(firstletters[x]+1,lastletters[x])):
                        final.append(code[y])
        if extra == "yes":
            letters = ['a','e','i','o','s']
            chars = ['4','3','1','0','$']
            for y in range(len(final)):
                for n in range(len(letters)):
                    if letters[n] == final[y]:
                        final[y] = chars[n]
                actualfinal += final[y]
        else:
            for y in range(len(final)):
                actualfinal += final[y]
        print("Your encrypted message is " + actualfinal)
    elif typecode == "column":
        code = str(input("Input your message(no periods): "))
        key = str(input('Input your key: '))
        final = ""
        code,key = format1(code,key)
        quest = str(input("Encrypt/decrypt"))
        quest =  quest.lower()
        num1 = 0
        num2 = 1
        if quest == "encrypt":
            length = len(key)
            quest =  quest.lower()
            for x in range(len(code)):
                final = final + code[num1]
                if (num1 + length > len(code) - 1):
                    num1 = num2
                    num2 += 1
                else:
                    num1 += length
            print("Your encrypted message is " + final)
        elif quest == "decrypt":
            num1 = 0
            num2 = 1
            if len(code)%len(key) == 0:
                length = len(code)//len(key)
            else:
                length = (len(code)//len(key))+1
            quest =  quest.lower()
            for x in range(len(code)):
                final = final + code[num1]
                if (num1 + length > len(code) - 1):
                    num1 = num2
                    num2 += 1
                else:
                    num1 += length
            print("Your decrypted message is " + final)
    elif typecode == "vig":
        alpha1 = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        code = str(input("Please input your message."))
        key = str(input("Please input your key."))
        code,key = format1(code,key)
        final = ""
        codelist = []
        keylist = []
        ques = str(input("Encrypt or decrypt?"))
        if ques == "encrypt":
            for x in range(len(code)):
                for y in range(len(alpha1)):
                    if code[x] == alpha1[y]:
                        codelist.append(y)
                    if key[x] == alpha1[y]:
                        keylist.append(y)
            for z in range(len(code)):
                if (keylist[z] + codelist[z] > 27):
                    final += alpha1[keylist[z] + codelist[z] - 27]
                elif(keylist[z] == 0 or codelist[z] == 0):
                    final += " "
                else:
                    final += alpha1[keylist[z] + codelist[z]-1]
            print("Your encrypted message is " + final)
        elif ques == "decrypt":
            for x in range(len(code)):
                for y in range(len(alpha1)):
                    if code[x] == alpha1[y]:
                        codelist.append(y)
                    if key[x] == alpha1[y]:
                        keylist.append(y)
            for z in range(len(code)):
                if(keylist[z] == 0 or codelist[z] == 0):
                    final += " "
                elif (codelist[z] - keylist[z] < 0):

                    final += alpha1[codelist[z] - keylist[z] + 27]
                else:
                    final += alpha1[codelist[z]- keylist[z]+1]
            print("Your decrypted message is " + final)
    elif typecode == "tri":
        code = str(input("Please input your message(You may include periods)."))
        key = str(input("Please input your key of all letters of the alphabet with a period or type random for a random key."))
        keylist = []
        if key == "random":
            keybase = "abcdefghijklmnopqrstuvwxyz."
            keylistrand = list(keybase)
            shuffle(keylistrand)
            key = ''.join(keylistrand)
            print("Your key is " + key)
        code,key = format1(code,key,False)
        keylist1 = [[key[0],key[1],key[2]],[key[3],key[4],key[5]],[key[6],key[7],key[8]]]
        keylist2 = [[key[9],key[10],key[11]],[key[12],key[13],key[14]],[key[15],key[16],key[17]]]
        keylist3 = [[key[18],key[19],key[20]],[key[21],key[22],key[23]],[key[24],key[25],key[26]]]
        keylist = [keylist1,keylist2,keylist3]
        period = int(input("Please input your period(how you want to group the code)"))
        quest = str(input("Encrypt or decrypt?"))
        quest = quest.lower()
        if quest == "encrypt":
            codelist = []
            for y in range(len(code)):
                for a in range(3):
                    for b in range(3):
                        for c in range(3):
                            if (code[y] == keylist[a][b][c]):
                                codelist.append([a+1,b+1,c+1])
            codelist2 = []
            n1 = 0
            n2 = period
            for n in range((len(code)//period) +1):
                codelist2.append(codelist[n1:n2])
                if (n2 + period > len(codelist) - 1):
                    n2 += (len(code)%period)
                else:
                    n2 += period
                n1 += period
            codelist3 = []
            final = ""
            for k in range((len(code)//period) +1):
                finalnumbers = ""
                num1 = 0
                for y in range(3):
                    for x in range(len(codelist2[k])):
                           finalnumbers += str(codelist2[k][x][num1])
                    num1 += 1
                var1 = 0
                var2 = 3
                for n in range(int(len(finalnumbers)/3)):
                    for a in range(3):
                        for b in range(3):
                            for c in range(3):
                                if (finalnumbers[var1:var2] == str(a+1) + str(b+1) + str(c+1)):
                                    final += keylist[a][b][c]
                    var1 += 3
                    var2 += 3
                if k != (len(code)//period):
                    final += " "
                
            print("Your encrypted message is " + final)
        elif quest == "decrypt":
            codelist = []
            final = ""
            for y in range(len(code)):
                for a in range(3):
                    for b in range(3):
                        for c in range(3):
                            if (code[y] == keylist[a][b][c]):
                                codelist.append(a+1)
                                codelist.append(b+1)
                                codelist.append(c+1)
            codelist2 = []
            n1 = 0
            n2 = period
            for n in range(((len(code)//period)+1)*3):
                codelist2.append(codelist[n1:n2])
                if (n1 >= len(codelist)-(len(code)%period)*3):
                    n2 += int(len(code)%period)
                    n1 += int(len(code)%period)
                else:
                    n2 += period
                    n1 += period
            n1 = 0
            codelist3 = []
            for x in range((len(code)//period)+1):
                for y in range(period):
                    if len(codelist3) == len(code):
                        break
                    codelist3.append([codelist2[n1][y],codelist2[n1+1][y],codelist2[n1+2][y]])
                n1 += 3
            for n in range(len(codelist3)):
                for a in range(3):
                    for b in range(3):
                         for c in range(3):
                            if (codelist3[n] == [a+1,b+1,c+1]):
                                      final += keylist[a][b][c]
            print("Your decrypted message is " + final)
    again = str(input("Would you like to decrypt/encrypt again? "))
    again = again.lower()
    if again == "yes":
        print("Okay.")
    elif again == "no":
        break
