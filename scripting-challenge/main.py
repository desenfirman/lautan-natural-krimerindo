import sys

BASIC_NUMBER_WORD = [
    "",
    "satu",
    "dua",
    "tiga",
    "empat",
    "lima",
    "enam",
    "tujuh",
    "delapan",
    "sembilan",
    "sepuluh",
    "sebelas"
]


def get_literal_number_less_than_m(number: int):
    """
    input param:
        number (int): a number representation in integer
    returns:
        string: a string representation of number
    """
    if number == 0:
        return 'nol'

    words = []
    # STEP 1: translate all hundreds first in every thousands
    while number != 0:
        word = []
        proc_number = number % 1000
        if proc_number % 100 > 0:
            below_hundreds = proc_number % 100
            tens = below_hundreds // 10
            ones = below_hundreds % 10
            if below_hundreds < 12:
                word.append(f"{BASIC_NUMBER_WORD[below_hundreds]}")
            elif below_hundreds < 20:
                word.append(f"{BASIC_NUMBER_WORD[ones]} belas")
            else:
                if ones > 0:
                    word.append(f"{BASIC_NUMBER_WORD[ones]}")
                word.append(f"{BASIC_NUMBER_WORD[tens]} puluh")

        if proc_number >= 100:
            hundreds = proc_number // 100
            if hundreds == 1:
                word.append('seratus')
            elif hundreds > 1:
                word.append(f"{BASIC_NUMBER_WORD[hundreds]} ratus")

        words.append(' '.join(reversed(word)))
        number //= 1000


    # STEP 2: find the thousands and millions
    final_word = []
    for i in range(len(words)):
        inv_i = len(words) - 1 - i
        if words[inv_i] == '':
            continue
        if inv_i == 0:
            final_word.append(words[inv_i])
        elif inv_i == 1:
            if words[inv_i] == 'satu':
                final_word.append('seribu')
            else:
                final_word.append(words[inv_i])
                final_word.append('ribu')
        else:
            final_word.append(words[inv_i])
            final_word.append('juta')

    if final_word[-1] == ' ':
        final_word = final_word[:-1]
    return ' '.join(final_word)


if __name__ == "__main__":
    """
    input param:
        number (stdin): a number representation that less than 999.999.999
    output type:
        literal_number (stdout):  a literal representation from a number. 
        print warning exception of number is more than 999.999.999
    """
    try:
        n = int(input())
        for _ in range(n):
            number = int(input())
            if number > 999999999:
                print('Number should be less than 999.999.999')
            print(f"{number}: {get_literal_number_less_than_m(number)}")
    except Exception as e:
        print(e.args)
