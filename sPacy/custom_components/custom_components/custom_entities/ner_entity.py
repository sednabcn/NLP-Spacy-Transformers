import os
import spacy
import pandas as pd
from custom_components.custom_ner import custom_desc_components,custom_formulas_components
from custom_components.utils.utils import set_entity

class Custom_ner_entities:

         def __init__(self,data,path_ner_entity,column_name):
             self.data=data
             self.path_ner_entity=path_ner_entity
             self.column_name=column_name

         def get_entity(self):     
             return set_entity(self.data,self.column_name,self.path_ner_entity)
