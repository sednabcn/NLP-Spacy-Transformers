import os
import pandas as pd


from custom_components.utils.utils import normalize_formula, dataset_normalized


class Normalization:
                def __init__(self,path_,data,column_name=None):
                    self.path_data=os.path.join(path_,data)
                    self.column_name=column_name

                def get_dataset_normalized(self):
                      return dataset_normalized(self.path_data,self.column_name)
      
                  
                        
