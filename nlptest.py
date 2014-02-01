import nltk
#fuck I don't know how to do this man
#1) tokenize
#2) tag
#3) pick out nouns and verbs
#4) chunk about said nouns and verbs
#5) maybe find some way to evaluate "relative importance" to the sentence
#6) look up simpler versions of chunked phrases, substitute
#7) dogeify by inserting "such" "much" "so" "very" "wow" "amaze" etc
#7b) do some sort of frequency analysis/training to figure out which constructs "sound better"

document = "so I heard you like mudkips"
#wow this sentence presents problems
#e.g. the canonical spelling of "like" in this sentence would present problems
#also I'd want to turn it into something like "wow many mudkip much liek" which involves reordering of the words. HOW???