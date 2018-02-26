import json
from difflib import get_close_matches

words = json.load(open('/Users/Kumaran/PycharmProjects/project1/MegaPython/Dictionary App/dict.json'))

def translate(w):
    wc = w.capitalize()
    w = w.lower()
    if w in words:
        return words[w]
    elif wc in words:
        return words[wc]
    elif len(get_close_matches(w, words.keys())) > 0:
            yn = input('Did you mean this %s word?, enter Y for yes or N for no: ' % get_close_matches(w, words.keys())[0])
            if yn == 'Y':
                return words[get_close_matches(w, words.keys())[0]]
            elif yn == 'N':
                return 'Word not found in the dictionary'
            else:
                return 'We could not recognise the input'
    else:
        return 'Word not found in the dictionary'


w = input('Enter a word: ')
output = translate(w)
if type(output) is list:
    for e in output:
        print('\n', e, '\n')
else:
    print(output,'\n')

