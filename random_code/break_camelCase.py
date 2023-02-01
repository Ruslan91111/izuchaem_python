"""Function will break up camel casing, using a space between words."""
def camel_case(string):
    return "".join(' ' + i if i.isupper() else i for i in string)


def camel_case2(string):
    new_string = ''
    for i in string:
        if i in list('QWERTYUIOPLKJHGFDSAZXCVBNM'):
            new_string += ' '
            new_string += i
        else:
            new_string += i

    return new_string


def camel_case3(string):
    lst = list(string)
    new_lst = []
    for i in lst:
        if i.isupper():
            new_lst.append(' ')
            new_lst.append(i)
        else:
            new_lst.append(i)

    return "".join(new_lst)





