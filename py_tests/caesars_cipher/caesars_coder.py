


message = 'JOIN ME AT EIGHT BY THE ZOO'

#This version works with upper-case letters only.
#Caesar's cipher coder:
def caesars_coder(string, offset):
    out_string = str()
    for letter in range(0, len(string)):
        if string[letter] != " " and (ord(string[letter]) + offset) < 91:
            out_string += chr(ord(string[letter]) + offset)
        elif string[letter] != " " and (ord(string[letter]) + offset) >= 91:
            out_string += chr(ord(string[letter]) + offset - 26)
        else:
            out_string += string[letter]
    return out_string

#Function test:
print(caesars_coder(message, 2))