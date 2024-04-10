import os
import pandas as pd
import custom_components
from custom_components.custom_entities.ner_entity import Custom_ner_entities
from custom_components.tests import custom_desc_components, custom_formulas_components

def get_ner_entity(path_data,path_entity_name,column_name):
       return Custom_ner_entities(path_data,path_entity_name,column_name).get_entity()   

if __name__=='__main__':
    
     ent_desc,Train_desc_data=get_ner_entity('formulas_nor.xlsx','ner_desc','Description')
     ent_formulas, Train_formulas_data=get_ner_entity('formulas_nor.xlsx','ner_formulas','Formula (Tableau)')
     ent_test_desc,Test_desc_data=get_ner_entity('formulas_test_nor.xlsx','ner_desc','Description')
     ent_test_formulas, Test_formulas_data=get_ner_entity('formulas_test_nor.xlsx','ner_formulas','Formula (Tableau)')
     
     
