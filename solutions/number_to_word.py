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
					
					
#Alternate and re-factored solution: @nandaa

def num_to_word(num):
  num = str(num)
  words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 
           'Six','Seven', 'Eight', 'Nine']
  for i in num:
    
    print words[int(i)] + " ",


#print num_to_word(488833)
#print num_to_word(438483478)




