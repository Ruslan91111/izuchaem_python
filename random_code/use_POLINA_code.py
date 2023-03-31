""" Подобрать из символов 'ПОЛИНА' шестизначные коды, буквы встречаются по одному разу.
Посчитать количество вариантов кода при условии, что не должно подряд идти двух гласных или согласных"""
from itertools import product, permutations


# Набор символов из которых необходимо выполнить подбор кодов.
string = 'POLINA'

# Формируем итерируемую последовательность вариантов кода
iter_seq = product(string, repeat=6)

# Гласные
vowels = 'OIA'
# Согласные
consonants = 'PLN'

# формируем подходящие варианты, чтобы все буквы были по одной
new_list = []
for item in iter_seq:
    if item.count('P') == 1 and item.count('O') == 1 and item.count('L') == 1 \
            and item.count('I') == 1 and item.count('N') == 1 and item.count('A') == 1:
        new_list.append(item)

# Либо можно сформировать не обходимую последовательность через itertools
new_list2 = permutations(string, r=6)

# Счетчик
count = 0
# Перебираем последовательно каждый внутренний список и проверяем на выполнение условия.
for inner_list in new_list:
    flag = True

    # Цикл for запускается в диапазоне внутреннего списка.
    # Минус один (-1), потому что счет с 0, и чтобы не было лишней итерации
    for indx in range(len(inner_list)-1):
        # Проверка, что рядом нет двух согласных или гласных.
        if (inner_list[indx] in consonants and inner_list[indx+1] in consonants) or \
                (inner_list[indx+1] in vowels and inner_list[indx] in vowels):
            flag = False
    if flag:
        count += 1

print(count)



