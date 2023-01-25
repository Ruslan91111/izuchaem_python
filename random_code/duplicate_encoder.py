"""Перевести буквы в '(' если единожды встречается и ')' если встречается дважды"""
from collections import Counter


def duplicate_encode(word):
    word = list(word.lower())
    counter = Counter(word)
    new_str = ""
    for char in word:
        if counter[char] == 1:
            new_str += '('
        else:
            new_str += ')'

    return new_str


def duplicate_encode2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)


#This solution is O(n) instead of O(n^2) like the methods that use .count()
#because .count() is O(n) and it's being used within an O(n) method.
#The space complexiety is increased with this method.
import collections
def duplicate_encode(word):
    new_string = ''
    word = word.lower()
    #more info on defaultdict and when to use it here:
    #http://stackoverflow.com/questions/991350/counting-repeated-characters-in-a-string-in-python
    d = collections.defaultdict(int)
    for c in word:
        d[c] += 1
    for c in word:
        new_string = new_string + ('(' if d[c] == 1 else ')')
    return new_string











def duplicate_encode(word):
    """a new string where each character in the new string is '('
    if that character appears only once in the original word, or ')'
    if that character appears more than once in the original word.
    Ignores capitalization when determining if a character is a duplicate. """
    word = word.upper()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("

    return result










