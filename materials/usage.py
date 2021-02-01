
def list_usage():
    # list -> built-in mutable type that keeps the order of the elements (can access through index) and provides iteration over them
    # mutable means that you can change the elements of the list as you wish

    # 1. Initializing an empty list
    list_1 = []
    list_2 = list()

    # 2. Creating a list from predefined elements
    list_3 = [2, 3, 4]
    list_4 = [list_1, list_2, list_3]
    list_5 = list(list_3)  # the list constructor can create a list from any 'iterable' object (set, list, 'dict.items()', tuple)
    list_6 = [el for el in list_4]

    # 3. list methods
    demo_list = ["e", "a", "b"]

    # '.append(el)' -> adds 'el' at the end of the list
    demo_list.append("e")  # demo_list = ["e", "a", "b", "e"]

    # '.pop(index)' -> removes and returns the element at 'index'
    el = demo_list.pop(1)  # el = "a"; demo_list = ["e", "b", "e"]

    # '.remove(el)' -> removes the first occurrence of 'el' from the list
    demo_list.remove("e")  # demo_list = ["b", "e"]

    # '.reverse()' -> reverses the list
    demo_list.reverse()  # demo_list = ["e", "b"]

    # '.insert(index, el)' -> adds 'el' at 'index' position in the list
    demo_list.insert(0, el)  # demo_list = ["a", "e", "b"]

    # '.index(el)' -> returns the index of the first occurrence of 'el'
    idx = demo_list.index("b")  # idx = 2

    # '.count(el)' -> returns the number of occurrences of 'el' in the list
    count_a = demo_list.count("a")  # count_a = 1

    # '.extend(iterable)' -> extends the list by adding the elements of 'iterable' at the end of the list
    # same effect: demo_list = demo_list + list_5
    demo_list.extend(list_5)  # demo_list = ["a", "e", "b", 2, 3, 4]

    # 4. operations over list
    list_a, list_b = [2, 3, 4], [5, 6, 7]

    # concatenation
    list_c = list_a + list_b  # list_c = [2, 3, 4, 5, 6, 7]

    # 'in' and 'not in' operators: el in/not in list
    contains = 2 in list_a  # contains = True
    contains = 2 not in list_a  # contains = False

    # accessing elements through index
    # in python, the indexing of list begins from 0
    # ex: list = ["a", "b", "c"] -> indices = [0, 1, 2]
    # python gives us one more feature for indexing and that's indexing the list from the back with negative indices, starting from -1
    # ex: list = ["a", "b", "c"] -> negative indices = [-3, -2, -1]
    el = list_a[2]  # el = 4
    el = list_a[-1]  # el = 4

    el = list_a[1]  # el = 3
    el = list_a[-2]  # el = 3

    el = list_a[0]  # el = 2
    el = list_a[-3]  # el = 2

    # slicing: list[start_index_inclusive:end_index_exclusive]
    sub_list = list_c[2:5]  # sub_list = [4, 5, 6]
    sub_list = list_c[:3]  # sub_list = [2, 3, 4]
    sub_list = list_c[3:]  # sub_list = [5, 6, 7]

    # changing elements through index
    list_c[5] = 9  # list_c = [2, 3, 4, 5, 6, 9]

    # getting the length of a list with 'len()'
    length = len(list_c)  # length = 6

    # 5. iterations over lists
    # element by element
    for el in list_c:
        print(el)

    # by index
    # range(startInclusive, endExclusive) -> returns a "list" of numbers from startInclusive to endExclusive - 1
    # ex: range(0, 5) -> [0, 1, 2, 3, 4]
    # later we use that "list" and iterate it's elements in a regular for loop
    # if we don't specify startInclusive, Python sets startInclusive to 0
    # so this: range(len(list_c)) is equivalent to this: range(0, len(list_c))
    for i in range(len(list_c)):
        print(list_c[i])

    # iterating over multiple lists in one loop with 'zip()'
    # 'zip(list_1, list_2, ...)' -> allows for iteration of the list arguments in one loop
    # the lists should be of same length
    for el_a, el_b, el_new in zip(list_a, list_b, [8, 9, 10]):
        # el_a -> list_a; el_b -> list_b; el_new -> [8, 9, 10]
        print(el_a, el_b, el_new)


def tuple_usage():
    # tuples are a built-in immutable type that store data in a similar way to lists (keep the order)
    # immutable means that the values inside an already initialized tuple can't be changed
    # more info: https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/

    # creating a tuple -> with '()'
    tup = (2, 3)

    # with 'tuple()' constructor
    # the 'tuple()' constructor can create a tuple from any iterable object, such as list, set, another tuple...
    some_list = [2, 3]
    tup = tuple(some_list) # tup = (2, 3)

    # tup[0] = 3 -> this is not possible because tuples are immutable
    # if you want some change in a tuple, you must create a new one
    # let's say you want to swap the positions of the elements in the tuple
    # you do this:
    # tmp = tup[0]
    # tup[0] = tup[1]
    # tup[1] = tmp
    # if 'tup' was a list it would be possible, but this will throw an error. Instead the right way is this: (create a new tuple)
    swapped_tuple = (tup[1], tup[0])

    # iterates through every element in the tuple
    for el in tup:
        print(el)

    tuple_list = [(2, 4, 5), (2, 4, 7), (5, 6, 0)]

    # iterating through tuple list
    for tup in tuple_list:
        print(tup[0], tup[1], tup[2])

    for (el1, el2, el3) in tuple_list:
        print(el1, el2, el3)


def list_comprehension_usage():
    # list comprehension -> the process of creating a list, from another list
    # the syntax: new_list = [expression for item in otherList if some-condition]
    # 'expression' can be any manipulation of 'item' which result will be saved in 'new_list'
    # 'some-condition' tests the item for some condition; if it results to 'True', 'expression' is executed over that item, else it's ignored
    # 'some-condition' is optional
    demo_list = [1, 2, 3, 4, 5]

    # expression = 'item * 2'
    # condition = 'item > 3'
    list = [item * 2 for item in demo_list if item > 3]  # list = [8, 10]
    list = [item for item in demo_list]  # copy of 'demo_list'; no condition

    lists = [[2, 4], [6, 9], [10, 6]]
    # create a list which contains the maximum elements of each list in 'lists'
    result = [max(list) for list in lists]  # result = [4, 9, 10]

    # create a tuple list of the list 'lists' so that each element in the new list
    # will be a tuple consisting of one element of each list
    # lists = [[2, 4], [6, 9], [10, 6]]; result = [(2, 6, 10), (4, 9, 6)]
    result = [(el1, el2, el3) for el1, el2, el3 in zip(lists[0], lists[1], lists[2])]

    # filter each list in 'lists' so that each one of the inner lists contains only elements larger than 5
    result = [[el for el in list if el > 5] for list in lists]  # 'expression' can be another list comprehension
    # result = [[], [6, 9], [10, 6]]

    lists = [[2, 4, 5], [6, 9, 10], [10, 6, 20]]
    # make every list in 'lists' to contain only the first and last element of the current list
    result = [[list[0], list[-1]] for list in lists]  # result = [[2,5], [6,10], [10,20]]

    tuple_list = [("a", 2), ("b", 3), ("c", 4)]
    # swap the elements position in the tuples in 'tuple_list'
    result = [(el2, el1) for (el1, el2) in tuple_list]  # result = [(2, "a"), (3, "b"), (4, "c")]
    result = [(tup[1], tup[0]) for tup in tuple_list]  # result = [(2, "a"), (3, "b"), (4, "c")]

    demo_list = [2, 3, 4, 5, 6, 7]
    # filter 'demo_list' so that it only contains even numbers
    # then create an list from each even number that contains exactly than many elements and every element in that list is that even number
    # ex: demo_list = [2, 3, 4] => [[2, 2], [4, 4, 4, 4]]
    result = [[num for i in range(num)] for num in demo_list if num % 2 == 0]

    tuple_list = [(2, 4, 5), (2, 4, 7), (5, 6, 0)]
    # filter 'tuple_list' so that every tuple contains only elements larger or equal than 5
    result = [tuple([el for el in tup if el >= 5]) for tup in tuple_list]  # result = [(5), (7), (5, 6)]


def set_usage():
    # set is a collection object which does not keep the order of the elements (can't access with index)


    empty_set = set()


if __name__ == '__main__':

    print("hello world!")
    list_usage()

