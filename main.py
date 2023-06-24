# Дана строка n, Вывести кол во каждого символа в ней.

def strCounter(string: str):
    for symbol in string:
        counter = 0
    for sub_symbol in string:
        if sub_symbol == symbol:
            counter += 1
    print(symbol, counter)


# Данный алгоритм работает со сложностью 0(N**2).
def strCounter_first(string: str):
    for symbol in string:
        counter = 0
    for sub_symbol in string:
        if sub_symbol == symbol:
            counter += 1
    print(symbol, counter)


# Данный алгоритм работает со сложностью O(N * M)
def strCounter_second(string: str):
    for symbol in set(string):
        counter = 0
        for sub_symbol in string:
            if sub_symbol == symbol:
                counter += 1
    print(symbol, counter)

# Данный алгорнитм работает за O(N)
def strCounter_third(string: str):
    symbols = {}
    for symbol in string:
        symbols[symbol] = symbols.get(symbol, 0) + 1
    return symbols