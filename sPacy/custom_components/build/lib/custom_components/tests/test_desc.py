import spacy
import os
import custom_desc_components
# Load ner_desc English tokenizer, tagger, parser and NER
path_ner=os.path.abspath('ner_desc')
print(path_ner)
nlp=spacy.load(path_ner)

# Test
text="Sum of Sepal Length. Average Sepal Width across all entries . Count the number of records in the dataset"
print(text)
doc=nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
