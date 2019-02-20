from __future__ import unicode_literals
#from spacy.vectors import Vectors
import spacy

#nlp = spacy.load('en')
nlp = spacy.load('en_vectors_web_lg')


tokens = nlp(u'RT @SOTTnet: Earth Changes: Aerial footage of devastating Colorado floods: Aerial footage shows the scale of destruction ca... http://t.co/\u2026')

data = []
for token1 in tokens:
    row = []
    value = 0 #the sum of similarities with other words in the bag
    row.append(token1.text)
    for token2 in tokens:
        value += token1.similarity(token2)
    row.append(value)
    data.append(row)

text_file = open("post.txt", "w")
for row in data:
    text_file.write("%s %f\n" % (row[0], row[1]))
text_file.close()
