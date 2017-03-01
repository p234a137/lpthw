
# the scanner will take a string of raw input from a user and return a sentence that's composed of a list of tuples with the (TOKEN, WORD) pairings. If a word isn't part of the lexicon, then it should still return  the WORD but set the TOKEN to an error token. These error tokens will tell users they messed up.

directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop = ['the', 'in', 'from', 'at', 'it', 'of']
nouns = ['door', 'bear', 'princess', 'cabinet']


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(input_string):
    words = input_string.split()
    word_list = []
    for word in words:
        if word in directions:
            token = 'direction'
        elif word in verbs:
            token = 'verb'
        elif word in stop:
            token = 'stop'
        elif word in nouns:
            token = 'noun'
        elif convert_number(word) != None:
            token = 'number'
            word = convert_number(word) # this is inefficient, calling convert_number twice
        else:
            token = 'error'
        word_list.append((token, word))
    return word_list

