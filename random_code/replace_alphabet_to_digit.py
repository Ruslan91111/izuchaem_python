# change alphabets to digits
def alphabet_position(text):
    lst = []
    for i in text:
        if i.isalpha():
            lst.append(str(ord(i.upper()) - 64))
        else:
            continue

    return ' '.join(lst).rstrip(' ')


def alphabet_position2(text):
    text = text.lower()
    string = ""
    for i in text:
        if i.isalpha():
            string += ' '
            string += str(ord(i) - 96)

    return string.strip()


txt = "The sunset sets at twelve o' clock."


print(alphabet_position(txt))
print(alphabet_position2(txt))
