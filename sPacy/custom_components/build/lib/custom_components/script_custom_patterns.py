import os
import pandas as pd
import custom_components
from custom_components.patterns.generation import Generation_custom_patterns
stopwords=[]

def patterns_gen(data,ind):
    
    if ind=="S" :
        stopwords= ['\\','Iri','Se','C','Sepal','ica','Length',"'s",'.',"'", 's', 'a','(',')','Petal','Distinct',"Width",',',"'","[","]"]     
    elif ind=="F": 
        stopwords=['\\','Iri','Se','C','Sepal','ica','Length',"'s",'.',"'", 's', 'a','(',')','Petal','Distinct','distinct',"Width",',','BY','by','from',"[","]"]
    else:
        pass
    return Generation_custom_patterns(data,stopwords,option).gen_custom_patterns()

if __name__=='__main__':
      PATH='~/Downloads/GEN_AI/PROJECTS/TABLEAU_POWERBI/FORMULAS/'
      path_data=os.path.join(PATH,"formulas.xlsx")
      option="F"
      patterns_gen(path_data,option)
