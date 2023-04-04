# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.

def pig_it(text):
    # Разбить строку по словам конвертировать в список.
    lst = list(text.split(' '))
    new_lst = []

    for word in lst:
        # Если слово содержит только буквы, то сложить слово согласно заданию.
        if word.isalpha():
            new_word = word[1:] + word[0] + 'ay'
            new_lst.append(new_word)
        # Если не только буквы, то добавить слово как оно есть.
        else:
            new_lst.append(word)
    # Собрать строку.
    string = ' '.join(new_lst)

    return(string)


print(pig_it('Pig latin is cool'))  # igPay atinlay siay oolcay
print(pig_it('Hello world !'))  # elloHay orldway !


def pig_it2(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

print(pig_it2('Pig latin is cool'))  # igPay atinlay siay oolcay
print(pig_it2('Hello world !'))  # elloHay orldway !