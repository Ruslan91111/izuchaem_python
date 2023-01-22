"""Из первого списка вычесть второй список, должны остаться значения, которые
есть в первом списке, но нет во втором
"""

my_list1 = [1, 2]
my_list2 = [1]


def subtracts_lists(lst1, lst2):
    new_lst = []
    for i in lst1:
        if i in lst2:
            pass
        else:
            new_lst.append(i)
    return new_lst


print(subtracts_lists(my_list1, my_list2))


# Apply list comrehension.
def subtracts_lists2(lst1, lst2):
    return [i for i in lst1 if i not in lst2]


print(subtracts_lists2(my_list1, my_list2))


def subtracts_lists3(lst1, lst2):
    return filter(lambda x: x not in lst2, lst1)


print(subtracts_lists3(my_list1, my_list2))




