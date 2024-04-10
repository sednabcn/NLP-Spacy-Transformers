#/usr/bin/python3
import spacy
import os
import custom_formulas_components
from custom_components.custom_entities.ner_entity import Custom_ner_entities

# Load English tokenizer, tagger, parser and NER

path_formulas=os.path.abspath("ner_formulas")
print(path_formulas)
nlp=spacy.load(path_formulas)
path_data=os.path.abspath('formulas_nor.xlsx')
path_data_t=os.path.abspath('formulas_test_nor.xlsx')
name_col='Formula (Tableau)'
 
# Train
ent_formulas, Train_formulas_data=Custom_ner_entities(path_data,path_formulas,column_name).get_entity()

print(ent_formulas)

for item in Training_formulas_data:
     print(item)

# Test
ent_test_formulas, Test_formulas_data=Custom_ner_entities(path_data_t,path_formulas,column_name).get_entity()

print(ent_test_formulas)

for item in Test_formulas_data:
    print(item)

# save to disk
path='~/Downloads/GEN_AI/PROJECTS/TABLEAU_FORMULAS/FORMULAS/custom_components/'
#Train
save_spacy_training_data(path,Train_formulas_data,"Train_formulas_data","ner_formulas")
save_spacy_training_data_to_json(path,Train_formulas_data,"Train_formulas_data")
#Test
save_spacy_training_data(path,Test_formulas_data,"Test_formulas_data","ner_formulas")
save_spacy_training_data_to_json(path,Test_formulas_data,"Test_formulas_data")
