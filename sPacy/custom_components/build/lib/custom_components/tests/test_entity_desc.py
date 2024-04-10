import spacy
import os
import custom_desc_components
from custom_components.custom_entities.ner_entity import Custom_ner_entities

# Load ner_desc English tokenizer, tagger, parser and NER
path_ner=os.path.abspath('ner_desc')
print(path_ner)
nlp=spacy.load(path_ner)
path_data=os.path.abspath('formulas_nor.xlsx')
path_data_t=os.path.abspath('formulas_test_nor.xlsx')
name_col='Description'

 
# Train
ent_desc, Train_desc_data=Custom_ner_entities(path_data,path_ner,column_name).get_entity()

print(ent_desc)

for item in Training_desc_data:
     print(item)

# Test
ent_test_desc, Test_desc_data=Custom_ner_entities(path_data_t,path_ner,column_name).get_entity()

print(ent_test_desc)

for item in Test_desc_data:
    print(item)

# save to disk
path='~/Downloads/GEN_AI/PROJECTS/TABLEAU_FORMULAS/FORMULAS/custom_components/'
#Train
save_spacy_training_data(path,Train_desc_data,"Train_desc_data","ner_desc")
save_spacy_training_data_to_json(path,Train_desc_data,"Train_desc_data")
#Test
save_spacy_training_data(path,Test_desc_data,"Test_desc_data","ner_desc")
save_spacy_training_data_to_json(path,Test_desc_data,"Test_desc_data")
