"""Take two stings, return one strings, containing distinct letters"""

my_str1 = "aretheyhere"
my_str2 = "yestheyarehere"

def sort_two_strings(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    union_sets = sorted(str1.union(str2))
    result_str = ''.join(union_sets)
    return result_str


def sort_two_strings2(str1, str2):
    return ''.join(sorted(set(str1+str2)))


def sort_two_strings3(str1, str2):
    return ''.join(sorted(set(str1) | set(str2)))


print(sort_two_strings(my_str1, my_str2))
print(sort_two_strings2(my_str1, my_str2))
print(sort_two_strings3(my_str1, my_str2))





