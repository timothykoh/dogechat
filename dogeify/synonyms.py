#depends on wnconfig.py, which I am not committing to the git repo

from wordnik import *
import wnconfig as config

client = swagger.ApiClient(config.key, config.url)
wa = WordApi.WordApi(client)

#takes in a POS as tagged by the POS tagger and returns a string that (hopefully) wordnik likes
# wow this was going to be beautiful but it turns out wordnik doesn't (yet) support
# parts of speech for the synonyms. gg this is going to turn out horribly :O
# def get_pos(pos):
#     if pos == "V" or pos == "VD" or pos == "VG" or pos == "VN":
#         return 

def get_synonyms(word, pos): #silently discard pos... for now?
    return wa.getRelatedWords(word, relationshipTypes='synonym', limitPerRelationshipType=1000)

#wow it actually returns pretty terrible synonyms. we'd probably have to run them through wordnet's similarity checks if we actually wanted to use them.