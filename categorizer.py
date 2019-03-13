from __future__ import unicode_literals
from spacy.pipeline import TextCategorizer
from spacy.vocab import Vocab
import spacy
import thinc

nlp = spacy.load('en')
textcat = TextCategorizer(nlp.vocab)
textcat.from_disk('/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification')

