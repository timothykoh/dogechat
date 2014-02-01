#what does nltk.classify do?
import nltk
from chattagger import tagger
#fuck I don't know how to do this man
#1) tokenize
#2) tag
#3) pick out nouns, verbs, and adjectives
#4) chunk about said nouns and verbs
#5) maybe find some way to evaluate "relative importance" to the sentence
#6) look up simpler versions of chunked phrases, substitute
#6b) oh yes deinflect things
#7) dogeify by inserting "such" "much" "so" "very" "wow" "amaze" etc
#7b) do some sort of frequency analysis/training to figure out which constructs "sound better"

sentence = "so I heard you like mudkips. this is dangerous."
document = 'What is the sentence? "The Jews are our affliction!"' #herp derp such friedrich
#wow this sentence presents problems
#e.g. the canonical spelling of "like" in this sentence would present problems
#also I'd want to turn it into something like "wow many mudkip much liek" which involves reordering of the words. HOW???

def simplify_tags(wut):
    return [(word, nltk.tag.simplify_wsj_tag(tag)) for (word, tag) in wut]

print simplify_tags(tagger.tag(nltk.word_tokenize(sentence)))

# Tag Meaning Examples
# ADJ adjective   new, good, high, special, big, local
# ADV adverb  really, already, still, early, now
# CNJ conjunction and, or, but, if, while, although
# DET determiner  the, a, some, most, every, no
# EX  existential there, there's
# FW  foreign word    dolce, ersatz, esprit, quo, maitre
# MOD modal verb  will, can, would, may, must, should
# N   noun    year, home, costs, time, education
# NP  proper noun Alison, Africa, April, Washington
# NUM number  twenty-four, fourth, 1991, 14:24
# PRO pronoun he, their, her, its, my, I, us
# P   preposition on, of, at, with, by, into, under
# TO  the word to to
# UH  interjection    ah, bang, ha, whee, hmpf, oops
# V   verb    is, has, get, do, make, see, run
# VD  past tense  said, took, told, made, asked
# VG  present participle  making, going, playing, working
# VN  past participle given, taken, begun, sung
# WH  wh determiner   who, which, when, what, where, how