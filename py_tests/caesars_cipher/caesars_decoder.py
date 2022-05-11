


message = 'LQKP OG CV GKIJV DA VJG BQQ'

#This version works with upper-case letters only.
#Caesar's cipher decoder with known shift:
def caesars_decoder(string, offset):
    out_string = str()
    for letter in range(0, len(string)):
        if string[letter] != " " and (ord(string[letter]) - offset) < 65:
            out_string += chr(ord(string[letter]) - offset + 26)
        elif string[letter] != " " and (ord(string[letter]) - offset) >= 65:
            out_string += chr(ord(string[letter]) - offset)
        else:
            out_string += string[letter]
    return out_string

#Function test:
print(caesars_decoder(message, 2))
