from random import shuffle


# Формируем список из цифр.
my_list = list('7'*40 + '9' * 40 + '4' * 50)

# Перемешиваем его - цифры располагаются в произвольном порядке.
shuffle(my_list)

# Объединяем в единую строку.
my_string = "".join(my_list)

count = 0
while '49' in my_string or '97' in my_string or '47' in my_string:
    count += 1
    if '47' in my_string:
        my_string = my_string.replace('47', '74', 1)
    elif '97' in my_string:
        my_string = my_string.replace('97', '79', 1)
    elif '49' in my_string:
        my_string = my_string.replace('49', '94', 1)


print(count)
print(my_string)
print(my_string[25] + my_string[71] + my_string[105])




