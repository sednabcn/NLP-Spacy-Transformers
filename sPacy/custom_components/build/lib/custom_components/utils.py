# Functions to use to get tokens and components
#make_predictions, evaluate_the_model, save_model,save_spacy_training_data, upload_spacy_training_data,save_spacy_training_data_to_json, upload_spacy_training_data_from_json,normalize_formula, dataset_normalized, get_pos_,get_patterns,set_entity,create_ruler, preproc_ent,tok_formulas
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize,wordpunct_tokenize
nltk.download('punkt')
import pandas as pd
import spacy
from spacy.pipeline import EntityRuler
nlp = spacy.load("en_core_web_sm")

def make_predictions(model_path,texts,option=1):
    import spacy
    from spacy import displacy
    """
    options:
    1-print
    else-displacy ents
    """
    # Replace 'your_model_directory' with the path to your trained model
    nlp = spacy.load(model_path)
    print(nlp.pipe_names)
    if isinstance(texts,type)=='list' and option==1:
         for doc in nlp.pipe(texts):
              print([(ent.text, ent.label_) for ent in doc.ents])
    elif isinstance(texts,type)=='list' and option!=1:
         for doc in nlp.pipe(texts):
              displacy.render(doc, style="ent")
    elif isinstance(texts,type)!='list' and option==1:
          print(texts)
          # Process the text
          doc = nlp(texts)

          # Display the entities in the text
          for ent in doc.ents:
                 print(ent.text, ent.label_)
    else:
          print(texts)
          # Process the text
          doc = nlp(texts)
          displacy.render(doc, style="ent")

def evaluate_the_model(model_path, TEST_DATA):
    import spacy
    from spacy.training import Example

    nlp = spacy.load(model_path)

    # Convert test data to Example objects
    examples = []
    for text, annotations in TEST_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        examples.append(example)

    # Evaluate the model
    scores = nlp.evaluate(examples)
    return scores


def save_model(model_name,location):
   import os
   from pathlib import Path
   if location=='drive':
      from google.colab import drive
      drive.mount('/content/drive')
      # Define the base path for the folder where you want to save your model
      folder_path = '/content/drive/My Drive/MyModels'
   else:
      # Define the base path for the folder where you want to save your model
      folder_path = '/content/'

   # Create the folder if it doesn't exist
   os.makedirs(folder_path, exist_ok=True)
   model_path = os.path.join(folder_path, model_name)
   # Save the model to the specified directory in Google Drive
   nlp.to_disk(model_path)
   print(f'Model saved to: {model_path}')
   # Load the model to ensure it's been saved correctly
   nlp2 = spacy.load(model_path)


def save_spacy_training_data(output_dir,training_data,filename, model):
  import spacy
  from spacy.training import Example
  from spacy.tokens import DocBin

  # Load the spaCy model
  nlp = spacy.load(model)

  # Create the output directory if it doesn't exist
  os.makedirs(output_dir, exist_ok=True)


  # Convert the training data to spaCy Examples
  training_examples = []
  for text, annotations in training_data:
        # Process the text through the pipeline to create a Doc
        doc = nlp.make_doc(text)
        # Create an Example using the Doc and its annotations
        example = Example.from_dict(doc, annotations)
        training_examples.append(example)

  # Create a DocBin and add the examples
  doc_bin = DocBin(docs=[ex.reference for ex in training_examples],store_user_data=True)

  # Save the DocBin to disk
  doc_bin.to_disk(os.path.join(output_dir,filename +".spacy"))

def upload_spacy_training_data(input_dir,filename, model):
    import spacy
    from spacy.tokens import DocBin
    from pathlib import Path

    # Load the spaCy model
    nlp = spacy.load(model)

    # Define the file path
    file_path = Path(input_dir) / (filename + ".spacy")

    # Load the DocBin from the file
    doc_bin = DocBin().from_disk(file_path)

    # Extract docs from the DocBin
    docs = list(doc_bin.get_docs(nlp.vocab))

    # Assuming entity annotations are what you're interested in,
    # here's how you might retrieve entities from each doc
    training_data=[]
    for doc in docs:
        # Accessing the entities in each doc
        entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
        training_data.append((doc,{"entities":entities}))
    return training_data

"""# Save and Lod Spacy's Training Data in json format"""

def save_spacy_training_data_to_json(output_dir,training_data,filename):
    import json
    import os

    # file_path
    file_path=os.path.join(output_dir,filename +".json")
    # Save the training data to a JSON file
    with open(file_path, 'w', encoding='utf-8') as f:
      json.dump(training_data, f, ensure_ascii=False, indent=4)

def upload_spacy_training_data_from_json(input_dir,filename):
    import os
    import json
    # file_path
    file_path=os.path.join(input_dir,filename +".json")
    # Load the training data from a JSON file
    training_data=[]
    with open(file_path, 'r', encoding='utf-8') as f:
         loaded_training_data = json.load(f)

    for ii in range(len(loaded_training_data)):

           training_data.append(tuple(loaded_training_data[ii]))
    return training_data

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

# Function for the normalization the datasets with "FORMULAS"
def dataset_normalized(path_data,col_name):
     # Check the format file endswith "xlsx" or "xls" or "csv"
     df=pd.read_excel(path_data)
     # normalize data
     df[col_name]=df[col_name].apply(lambda x:normalize_formula(x))
     return df
 
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

# Function to get entities in the format (text, ent.start_char, ent.end_char, ent.label_) 
def set_entity(data,col_name,ner_entity):
     import spacy
     nlp=spacy.load(ner_entity)
     dd=[]
     dt=[]
     for text in data[col_name]:
          doc=nlp(text)
          dp=[text]
          dt_e={}
          dt_e["entities"]=[]
          for ent in doc.ents:
                    dp.append([ent.text,ent.label_])
                    dt_e["entities"].append((int(ent.start_char),int(ent.end_char),ent.label_))
          dt.append((text,dt_e))
          dd.append(dp)
     return dd,dt

 
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

# Functions to tokenize "FORMULAS" with symbols and get the operators
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

 
