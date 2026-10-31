# Tuple:
    # Tuple is a collection
    # Tuple is immutable
    # Tuple is heterogeneous
    # Tuple is initialized using (), tuple()
    # tuple is ordered 
    # tuple supports indexing
    # tuple allows duplicates

#----------------------------------------------------------
# Initialization of tuple:

# t1 = ()
# print(t1, type(t1))

# t2 = (1, 2, 3)
# print(t2, type(t2))

# t3 = (1, 1.1, 2+4j, "Hi", False, ["Apple", 12, 34.5, "Banana"], (100, "Canada"))
# print(t3, type(t3))

# t4 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# print(t4, type(t4))

# NOTE: tuple() is famous to convert another collection into tuple
# t5 = tuple()
# print(t5, type(t5))

# t6 = tuple([1, 2, 3])
# print(t6, type(t6))   #TypeError: tuple expected at most 1 argument, got 4, TypeError: 'int' object is not iterable

# t7 = tuple("BANANA")
# print(t7, type(t7))

#-----------------------------------------------------
# Indexing:

# t8 = (12, 34, 89, 56)
# print(t8, type(t8))

# print(t8[0])
# print(t8[1])
# print(t8[2])

# print(t8[-2])
# print(t8[-3])
# print(t8[-4])

#------------------------------------------------------
# Slicing:  start: stop: step=> direction

# t9 = ("A", "B", "C", 78, 45, 55, 10, 5.5, 6.6, 7.7)

# print(t9[0:3:1])
# print(t9[2::-1])

# print(t9[-7:-3:1])
# print(t9[-7:-3:1][::-1])
# print(t9[-4:-8:-1])

# print(t9[0::2])
# print(t9[-1::-2])

#----------------------------------------------------------
# Built-In Methods:

    # .count()  => counts specific elments occurences into tuple
    # .index()  => gets you the +ve index number of specified elment's first occurence

# t10 = (12, 34, 12, 78, 5, 4, 12, 90, 5, 4, 0, 12)
# print(t10.count(12))
# print(t10.index(12))
# print(t10.index(5))


# packing and unpacking:

# t11 = ("Hi", "Adam", 45)
# greet, name, marks = t11
# print(greet)
# print(name)
# print(marks)

# concatination:
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# print(t1+t2)

# repetation 
# t1 = (1, 2, 3)
# print(t1*2)
