
VOWELS = "aeiou"

def get_word():
    orig_word = input("Input word: ")
    return orig_word

def word_to_piglatin(orig_word):
    orig_word = orig_word.lower()
    if(orig_word[0] in VOWELS ):
        pig_latin_word = orig_word + "way"
    elif(orig_word[0].isalpha() ):
        pig_latin_word = orig_word[1:] + orig_word[0] + "ay"
    else:
        pig_latin_word = "Error"
    return pig_latin_word


if __name__ == "__main__":
    the_word = get_word()
    pig_latin_word = word_to_piglatin(the_word)
    print(pig_latin_word)