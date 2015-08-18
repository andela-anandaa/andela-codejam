relation = {
    0: 'zero',
    1:'one',
    2: 'two',
    3:'three',
    4: 'four',
    5:'five',
    6: 'six',
    7:'seven',
    8: 'eight',
    9:'nine',
    10: 'ten'
};


def num_to_word(number):
        number = str(number)
        x = map(int,number)
        for val in x:
            for d in relation:
                if val == d:
                    print relation[d],





print num_to_word(438483478)




