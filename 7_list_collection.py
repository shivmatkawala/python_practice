# List Collection:
    # List is a collection datatype.
    # List is the most popular collection in python.
    # List is non-primitive datatype
    # List is mutable (Can be modified)
    # List is heterogenous (Allows all types of data into it)
    # List allows us to store duplicates
    # List is formed using [], list()
    # List is ordered 
    # List also supports Indexing.

#----------------------------------------------------
# Initialization of List:

# l1 = []
# print(l1, type(l1))

# l2 = [1, 2, 3, 4]
# print(l2, type(l2))

# l3 = [1, 1.1, 2+3j, True, "Apple"]
# print(l3, type(l3))

# l4 = [[1, 2, 3], ["A", "B", 55], [3.3, 6-7j], "Andrew"]
# print(l4, type(l4))

# list()  is famous to convert non-list collection into list
# l5 = list()
# print(l5, type(l5))

# l6 = list(1)
# print(l6, type(l6))  #TypeError: list expected at most 1 argument, got 4, TypeError: 'int' object is not iterable

# t1 = (1, 2, 34)
# l7 = list(t1)
# print(l7, type(l7))

#-----------------------------------------------------------
# Indexing:
    # +ve Indexing
    # -ve Indexing

# list1 = [12, 23, 34, 45, "A", "K", 4.5, 9-8j]
# print(list1, type(list1))

# print(list1[0])
# print(list1[1])
# print(list1[5])
# print(list1[7])
# print(list1[-4])
# print(list1[-8])
# print(list1[-6])

#------------------------------------------------------------
# Slicing:
# list1 = [12, 23, 34, 45, "A", "K", 4.5, 9-8j]

# start index, stop index, step, direction
# 12, 23, 34, 45
# 0, 4, 1
# print(list1[0:4:1])
# print(list1[-1:-4:-1])
# 23, "A, 9-8j
# print(list1[1::3])
# 4.5, "A", 34
# print(list1[-2:1:-2])

#-------------------------------------------------------
# Built-In Methods of List:

l1 = []

    # Insertion Methods:
        # .append()  => adds exactly one elment at the end of list
        # .extend()  => adds multiple elements at the end of list
        # .insert()  => adds exactly one elment at specific index

# l1.append("Hi")
# l1.append("Bye")
# l1.append(45)

# l1.extend([1, 2, 3])
# l1.extend("Apple")

# l1.insert(0, 100)
# l1.insert(4, 500)


    # Deletion Methods
        # .pop()  # removes element from specified index, 
        # if index not given then last element.

        # .remove()  # removes the spcified element from the list,
        # only first appearance of the element

        # .clear()  # It removes all elements from the list 
        # and make list empty.

# l1.pop()
# l1.pop(2)

# l1.remove(500)
# l1.remove("p")

# l1.clear()
# print(l1)

    # Some Other Methods:
        # .copy()   # Creates shallow copy of list
        # .count()  # counts specific elments occureneces in list
        # .sort()  # sorting of list elements in asc, desc order
        # .reverse() # to reverse a list

# l2 = ["A", 67, 12, 'k', "H", "B", 0, 67, "a", 67]
# l3 = l2.copy()
# print(l3, type(l3))

# print(l3.count(67))


l3 = [5, 3, 8, 9, 1,0, 2]

# l3.sort()   # [0, 1, 2, 3, 5, 8, 9]
# l3.sort(reverse=True)   #[9, 8, 5, 3, 2, 1, 0]

# l3.reverse()

# print(l3)

#-------------------------------------------------
# Packing & Unpacking:
# l11 = [12, 23, 34]
# x, y, z = l11

# print(x)
# print(y)
# print(z)

# Concation
# l1 = [1, 2, 3]
# l2 = [4, 5, 6, 7, 8]
# print(l1+l2)

# Repetation:
# l1 = [12, 23, 34]
# print(l1*4)
