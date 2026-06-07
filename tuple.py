tup = (1, 2, 3, 4, 5)
# you can slice a tuple by copying a part but you cannot change the original tuple
tup2 = tup[0:3]  # this will print the first three elements of the tuple
print(tup2)
# you cannot change tuple but you can first convert it to a list and then change it and then convert it back to a tuple
tup_list = list(tup)  # convert tuple to list
tup_list[0] = 10  # change the first element of the list
tup = tuple(tup_list)  # convert list back to tuple
print(tup)  # this will print the modified tuple

# when you concatenate two tuples, it creates a new tuple that contains all the elements of both tuples. The original tuples remain unchanged.
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = tup1 + tup2  # concatenate the two tuples
print(tup3)  # this will print (1, 2, 3, 4, 5, 6)

# count() method is used to count the number of occurrences of a specific element in a tuple.
tup = (1, 2, 3, 4, 5, 1, 2, 3)
count_1 = tup.count(1)  # this will count the number of times 1 appears in the tuple
print(count_1)

# index() method is used to find the index of the first occurrence of a specific element in a tuple.
tup = (1, 2, 3, 4, 5)
index_3 = tup.index(
    3
)  # this will find the index of the first occurrence of 3 in the tuple
print(index_3)
# if i want to do the slicing first and then look for the index of an element in the sliced tuple, i can do it like this
res = tup.index(
    3, 0, 3
)  # this will look for the index of 3 in the sliced tuple from index 0 to index 3
print(res)
