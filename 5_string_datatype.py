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

str2 = "India is My Country"
print(str2[0:5:1])
print(str2[-7::1])

# aidnI
print(str2[4::-1])

# yrtnuoC
print(str2[-1:-8:-1])

# Idai
print(str2[0:7:2])
# Ia Ct
print(str2[0::4])

# CMii
print(str2[-7:2:-3])
