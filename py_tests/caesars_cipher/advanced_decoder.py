


letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]

ords = []
for n in range(0, 128):
    ords.append(n)

upper_letters_ord = ords[65:91]
upper_letters_chr = []
for ul in upper_letters_ord:
    upper_letters_chr += chr(ul)


#Caesar's cipher decoder (using 'letter goodness'):

#You may try to use a given encoded message or use yours
#(uncomment 'string' and 'print(value_counter(string))' at the bottom.
#The main disadvantage of this method is that the shorter the message, the higher the error.
encoded_message = "LQKP OG CV GKIJV DA VJG BQQ"
#string = input("Enter the encoded message: ")

alphabet_dict = dict(zip(upper_letters_chr, letterGoodness))



#'roulette' + 'cassete' prints a list with all possibilities of decoded message:
def roulette(string, offset):
    out_string = str()
    for letter in range(0, len(string)):
        if string[letter] != " " and (ord(string[letter]) + offset) < 91:
            out_string += chr(ord(string[letter]) + offset)
        elif string[letter] != " " and (ord(string[letter]) + offset) >= 91:
            out_string += chr(ord(string[letter]) + offset - 26)
        else:
            out_string += string[letter]
    return out_string

def cassette(string):
    lst = []
    for offset in range(0, 26):
        lst.append(roulette(string, offset))
    return lst

#Function tests:
#print(cassette("HUD"))
#print(cassette(encoded_message))



def value_counter(string):
    lst = []
    for item in cassette(string):
        count = float()
        for letter in item:
            if letter != " ":
                count += alphabet_dict[letter]
            else:
                continue
        lst.append(count)
    return roulette(string, lst.index(max(lst)))

#'value_counter' tests:
print(value_counter(encoded_message))
#print(value_counter(string))