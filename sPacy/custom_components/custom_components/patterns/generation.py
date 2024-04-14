
import os
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import re
import spacy
from nltk.tokenize import word_tokenize, sent_tokenize,wordpunct_tokenize

from spacy import displacy
from spacy.matcher import matcher
from spacy.tokens import span
from spacy.language import Language
from spacy.pipeline import EntityRuler
from custom_components.utils.utils import normalize_formula, preproc_ent,tok_formulas,get_pos_,get_patterns


nltk.download('punkt')

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


class Generation_custom_patterns:
       def __init__(self, path_data,stopwords,option,train=True):
           self.data=path_data
           self.stopwords=[]
           for  x in stopwords:
                  self.stopwords.append(x)
           self.train=train
           self.option=option #option="S","F"

       def gen_custom_patterns(self):
              
              out_d,out_f= preproc_ent(self.data,self.stopwords)

              if self.option=="S":
                     p_d=get_patterns(out_d,"vocab")
             
                     # patterns to description
                     desc_conj=p_d['CCONJ']+ p_d['SCONJ']
                     desc_intj=p_d['INTJ']
                     desc_verb=p_d['VERB'] + p_d['AUX']
                     desc_num=p_d['NUM']
                     desc_adv=p_d['ADV']
                     desc_pron=p_d['PRON'] + p_d['DET']
                     desc_adp=p_d['ADP']
                     desc_noun=[x for x in p_d['X'] if x != p_d['X'][1]]+p_d['NOUN'] +['dataset']
                     desc_adj=[p_d['X'][1]]+[x for x in p_d['ADJ'] if x !='dataset' ]
                     desc_propn=['Sepal Length','Sepal Width', 'Petal Length', 'Petal Width']+p_d['PROPN']
                     return print(desc_conj,'\n',desc_intj,'\n',desc_verb,'\n',desc_num,'\n',desc_adv,'\n',desc_pron,'\n',desc_adp,'\n',desc_noun,'\n',desc_adj,'\n',desc_propn)

              elif self.option=="F":
                     p_t=get_patterns(out_f,"vocab")
                     
                     p_t['ARG']=['[Sepal Length]','[Sepal Width]','[Petal Length]','[Petal Width]', '[Species]']
                     p_t['ARGN']=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']
                     p_t['NOUN'] =['month', 'TODAY', 'color','YEAR','versicolor','setosa','year','virginica']
                     p_t['STOPWORDS']=['[Sepal','Sepal','[Petal','Width]','Width','Petal','Length]',"'Se'",':','"virginica",'"setosa",'','{',')','*',"'Setosa'","'month', ",'4.0 AND','"setosa" AND','ica',"Iri",'!= 3.0','"versicolor" AND',"Species STARTS WITH 'Se'","Length",'"Iri"' ]
                     p_t['NUM']=[ff  for ff in p_t['NUM'] if ff !='TOP']+['1.5','2.5','4.5','3.0','3','2.0','5.0']
                     p_t['ADP']+=['to','AND','>=','<','!=','<=','=','>']
                     p_t['ADV']=[ff for ff in p_t["ADV"] if ff!="SORT"] + ['highest to lowest','ASC','DESC','NULL','LEFT']
                     p_t['ADJ']=[ff for ff in p_t['ADJ'] if  ff!='SORTED']
                     ptt=p_t['ARG']+p_t['NOUN']+p_t['NUM'] + p_t['STOPWORDS'] + p_t['ARGN'] + p_t['ADV'] + p_t['ADP']+p_t['ADJ']
                     p_t['OPER']=['STARTS WITH']
                     p_t['OPER']+=tok_formulas(self.data,ptt)
                     p_t['OPER'][p_t['OPER'].index('LISTED')]='LISTED FROM'
                     p_t['OPER'][p_t['OPER'].index('TOP BY')]='TOP'
                     p_t['OPER']+=['IF CONTAINS','BY']
                     p_t['NOUN']=[ff for ff in p_t['NOUN'] if ff not in p_t['OPER']]

                     # patterns to formulas
                     oper_arg=p_t['ARG']
                     oper_argn=p_t['ARGN']
                     oper_numm=p_t['NUM']
                     oper_advv=p_t['ADV']
                     oper_oper=p_t['OPER']
                     oper_adpp=p_t['ADP']
                     oper_nounn=p_t['NOUN']
                     oper_adjj=p_t['ADJ']

                     return print(oper_arg,'\n',oper_argn,'\n',oper_numm,'\n',oper_advv,'\n',oper_oper,'\n',oper_adpp,'\n',oper_nounn,'\n',oper_adjj)
              else:
                     pass
