#what does nltk.classify do?
import nltk
from chattagger import tagger

# sentence = "so I heard you like mudkips. this is dangerous."
sentence = 'I want you'
document = 'What is the sentence? "The Jews are our affliction!"' #herp derp such friedrich
#wow this sentence presents problems
#e.g. the canonical spelling of "like" in this sentence would present problems
#also I'd want to turn it into something like "wow many mudkip much liek" which involves reordering of the words. HOW???

def simplify_tags(wut):
    return [(word, nltk.tag.simplify_wsj_tag(tag)) for (word, tag) in wut]

print simplify_tags(tagger.tag(nltk.word_tokenize(sentence)))
