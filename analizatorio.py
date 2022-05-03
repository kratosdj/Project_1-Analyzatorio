import collections
from itertools import count
import sys

'''
author = Ludek Larys DJ Kratos
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# MOZNE PRIHLASOVACI UDAJE
usernames = ['bob', 'ann', 'mike', 'liz']
passwords = ['123', 'pass123', 'password123', 'pass123']

# SEBRANI UZIVATELSKEHO JMENA A HESLA
username = input("USERNAME: ")
password = input("PASSWORD: ")

# KONTROLA PRIHLASOVACIHO JMENA VUCI JMENUM
if username in usernames:
    # ZJISTENI INDEXU PRO UZIVATELE
    index = usernames.index(username)
    # NASLEDNA KONTROLA HESLA PRO UZIVATELE POMOCI INDEXU
    if password == passwords[index]:
        print(f"WELCOME TO ANALYZATORIO {username}.")
        # VZIT JENOM INTEGER INPUT
        try:
            analyze_text = int(input("CHOOSE WHICH TEXT TO ANALYZE [1-3]: "))
        # POKUD NEDOSTANEME INTEGER - PROGRAM UKONCIME
        except:
            print("INVALID INPUT DETECTED... SHUTTING DOWN")
            sys.exit()
        # POKUD JE VOLBA VETSI NEZ VELIKOST NASEHO LISTU NEBO 0 - PROGRAM UKONCIME
        if analyze_text >= 4:
            print("YOU HAVE CHOSEN INVALID TEXT ID... SHUTTING DOWN")
            sys.exit()
        elif analyze_text == 0:
            print("YOU HAVE CHOSEN INVALID TEXT ID... SHUTTING DOWN")
            sys.exit()
        else:
            text = TEXTS[analyze_text - 1] # ODECTEME JEDNU PRO SPRAVNY INDEX
            splited = text.split() # SPLIT TEXTU
            number_of_words = len(splited) # POCET SLOV V TEXTU
            
            ###
            ### POSSIBLE COMPREHENSION SOLUTION
            ###

            # cap_wrd = [ x.istitle() for x in splited]
            # cap_count = cap_wrd.count(True)
            # print(f"Number of Cap-WRD {cap_count}")
            
            # low_wrd = [ x.islower() for x in splited ]
            # low_count = low_wrd.count(True)
            # print(f"Lower words {low_count}")
            
            # upp_wrd = [ x.isupper() for x in splited ]
            # upp_count = upp_wrd.count(True)
            # print(f"Upper words {upp_count}")

            # num_wrd = [ x.isnumeric() for x in splited ]
            # num_count = num_wrd.count(True)
            # print(f"Number words {num_count}")
            
            # num_list = [ int(x) for x in splited if x.isdigit()]
            # num_sum = sum(num_list)
            # print(f"Numeric Sum is {num_sum}")
            
            capital_words = 0 # POCET SLOV ZACINAJICICH VELKYM PISMEM
            lower_words = 0 # POCET SLOV JEN S MALYMI PISMENY
            upper_words = 0 # POCET SLOV JEN S VELKYMI PISMENY
            numers = 0 # POCET CISEL
            number_list = [] # LIST PRO DRZENI CISEL
            for i in splited:
                if i.islower(): # KONTROLA MALYCH PISMEN
                    lower_words += 1
                elif i.isupper(): # KONTROLA VELKYCH PISMEN
                    upper_words += 1
                elif i[0].isupper(): # KONTROLA PRVNIHO VELKEHO PISMENA
                    capital_words += 1
                elif i.isnumeric(): # KONTROLA CISEL V TEXTU
                    numers += 1
                    number_list.append(int(i))
            numero_sum = 0
            for n in number_list: # SECTENI VSECH CISEL V TEXTU
                numero_sum = numero_sum + n          

            # TISK NASBIRANYCH HODNOT
            print(f"Number of Words: {number_of_words}")
            print(f"Capitals: {capital_words}\nLower: {lower_words}\nUpper: {upper_words}\nNumers: {numers}\nSum of Numbers: {numero_sum}")
            print("Capitals: " + ("*" * capital_words) )
            print("Lowers: " + ("*" * lower_words))
            print("Uppers: " + ("*" * upper_words))
            print("Numeros: " + ("*" * numers))

            worderino = [len(x) for x in splited]
            worderino.sort()
            
            occurences = collections.Counter(worderino)
            print("...LEN...|...OCC...|...NUM...")
            for i in occurences:
                star = occurences[i] * "*"
                print(f"{i}|{star}|{occurences[i]}")
        
            
    # KONTROLA HESEL VUCI DOSTUPNYM HESLUM
    elif password in passwords:
        print("YOUR PASSWORD MATCHES DIFFERENT USER")
    else:
        print("INVALID PASSWORD... SHUTTING DOWN")
        sys.exit()
# POKUD NEDOSTANEME PLATNE HESLO - PROGRAM UKONCIME
else:
    print("INVALID USERNAME... SHUTTING DOWN")
    sys.exit()
