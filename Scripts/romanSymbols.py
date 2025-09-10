ROMAN_SYMBOLS = {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
    'VI': 6,
    'VII': 7,
    'VIII': 8,
    'IX': 9,
    'X': 10,
}


def translate(symbol_a, symbol_b):
    value_a,value_b  = symbol_a, symbol_b

    for key, value in ROMAN_SYMBOLS.items():
        if symbol_a == key:
            value_a = value
        elif symbol_b == key:
            value_b = value

    return value_a, value_b