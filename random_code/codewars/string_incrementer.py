"""Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.
"""
from itertools import count


def increment_string(strng):
    string_without_digits_in_the_end = strng.rstrip('1234567890')
    digits_in_the_end = strng[len(string_without_digits_in_the_end):]

    if digits_in_the_end == '':
        return strng + '1'
    else:
        return string_without_digits_in_the_end + str(int(digits_in_the_end) + 1).zfill(len(digits_in_the_end))


print(increment_string("foo"))          #"foo1")
print(increment_string("foobar001"))    #"foobar002")
print(increment_string("foobar1"))      #"foobar2")
print(increment_string("foobar00"))     #"foobar01")
print(increment_string("foobar99"))     #"foobar100")
print(increment_string("foobar099"))    #"foobar100")
print(increment_string("fo99obar99"))   #"fo99obar100")
print(increment_string(""))             #"1")
