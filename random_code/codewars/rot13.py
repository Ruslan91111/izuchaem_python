"""Шивфрует строку: выдает символ от исходного через 13 позиций по ASCII,
если до 'N' и 'n' + 13 позиций, если после - 13 позиций. """


def rot13(message):

    first_half_of_alphabet = 'abcdefghijklmABCDEFGHIJKLM'
    new_message = []
    for symbol in message:
        if symbol.isalpha():
            if symbol in first_half_of_alphabet:
                new_message.append(chr(ord(symbol)+13))
            else:
                new_message.append(chr(ord(symbol) - 13))
        else:
            new_message.append(symbol)
    return ''.join(new_message)
