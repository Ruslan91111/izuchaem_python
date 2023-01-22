"""Take list and filer out strings """

my_lst = [1, 2, 'a', 'b']


def filter_list(lst):
    new_lst = []
    for i in lst:
        if isinstance(i, str):
            pass
        else:
            new_lst.append(i)

    return new_lst


# list comprehension
def filter_list2(lst):
    return [i for i in lst if not isinstance(i, str)]


def filter_list3(lst):
    return list(filter(lambda x: not isinstance(x, str), lst))


def filter_list4(lst):
    return [x for x in lst if type(x) is not str]


print(filter_list(my_lst))
print(filter_list2(my_lst))
print(filter_list3(my_lst))
print(filter_list4(my_lst))

