import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

from pyresparser.utils import extract_name
doc = nlp("My name is John Doe")
print(extract_name(doc, matcher))

