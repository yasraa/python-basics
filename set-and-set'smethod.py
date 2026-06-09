# # sets: it is a collection of unique items, it is unordered and unindexed. It is mutable, meaning you can add or remove items from it. Sets are defined using curly braces {} or the set() function.
# my_set = {1, 2, 3, 2, 5}
# print(my_set)
# print(type(my_set))


# s1 = {1, 5, 4, 76}
# s2 = {3, 4, 2, 8, 0}

# # union: it returns a new set that contains all the unique items from both sets.
# union_set = s1.union(s2)
# # to update the original set with the union of two sets, you can use the update() method.
# s1.update(s2)
# print(union_set)
# print(s1)

# # intersection: it returns a new set that contains only the items that are present in both sets.
# intersection_set = s1.intersection(s2)
# # to update the original set with the intersection of two sets, you can use the intersection_update
# # method.
# s1.intersection_update(s2)
# print(intersection_set)
# print(s1)

# # symmetric_difference: it returns a new set that contains the items that are present in either set, but not in both.
# cities1 = {"New York", "Los Angeles", "Chicago"}
# cities2 = {"Chicago", "Houston", "Phoenix"}
# sym_diff_set = cities1.symmetric_difference(cities2)
# # to update the original set with the symmetric difference of two sets, you can use the symmetric_difference_update() method.
# cities1.symmetric_difference_update(cities2)
# print(sym_diff_set)
# print(cities1)


# # difference: it returns a new set that contains the items that are present in one set but not in the other.
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# difference_set = set_a.difference(set_b)
# # to update the original set with the difference of two sets, you can use the difference_update() method.
# set_a.difference_update(set_b)
# print(difference_set)
# print(set_a)

# # disjoint: it checks if two sets have no items in common. It returns True if the sets are disjoint, and False otherwise.
# set_x = {1, 2, 3}
# set_y = {4, 5, 6}
# print(set_x.isdisjoint(set_y))  # Output: True


# # subset and superset: A set A is a subset of set B if all elements of A are also elements of B. A set B is a superset of set A if it contains all elements of A.
# set_a = {1, 2, 3}
# set_b = {1, 2, 3, 4, 5}
# print(set_a.issubset(set_b))  # Output: True
# print(set_b.issuperset(set_a))  # Output: True


# # add: it adds a single item to the set. If the item already exists, it does nothing.
# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)

# # remove: it removes a specific item from the set. If the item does not exist, it raises a KeyError.
# my_set.remove(2)
# print(my_set)
# # discard: it removes a specific item from the set. If the item does not exist, it does nothing.
# my_set.discard(5)
# print(my_set)

# # pop: it removes and returns an arbitrary item from the set. If the set is empty, it raises a KeyError.
# popped_item = my_set.pop()
# print(popped_item)
# print(my_set)


# # delete: it deletes the entire set. After using del, the set will no longer exist.
# my_set = {1, 2, 3}
# del my_set
# # print(my_set)  # This will raise a NameError because my_set has been deleted

# # clear: it removes all items from the set, leaving it empty.
# my_set = {1, 2, 3}
# my_set.clear()
# print(my_set)  # Output: set()


# set exercise:

# students = {"ali", "sarah", "maham", "habib", "ali"}
# print(students)


# student who plays sport:
cricket = {"Ali", "Ahmed", "Sara"}
football = {"Sara", "Bilal", "Ahmed"}

sports = cricket.intersection(football)
print(sports)
