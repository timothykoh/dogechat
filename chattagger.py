import pickle

with open('taggers/nps_chat_NaiveBayes_ubt.pickle') as f:
    tagger = pickle.load(f)
