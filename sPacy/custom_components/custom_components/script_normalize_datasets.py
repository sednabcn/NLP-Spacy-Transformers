import os
import pandas as pd
import custom_components
from custom_components.normalize.normalization_formulas import Normalization

# data in excel format !!Be careful
def get_normalization(path,data,name_col):
       return Normalization(path,data,name_col).get_dataset_normalized()
 
if __name__=='__main__':
     get_normalization('./datasets/','formulas.xlsx','Formula (Tableau)')
     get_normalization('./datasets/','formulas_test.xlsx','Formula (Tableau)')
     
