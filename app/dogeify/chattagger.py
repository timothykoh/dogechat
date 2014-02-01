import nltk
import pickle
# nltk.data.path.append('./nltk_data')

# tagger = nltk.data.load('taggers/nps_chat_NaiveBayes_ubt.pickle')
with open('taggers/nps_chat_NaiveBayes_ubt.pickle') as f:
    tagger = pickle.load(f)
# tagger = nltk.data.load('taggers/nps_chat_ubt.pickle')

def _simplify_tags(wut):
    return [(word, nltk.tag.simplify_wsj_tag(tag)) for (word, tag) in wut]

#given some text, returns simplified tags
def get_tags(text):
    result = []
    def get_sentence_tags(sentence):
        return _simplify_tags(tagger.tag(nltk.word_tokenize(sentence)))

    for sentence in nltk.sent_tokenize(text):
        result.append(get_sentence_tags(sentence))

    return [item for sublist in result for item in sublist]

# cats
# rainbows
# basically anything that didn't occur in the chat corpus I'm guessing
# if you don't use bayesian, it just doesn't guess anything for these. which is "better"?