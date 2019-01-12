
def get_input():
    roman_numeral = input("Input roman numeral: ")
    return roman_numeral

def to_value(letter):
    if letter == "I": return 1
    elif letter == "V": return 5
    elif letter == "X": return 10
    elif letter == "L": return 50
    elif letter == "C": return 100
    elif letter == "M": return 1000


def roman_num_to_arabic_num(roman_numeral):
    total = 0 
    previous = 0
    roman_numeral = roman_numeral.upper()

    for letter in roman_numeral:
        current = to_value(letter)
        if previous < current:
            total -= previous
            current -= previous
        total += current
        previous = current
    return total


if __name__ == "__main__":
    roman_numeral = get_input()
    #roman_numeral = "xvi"
    arabic_number = roman_num_to_arabic_num(roman_numeral)
    print(arabic_number)