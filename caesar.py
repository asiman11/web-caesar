import string

def encrypt(text, rot):
    enctext = ""
    for letter1 in text:
        enctext += rotate_character(letter1, rot)
    return enctext
def alphabet_position(letter):
    if letter in string.ascii_lowercase:
        pos = string.ascii_lowercase.find(letter)
    elif letter in string.ascii_uppercase:
        pos = string.ascii_uppercase.find(letter)
    return pos

def rotate_character(char, rot):
    if char in string.ascii_lowercase:
        newchar = string.ascii_lowercase[(alphabet_position(char)+rot)%26] #rotate lowercase
    elif char in string.ascii_uppercase:
        newchar = string.ascii_uppercase[(alphabet_position(char)+rot)%26] #rotate uppercase
    else:
        newchar = char
    return newchar