#/usr/bin/python3
import spacy
import os
import custom_formulas_components
# Load English tokenizer, tagger, parser and NER

path_formulas=os.path.abspath("ner_formulas")
print(path_formulas)

nlp=spacy.load(path_formulas)

# Test
text="SUM ( Sepal Length ) AVG ( Sepal Length )"
print(text)
doc=nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)


# Test
text=" SORT ( [ Species ] , DESC ) "
print(text)
doc=nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)

# Test
text=" SORT ( [ Species ] , DESC ) INDEX ( ) < = 3 SORT BY [ Petal Length ] ASC"
print(text)
doc=nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
