import spacy
from spacy.language import Language
from spacy.pipeline import EntityRuler

from custom_components.utils import create_ruler

nlp = spacy.load("en_core_web_sm")

# Create component factories
@Language.component("ruler_arg")
def ruler_arg_component(doc):
    oper_arg=['[Sepal Length]', '[Sepal Width]', '[Petal Length]', '[Petal Width]', '[Species]']
    ruler_arg = create_ruler(oper_arg,'ARG')
    return ruler_arg(doc)
                     
@Language.component("ruler_argn")
def ruler_argn_component(doc):
    oper_argn=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']  
    ruler_argn = create_ruler(oper_argn,'ARGN')
    return ruler_argn(doc)
                     
@Language.component("ruler_numm")
def ruler_numm_component(doc):
    oper_numm=['0', '1', '9', '5', '3', '4', '2', '1.5', '2.5', '4.5', '3.0', '3', '2.0', '5.0']
    ruler_numm  = create_ruler(oper_numm,'NUM')
    return ruler_numm(doc)
                     
@Language.component("ruler_advv")
def ruler_advv_component(doc):
    oper_advv=['alphabetically', 'THEN', 'ELSE', 'highest to lowest', 'ASC', 'DESC', 'NULL', 'LEFT']
    ruler_advv  = create_ruler(oper_advv,'ADV')
    return ruler_advv(doc)
                     
@Language.component("ruler_oper")
def ruler_oper_component(doc):
    oper_oper= ['STARTS WITH', 'SORT', 'SUM', 'AVG', 'MEDIAN', 'COUNT', 'COUNT DISTINCT', 'MIN', 'MAX', 'GROUP BY', 'ORDER BY', 'TOP', 'STARTS', 'COUNTD','ENDSWITH', 'INDEX', 'IF', 'DATETRUNC', '[Date]', 'RANK_PERCENTILE', 'FIXED', 'SORTED BY', 'RANK', 'LISTED FROM', 'STARTSWITH', 'IF CONTAINS', 'BY']
    ruler_oper = create_ruler(oper_oper,"OPER")
    return ruler_oper(doc)
                     
@Language.component("ruler_adpp")
def ruler_adpp_component(doc):
    oper_adpp=['FROM', 'BETWEEN', 'WITH', 'to', 'AND', '>=', '<', '!=', '<=', '=', '>']
    ruler_adpp  = create_ruler(oper_adpp,'ADP')
    return ruler_adpp(doc)
                     
@Language.component("ruler_nounn")
def ruler_nounn_component(doc):
    oper_nounn=['month', 'TODAY', 'color', 'YEAR', 'versicolor', 'setosa', 'year', 'virginica']
    ruler_nounn = create_ruler(oper_nounn, "NOUN")
    return ruler_nounn(doc)
                     
@Language.component("ruler_adjj")
def ruler_adjj_component(doc):
    oper_adjj=['highest', 'lowest']
    ruler_adjj = create_ruler(oper_adjj, "ADJ")      
    return ruler_adjj(doc)

@Language.component("ruler_sort_command")
def ruler_sort_command_component(doc):      
    for sent in doc.sents:
        text = sent.text.lower()
        if "sort by" in text:
           # Extract the criteria immediately following "sort by"
           criteria_start = text.index("sort by") + len("sort by")
           criteria = text[criteria_start:].strip()
           # Custom logic to handle "sort by <criteria>"
           # print(f"Handling 'sort by {criteria}' command")
        elif "sort" in text:
                       pass
        # Custom logic to handle "sort"
        #print("Handling 'sort' command")
        return doc
