import os
import pandas as pd
import custom_components
from custom_components.custom_ner.ruler_desc import Custom_ner_desc_component
from custom_components.custom_ner.ruler_formulas import Custom_ner_formulas_component

def get_ner_component(path_entity_name,option):

    if option=="S":
       return Custom_ner_desc_component(path_entity_name).get_entity_ruler()   
    elif option=="F":
       return Custom_ner_formulas_component(path_entity_name).get_entity_ruler() 
    else:
        pass

if __name__=='__main__':
     get_ner_component('ner_desc','S')
     get_ner_component('ner_formulas','F')
     
