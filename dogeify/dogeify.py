import nltk
import chattagger as tagger
import random
from nltk.stem.wordnet import WordNetLemmatizer

lmt = WordNetLemmatizer()

doge_words = ["such", "much", "so", "very"]

def to_stem(word):
    return lmt.lemmatize(word)

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

    after = [to_stem(word) for word, tag in tags if much_want(tag)]

    for word in after:
        result.append(' '.join([random.choice(doge_words), word]))

    return result

#definitely needs a pass through to filter out verbs to the right of pronouns?
#(that is an absolutely dreadful way of doing this but dammit I don't want to
# construct an english grammar...)