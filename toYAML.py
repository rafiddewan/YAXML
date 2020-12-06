"""
Does the following Conversion
YAML -> XML

Created on December 6, 2020

Required libraires: lxml

@author: Rafid Dewan
@company: Ciena Corporation

"""
from lxml import etree
import YAXML

# Gets the associated namespace if there is a namespace amongst the children, else returns None
def getNameSpace(input):
    if('xmlns' in input):
        namespace = input.pop("xmlns")
        return f'{YAXML.getPrefix()}-{namespace}'
    return None

#Creates an element, namespace is included with the element if it is not None
def createElem(key, namespace=None):
    if(namespace is None):
        return etree.Element(key)
    else:
        return etree.Element(key, xmlns=namespace)

#Maps the dictionary to an element and iterates over the values
def dict_to_elem(key, input):
    namespace = getNameSpace(input)
    root = createElem(key, namespace)
    for (key, val) in input.items():
        root.append(to_elem(key, val))
    return root

#Checks if its a dictionary element to add the element as a composite node, if not then set it as a leaf node
def to_elem(key, input):
    if isinstance(input, dict):
        return dict_to_elem(key, input)
    else:
        elem = createElem(key)     
        elem.text = str(input)
        return elem
