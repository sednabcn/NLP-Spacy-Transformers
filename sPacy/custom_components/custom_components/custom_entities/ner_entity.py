import os
import spacy
import pandas as pd
import custom_components
from custom_components.tests import custom_desc_components,custom_formulas_components


class Custom_ner_entities:

         def __init__(self,path_data,path_ner_entity,column_name):
             self.path_data=path_data
             self.path_ner_entity=path_ner_entity
             self.column_name=column_name

         def get_entity(self):
             return set_entity(self.path_data,self.column_name,self.path_ner_entity)
