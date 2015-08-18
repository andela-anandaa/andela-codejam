relation = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
};

def num_to_word(number):
        number = str(number)
        for val in number:
            print relation[int(val)],


#Alternate and re-factored solution: @nandaa

def num_to_word2(num):
  num = str(num)
  words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five',
           'Six','Seven', 'Eight', 'Nine']
  for i in num:

    print words[int(i)] + " ",
#loop removed 
def num_to_word3(num):
    num = str(num)

    key = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    word = [key[int(i)] for i in num]

    return " ".join(word)

#print num_to_word3(8983434)


#print num_to_word2(488833)
#print num_to_word(438483478)

#the None type output removed refactored...
def num_to_word(num):
  num = str(num)
  words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 
		   'Six','Seven', 'Eight', 'Nine']
  result = []
  for i in num:
    result.append(words[int(i)] + " ",)
  
  return(", ".join(result))
  
  