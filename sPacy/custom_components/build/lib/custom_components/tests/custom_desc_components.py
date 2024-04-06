import spacy
from spacy.language import Language
from spacy.pipeline import EntityRuler

from custom_components.utils import create_ruler
nlp = spacy.load("en_core_web_sm")
# Create rulers

# Create component factories
@Language.component("ruler_conj")
def ruler_conj_component(doc):
               desc_conj =['and', 'or', 'how', 'where', 'How'] 
               ruler_conj = create_ruler(desc_conj,'CONJ')       
               return ruler_conj(doc)

@Language.component("ruler_intj")
def ruler_intj_component(doc):
               desc_intj=['%'] 
               ruler_intj = create_ruler(desc_intj,'INTJ')
               return ruler_intj(doc)

@Language.component("ruler_verb")
def ruler_verb_component(doc):
               desc_verb=['contains', 'start', 'count', 'Show', 'sorted', 'Aggregate', 'Find', 'recorded', 'show', 'starting', 'ends', 'found', 'ascending', 'Organize', 'descending', 'grouped', 'Display', 'assuming', 'starts', 'are', 'is'] 
               ruler_verb = create_ruler(desc_verb,'VERB')
               return ruler_verb(doc)

@Language.component("ruler_num")
def ruler_num_component(doc):
               desc_num=['10', '1', '2', '3', '0', '5', '4'] 
               ruler_num  = create_ruler(desc_num,'NUM')
               return ruler_num(doc)
         
@Language.component("ruler_adv")
def ruler_adv_component(doc):
               desc_adv=['exactly', 'alphabetically', 'Sort', 'only']
               ruler_adv  = create_ruler(desc_adv,'ADV')
               return ruler_adv(doc)
         
@Language.component("ruler_pron")
def ruler_pron_component(doc):
               desc_pron=['all', 'each', 'both', 'there', 'this', 'What', 'the'] 
               ruler_pron = create_ruler(desc_pron,'PRON')
               return ruler_pron(doc)
         
@Language.component("ruler_adp")
def ruler_adp_component(doc):
               desc_adp=['than', 'at', 'above', 'with', 'by', 'within', 'between', 'over', 'across', 'for', 'from', 'in', 'of'] 
               ruler_adp  = create_ruler(desc_adp,'ADP')
               return ruler_adp(doc)

@Language.component("ruler_noun")
def ruler_noun_component(doc):
               desc_noun=['virginica', 'setosa', 'median', 'name', 'data', 'number', 'records', 'flower', 'Entries', 'points', 'versicolor', 'species', 'value', 'entries', 'order', 'observation', 'occurrences', 'types', 'Lengths', 'Number', 'field', 'year', 'Widths', 'color', 'month', 'List', 'flowers', 'Species', 'Determine', 'Sum', 'dataset'] 
               ruler_noun = create_ruler(desc_noun, "NOUN")
               return ruler_noun(doc)
         
@Language.component("ruler_adj")
def ruler_adj_component(doc):
               desc_adj=['10th', 'highest', 'average', 'Select', 'least', 'distinct', 'Highest', 'Lowest', 'Total', 'smallest', 'greater', 'top', 'low', 'last', 'bottom', 'Top', 'middle', 'Calculate', 'high', 'equal', 'less', 'total', 'percentile', 'Average', 'unique', 'many'] 
               ruler_adj = create_ruler(desc_adj, "ADJ")
               return ruler_adj(doc)
         
@Language.component('ruler_propn')
def ruler_propn_component(doc):
               desc_propn=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Count', 'Rank', 'Date', 'Group', 'Filter', 'Iris', 'Median', 'Maximum', 'Setosa', 'January', 'Minimum']
               ruler_propn = create_ruler(desc_propn,"PROPN")
               return ruler_propn(doc)

               
                  
