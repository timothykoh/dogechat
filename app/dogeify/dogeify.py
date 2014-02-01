import nltk
import chattagger as tagger
import random
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer

lmt = WordNetLemmatizer()
stm = PorterStemmer()

#we probably should have a list of adverbs to filter out, and #1 on it should be "really".

#first things first: DO NOT REPEAT
doge_words = ["much", "such", "very", "so", "many"]
doge_weights = [4,3,3,2,2]
wnt = {'N':'n', 'NP':'n', 'ADJ':'a', 'ADV':'r', 'V':'v', 'VD':'v', 'VG':'v', 'VN':'v', 'FW':'n', 'UH':'n'}
used = set()

def weighted_choice(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i

class DogeWord:
    def __init__(self):
        self.prev_choice = None

    def __call__(self):
        temp = doge_words[weighted_choice(doge_weights)]
        while temp == self.prev_choice:
            temp = doge_words[weighted_choice(doge_weights)]

        self.prev_choice = temp
        return temp

_get_doge_word = DogeWord()

def _to_stem(word, tag):
    return lmt.lemmatize(word, wnt[tag])

def to_doge(text):
    result = ["wow"]
    tags = tagger.get_tags(text)
    # print tags
    def much_want(tag):
        if tag == 'ADJ' or tag == 'ADV' or tag == 'FW' or tag == 'N'\
        or tag == 'UH' or tag == 'V' or tag == 'VD' or tag == 'VG'\
        or tag == 'VN' or tag == 'NP':
            return True
        else:
            return False

    #must update set, cannot use list comprehension anymore
    # after = [_to_stem(word, tag) for word, tag in tags if much_want(tag)]
    after = []
    for word, tag in tags:
        if much_want(tag) and word not in used:
            used.add(word)
            after.append(_to_stem(word, tag))

    for word in after:
        if word[0] == "'":
            continue
        result.append(' '.join([_get_doge_word(), word]))

    return result

#definitely needs a pass through to filter out verbs to the right of pronouns?
#(that is an absolutely dreadful way of doing this but dammit I don't want to
# construct an english grammar...) (and also don't know how to)
#actually no that totally doesn't work. there are plenty of legit reasons to have V to right of PRO
#only keep adjectives if they're like a "basic form" already

#just go through list. where you see PRO, get rid of words after it until you see a V, or
#??? I forgot
#unless list is already "too short"