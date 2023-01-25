"""If the string have repeated letter it's not a isogram - return False. No matter upper or lower case. Blank string
also isogram"""



def is_isogram(string):
    if string == '':
        return True

    else:
        lst = list(string.lower())
        new_lst = []
        for i in lst:
            if i in new_lst:
                return False

            else:
                new_lst.append(i)

        print(new_lst)

        if new_lst:
            return True


def is_isogram2(string):
    return len(string) == len(set(string.lower()))


def is_isogram3(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True







