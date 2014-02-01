## doge “translator”: some observations thus far
- So, I feel like the following steps are important in the doge translation process:
  1. tokenize
    * we can probably use a simple sentence tokenizer, then a word tokenizer, since you wouldn't expect normal people to write long essays in instant messages, especially not a "dogechat" one, lulz.
    * a method of tokenization that retains *some* amount of punctuation is probably good. I haven't thought about what other punctuation might be good for yet, but it seems clear that question marks are extremely useful. Doge *does* tag questions, right?
  2. tag
    * NLTK's default POS tagger is trained on... WSJ data, apparently, which will clearly not be very helpful.
    * alright, so I trained a tagger on the NLTK NPS Chat corpus. I hope it's better.
  3. pick out nouns, verbs, and adjectives.
    * this is because afaik, most doge is done on just these 3 classes of words.
    * there are probably shittons of counterexamples that aren't coming to mind because
      1. I'm dumb
      2. It's 4.30am
    * but for a first pass this will probably work decently enough. there are probably far more serious problems elsewhere anyway.
  4. "chunk about said nouns, verbs, and adjectives."
    * WOW many buzzword wtf does this mean? idk man the idea here is that you'd like to be able to assemble things into phrases you know. the more I think about this the more uneasy I feel, as though I should have trained a phrase classifier or something of the sort in the previous step, but I don't know what I'm talking about anymore so I am going to do further investigation into this first.
  5. Find some way to determine "relative importance" to the content of the sentence (hahaha this is funny isn't it we're "translating: people's utterances into doge and talking about the "content of the sentence"???)
    * I'm also not so sure what I am talking about here, but I'll try to give an example in terms of my favourite sentence, "So I heard you like mudkips." (I realise things are misspelt here, yes.) For instance, here you'd (ok fine, I'd) want to generate the output "wow many mudkip much like", which drops the "heard", even though it's clearly a verb. this I hypothesise is because doges do not grasp the concept of reported speech. so we'll probably want to do something to remove verbs that are used for reported speech (I have no idea what, since all of them can unquestionably be used elsewhere too).
    * After removing the reported speech "heard" from consideration, you also need to reverse "mudkip" and "like". I haven't thought very hard about this, but I feel like in practically every <VERB> <OBJECT> sentence, the order of object and the verb should be swapped when translating to doge (but only for the first occurrence!)
  6. This was going to be "look up thesaurus and use simplest alternative", but I realised this is painful.
    * wordnik seems to work well, but it throws out so many synonyms, most of which would be completely wrong if substituted. To fix this we'd probably have to use wordnet's lexical distance evaluation or whatever, which sounds incredibly troublesome.
    * also, how the hell would we judge "simplest"?
  7. DEINFLECT THINGS. this one should be easy. I don't know why it's 7th instead of appearing earlier. Probably because I'm stupid.
  8. Dogeify by inserting "such" "much" "so" "very" "wow" "amaze" etc before the stuff that was already parsed out and reordered earlier.
    * This could be done really simply, but I feel like I at least want to draw them from a non-uniform distribution, because some of those words definitely should appear more than others.
    * Also, it would be nice to include something like "no", but this would involve detecting negative constructions in the original sentence then.
    * QUESTIONS?
    * The other thing is that you would like to lower the chance of something repeating
  9. "frequency analysis/training to figure out which constructs sound better." Don't be silly, this will never be done...

## Tag meaning examples
* ADJ adjective   new, good, high, special, big, local
* ADV adverb  really, already, still, early, now
* CNJ conjunction and, or, but, if, while, although
* DET determiner  the, a, some, most, every, no
* EX  existential there, there's
* FW  foreign word    dolce, ersatz, esprit, quo, maitre
* MOD modal verb  will, can, would, may, must, should
* N   noun    year, home, costs, time, education
* NP  proper noun Alison, Africa, April, Washington
* NUM number  twenty-four, fourth, 1991, 14:24
* PRO pronoun he, their, her, its, my, I, us
* P   preposition on, of, at, with, by, into, under
* TO  the word to to
* UH  interjection    ah, bang, ha, whee, hmpf, oops
* V   verb    is, has, get, do, make, see, run
* VD  past tense  said, took, told, made, asked
* VG  present participle  making, going, playing, working
* VN  past participle given, taken, begun, sung
* WH  wh determiner   who, which, when, what, where, how