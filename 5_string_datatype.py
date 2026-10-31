# String:
    # String is a squence of charecters.
    # enclosed by quotes.
    # Ex: "apple", '7890', '#$%^', "dfghcvbFGHJ4567%^&"

    # What type of dattaype is string:
        # String is a sequence of charecters
        # String is Immutable (Can not be modified)
        # String is ordered
        # Strings supports Indexing.
        # Inside string you can have duplicates.

#-----------------------------------------------------------
# Formation of String using different quotes:
    # ''  => Single quotes
    # ""  => Double quotes
    # ''' ''' => Tripple Single quotes
    # """ """ => Tripple Double quotes

# str1 = 'Apple'
# print(str1, type(str1))

# str2 = "Apple"
# print(str2, type(str2))

# str3 = '''Apple'''
# print(str3, type(str3))

# str4 = """Apple"""
# print(str4, type(str4))


# NOTE: Small Strings line words or single line sentence
# then use '', ""

# str5 = 'Apple@1234'
# print(str5, type(str5))
# str6 = "Apple@1234"
# print(str6, type(str6))

# str7 = 'David is the "tallest" among all students.'
# print(str7, type(str7))

# str8 = "Sara is the most 'beautiful' among all ladies in the hall."
# print(str8, type(str8))

# NOTE: For Big Strings which are more than single line, to form them
# use ''' ''', """ """

# str9 = '''Python is a 'Programming' Language.
# Python is used to write "code".
# Python also used for "scripting."'''

# print(str9, type(str9))

# str10 = """Ravi asked kiran '''Where are we going?'''
# Kiran Replied '''We are heading to sara's home.'''
# Ravi laughed and said '''Weldone..!'''"""

# print(str10, type(str10))

# str11 = '''David """I am tired."""
# mother """Why ?"""
# David """I played a lot."""'''
# print(str11, type(str11))


#-------------- Final Mixed quotes string:

# str12 = """Bob '''Where are you bunny?'''
# bunny '''I am in park. it is very 'awesome'.'''
# Bob '''Shut up..! Immediately come to home. dont you remember we have to finish our "summer project".'''"""

# print(str12, type(str12))

#--------------------------------------------------------
# Indexing:

# str1 = "APPLE"
# print(str1)    #=> Access Complete String
#---> Positive Indexing
# print(str1[0]) #=> A
# print(str1[1]) #=> P
# print(str1[2]) #=> P
# print(str1[3]) #=> L
# print(str1[4]) #=> E

#---> Negative Indexing
# print(str1[-5]) #=> A
# print(str1[-4]) #=> P
# print(str1[-3]) #=> P
# print(str1[-2]) #=> L
# print(str1[-1]) #=> E


#---------------------------------------------

# str2 = '''Hello This is Shanghai.
# Worlds most beautiful city.'''

# print(str2[0])
# print(str2[6])
# print(str2[14])
# print(str2[24])

# print(str2[-5])
# print(str2[-15])
# print(str2[-19])

#---------------------------------------------
# Slicing:
# str1 = "APPLE"
# print(str1[0:3:1])   # APP

# print(str1[4:0:-1])  # ELPP

#-------------------------------------------------

# str2 = "India is My Country"
# print(str2[0:5:1])
# print(str2[-7::1])

# # aidnI
# print(str2[4::-1])

# # yrtnuoC
# print(str2[-1:-8:-1])

# # Idai
# print(str2[0:7:2])
# # Ia Ct
# print(str2[0::4])

# # CMii
# print(str2[-7:2:-3])


#--------------------------------------------------------
# String In Built Methods:

    # Method => Function => Block of code to perform a specific operation on data.

    # Methods can be of two types:
        # Built in Methods
            # Ready to use, provided by python itself

        # User Defined Methods:
            # Developers write these custom methods.

#---------- String Built In Methods:

    # Case Conversion:   NOTE: Related to only alphabets

        # .upper()   # converts only lowercase letters into uppercase
        # .lower()   # converts only uppercase letters into lowercase
        # .capitalize() # First letter of of string converted to uppercase and rest of the uppercase letters will be converted to lowercase.
        # .title()  # In String each words first alphabet converted to uppercase and rest lowercase
        # .swapcase()  # To convert uppercase to lowercase and lowercase to uppercase

# str1 = 'apple@#$1234'
# print(str1.upper())   #APPLE@#$1234

# str2 = "GRAPES@#$1234"
# print(str2.lower())   #grapes@#$1234

# str3 = "banANA@#$1234"
# print(str3.capitalize())  #Banana@#$1234

# str4 = "i love my inida, 3000 tonnes."
# print(str4.title())   #I Love My Inida, 3000 Tonnes.

# str5 = "ANDErson"
# print(str5.swapcase())   #andeRSON

#-----------------------------------------------------

    # is Methods: Returns Answer in Booleans (True, False)

        # .isupper()   # If strings all alphabets are in uppercase then "True" else "False"
        # .islower()   # If strings all alphabets are in lowercase then "True" else "False"
        # .istitle()   # Each word's firs alphabet is upper and rest lower then "True" else "False"
        # .isdigit()   # IF strings all elments are numeric digits then "True" else "False"
        # .isalpha()   # If Strings all elements are alphabets then "True" else "False"
        # .isalnum()   # If strings elements are alphabetic or numeric or both then "True" else "False"
        # .isspace()   # IF strings all elments are empty spaces then "True" else "False"

# str1 = "CROCODILE@#$1234"
# print(str1.isupper())

# str2 = "CHOcoLATE@123"
# print(str2.isupper())
# print(str2.islower())

# str3 = "Ferrari Is Best"
# print(str3.istitle())

# str4 = "12345"
# print(str4.isdigit())

# str5 = "Alpha1234"
# print(str5.isalnum())

# str6 = "AlphaBeta"
# print(str6.isalnum())

# str7 = "987654"
# print(str7.isalnum())

# str8 = "     "
# print(str8.isspace())

# str9 = "   ."
# print(str9.isspace())


#---------------------------------------------------

    # Some other methods of string:
# str1 = "BOB"

        # center()
# print(str1.center(11, "-"))

        # ljust()
# print(str1.ljust(11, "*"))

        # rjust()
# print(str1.rjust(11, "-"))

        # zfill()
# print(str1.zfill(8))

        # count()
# str2 = "hgsgdh743wueygdhjgerhewjhdbsansde"
# print(str2.count("g"))

        # endswith()
# print(str2.endswith("sansde"))

        # startswith()
# print(str2.startswith("hgsgdh"))

        # strip()
# str3 = "    We are python developers    "
# list1 = str3.strip(" ")
# print(list1)

        # lstrip()
# print(str3.lstrip())

        # rstrip()
# print(str3.rstrip())

        # split()
# list2 = str3.split()
# print(list2)

# str4 = "Our-Job-is-Ok"
# print(str4.split("-"))


        # join()
# words = ["Python", "Is", "Awesome"]
# str5 = " ".join(words)
# print(str5)

        # format()
name = "Shiv"
city = "Vaizag"

# str6 = "My name is {}, I am from {}".format(name, city)
# print(str6)

        # format_map()
# str7 = "My Dear Friend {friend}, you are from {country}".format_map({"friend": "John", "country": "Italy"})
# print(str7)

# str8 = f"Hello {name}, what enginner are you ? If you are IT Engineer then go to {city}"
# print(str8)


    # Search Methods:
# str9 = "Amanora AAAA Apple"

        # index()   # Leftmost elments index
# print(str9.index("A"))
# print(str9.index("Z"))    #ValueError: substring not found

        # find()
# print(str9.find("A"))
# print(str9.find("Z"))    # -1

        # rindex()
# print(str9.rindex("A"))   # rightmos lements index
# print(str9.rindex("Z"))   # ValueError: substring not found

        # rfind()
# print(str9.rfind("A"))
# print(str9.rfind("Z"))


#--------------------------------------

# Packing & Unpacking:

# char1, char2, char3 = "ABCD"
# print(char1)

#ValueError: too many values to unpack (expected 3)
#ValueError: not enough values to unpack (expected 3, got 2)


# Concatination: 
    # To attach different strings together
s1 = "Hello"
s2 = "Brother"

print(s1+" "+s2)

num1 = "5"
num2 = "7"
print(num1+num2)

# Repetation:
str11 = "Hi"
print(str11*5)  #HiHiHiHiHi


