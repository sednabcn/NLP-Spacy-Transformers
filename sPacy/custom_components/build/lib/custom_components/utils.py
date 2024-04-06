# Functions to use to get tokens and components
#normalize_formula,get_pos_,get_patterns,create_ruler, preproc_ent,tok_formulas
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize,wordpunct_tokenize
nltk.download('punkt')
import pandas as pd
import spacy
from spacy.pipeline import EntityRuler
nlp = spacy.load("en_core_web_sm")

# Funtion to normalize data to allow get the token more easily
def normalize_formula(text):
    
    # Add space after function names if missing
    text = re.sub(r"(\w)\(", r"\1 (", text)
    # Ensure there's a space before and after parentheses
    text = re.sub(r"\s*\(\s*", " ( ", text)
    text = re.sub(r"\s*\)\s*", " ) ", text)
    # Ensure there's a space before and after square brackets
    text = re.sub(r"\s*\[\s*", " [ ", text)
    text = re.sub(r"\s*\]\s*", " ] ", text)
    # Ensure there's a space before and after curly brackets
    text = re.sub(r"\s*\{\s*", " { ", text)
    text = re.sub(r"\s*\}\s*", " } ", text)
    # Ensure there's a space before and after comparison symbols
    text = re.sub(r"\s*\==\s*", " == ", text)
    text = re.sub(r"(?<!\=)\s*\=\s*(?!=)", " = ", text)
    text = re.sub(r"\s*\>=\s*", " >= ", text)
    text = re.sub(r"\s*\<=\s*", " <= ", text)
    text = re.sub(r"\s*\>\s*", " > ", text)
    text = re.sub(r"\s*\<\s*", " < ", text)
    # Ensure there's a space before and after interrogative/exclamative symbols
    text = re.sub(r"\s*\?\s*", " ? ", text)
    text = re.sub(r"\s*\!\s*", " ! ", text)

    return text

# Function to get the position of each token
def get_pos_(data,col_name):
  dd=[]
  gg=[]

  for tok in data[col_name]:

          for ent in nlp(str(list(str(tok).split()))):
              # checking text between punct
              dd.append({ent.text:ent.pos_})
              gg.append({ent.pos_:ent.text})
  return dd,gg

# Function to get patterns based on the tokenization
def get_patterns(data,col_name):
     dt,dp=get_pos_(data,col_name)

     pos_=[list(item.keys())[0] for item in dp]
     pos_=list(set(pos_))
     #print(dt)
     #print(col_name,":",pos_)
     patterns={}
     patterns_head=[]
     for key in pos_:
         patterns.update({key:list(set([d[key] for d in dp if  key==list(d.keys())[0] and d[key] not in data["stopwords"]]))})
     return patterns

 # Function to create and return an EntityRuler with specified patterns
def create_ruler(patterns, label):
    nlp = spacy.load("en_core_web_sm")
    ruler = EntityRuler(nlp, overwrite_ents=True)
    formatted_patterns = [{"label": label, "pattern": pattern} for pattern in patterns]
    ruler.add_patterns(formatted_patterns)
    return ruler


# Function to transform data 
def preproc_ent(path_data,stopwords,train='True'):

     # Check the format file endswith "xlsx" or "xls" or "csv"
     df=pd.read_excel(path_data)
     # normalize data
     df[df.columns[1]]=df[df.columns[1]].apply(lambda x:normalize_formula(x))
     if train:          
         out_d={}
         out_f={}
         # Tokenize data
         dg_tok=df.apply(lambda x:[wordpunct_tokenize(y) for y in x])
         dg_tok=dg_tok.rename(columns=lambda x:"Tokenized " + x)
         dg_tok=dg_tok.loc[:,dg_tok.columns[[0,1]]]
         dg_tok.rename(columns=lambda x:x.strip(), inplace=True)
         #Form dictionaries
         out_d['stopwords']=stopwords
         out_f['stopwords']=stopwords
         out_d['text']=[sentence for sentence in df[df.columns[0]]]
         out_f['text']=[sentence for sentence in df[df.columns[1]]]
         out_d['vocab']=list(set([word  for ii in range(len(dg_tok[dg_tok.columns[0]])) for word  in dg_tok[dg_tok.columns[0]][ii] if word not in out_d['stopwords']]))
         out_f['vocab']=list(set([word  for ii in range(len(dg_tok[dg_tok.columns[1]])) for word  in dg_tok[dg_tok.columns[1]][ii] if word not in out_f['stopwords']]))
     if train:
         return out_d, out_f
     else:
         return df

# Functions to tokenize formulas sentences with symbols and get the operators
def tok_formulas(path_data,not_oper):
                 import re
                 patterns='\(| = | >= | > | \[ | \) | \{ | \]'
                 # Check the format file endswith "xlsx" or "xls" or "csv"
                 df=pd.read_excel(path_data)
                 tr_0=[]
                 for tr in df[df.columns[1]]:
                        try:
                          it0,it1=re.split(patterns,tr)[0:2]
                        except:
                           it0=re.split(patterns,tr)[0:2][0]

                        it01=it0.split()

                        if len(it01)==1:
                              iten=it01[0]
                        elif len(it01)==2:
                               iten=it01[0] +' '+ it01[1]
                        else:
                               iten=''
                               for item in it01:
                                    if item not in tr_0 and item not in not_oper:
                                            iten+=item +' '
                               iten=iten.rstrip()
                               #print(it01,'-->',iten)

                        if iten not in tr_0 and iten not in not_oper:
                               #print(it01)
                               tr_0.append(iten)
                 return tr_0

 
