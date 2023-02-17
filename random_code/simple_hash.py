# Детский пример хеша. Каждый символ в строке переводится в код ASCII.
# Функция возвращает сумму кодов ASCII деленная на количестве слотов.
def hash1(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum % tablesize


# Умножаем каждый код ASCII на позиционный номер в последовательности.
# Не учитывая 0.
def hash2(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + (ord(astring[pos]) * (pos+1))

    return sum % tablesize







