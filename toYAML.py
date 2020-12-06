"""
Does the following Conversion
XML -> YAML

Created on December 6, 2020

Required libraires: lxml

@author: Rafid Dewan
@company: Ciena Corporation

"""
class XMLStructure:
    def __init__(self, tag, namespace=None, value=None):
        self.tag = tag
    
    def checkIfHasChild(self):
        pass

def getNameSpace():
    """
    Gets the associated namespace if there is a namespace amongst the children, else returns None
    @param: input which are the values or composite keys of the parent key
    @rtype: string of the namespace
    """
    pass

def createTag():
    """
    Creates the tag for the element
    """
    pass

def elem_to_dict():
    pass

def to_elem(root):
    # if(isinstance of root.)
    pass