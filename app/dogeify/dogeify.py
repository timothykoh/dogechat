import nltk
import chattagger as tagger
import random
from nltk.stem.wordnet import WordNetLemmatizer

lmt = WordNetLemmatizer()

#first things first: DO NOT REPEAT
doge_words = ["such", "much", "so", "very", "many"]
wnt = {'N':'n', 'NP':'n', 'ADJ':'a', 'ADV':'r', 'V':'v', 'VD':'v', 'VG':'v', 'VN':'v', 'FW':'n', 'UH':'n'}

class DogeWord:
    def __init__(self):
        self.prev_choice = None

    def __call__(self):
        temp = random.choice(doge_words)
        while temp == self.prev_choice:
            temp = random.choice(doge_words)
        self.prev_choice = temp
        return temp

get_doge_word = DogeWord()

def to_stem(word, tag):
    # print word
    return lmt.lemmatize(word, wnt[tag])

def to_doge(text):
    result = ["wow"]
    tags = tagger.get_tags(text)
    def much_want(tag):
        if tag == 'ADJ' or tag == 'ADV' or tag == 'FW' or tag == 'N'\
        or tag == 'UH' or tag == 'V' or tag == 'VD' or tag == 'VG'\
        or tag == 'VN' or tag == 'NP':
            return True
        else:
            return False

    after = [to_stem(word, tag) for word, tag in tags if much_want(tag)]

    for word in after:
        if word[0] == "'":
            continue
        result.append(' '.join([get_doge_word(), word]))

    return result

#definitely needs a pass through to filter out verbs to the right of pronouns?
#(that is an absolutely dreadful way of doing this but dammit I don't want to
# construct an english grammar...)
#lemmatizer doesn't expand abbreviations.
#only keep adjectives if they're like a "basic form" already

#just go through list. where you see PRO, get rid of words after it until you see a V, or
#??? I forgot
#unless list is already "too short"