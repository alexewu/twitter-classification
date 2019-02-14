from __future__ import unicode_literals
from spacy.vectors import Vectors
import spacy

#nlp = spacy.load('en')
nlp = spacy.load('en_vectors_web_lg')


tokens = nlp(u'dog cat banana')

data = []
for token1 in tokens:
    row = []
    row.append(token1.text)
    for token2 in tokens:
        row.append(token1.similarity(token2))
    data.append(row)
        #print(token1.text, token2.text, token1.similarity(token2))

# empty_vectors = Vectors(shape=(10000, 300))
#
# data = numpy.zeros((3, 300), dtype='f')
# keys = [u'cat', u'dog', u'rat']
# vectors = Vectors(data=data, keys=keys)
# for row in data:
#     for val in row:
#         print '{:4}'.format(val),
#     print

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in data]))
