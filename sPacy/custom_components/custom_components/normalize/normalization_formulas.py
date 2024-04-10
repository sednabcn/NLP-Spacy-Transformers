import os
import pandas as pd


from ..utils import normalize_formula, dataset_normalized


class Normalization:
                def __init__(self, data,path,column_name=None):
                    self.path_data=os.path.join(path,data)
                    self.column_name=column_name

                def get_dataset_normalized(self):
                      return dataset_normalized(self.path_data,self.column_name)

                  
                        
