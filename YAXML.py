"""
YAXML is the main controller of the
YAML -> XML
and 
XML -> YAML
conversion

Created on December 6, 2020

Required libraires: lxml, yaml, sys and optparse

@author: Rafid Dewan
@company: Ciena Corporation

"""   

import yaml
from sys import stdin, stdout, stderr, exit
from lxml import etree
from optparse import OptionParser
import toYAML
import toXML


#  Retrieves the URI for the XML and YAML conversions
def getPrefix():
  """
  Retrieves the URI for the XML and YAML conversions
  """
  return "this-is-a-uri"
  
def main():
  """
  Main function for YAXML
  """
  parser = OptionParser(usage="%prog [options] [filename]")
  parser.add_option("-y", action="store_true", dest="parseToYaml",
      help="This option is for you to specify if you want to convert an existing xml template file to pec yaml template")
  parser.add_option("-x", action="store_false", dest="parseToYaml",
      help="This option is for you to specify if you want to convert an existing yaml template file to pec xml template")
  parser.add_option("-p", dest="pec", default=None,
      help="run the file with the associated pec name for the file")
  (options, args) = parser.parse_args()

  # Need to have the flag that indicates the output filename and the flag for 
  # converting to yaml or converting to xml
  if len(args) > 2:
    parser.print_help(stderr)
    exit(1)
  
  #open thefile
  input = open(args[0], "r") if any(args) and args[0] != "-" else stdin

  #Running the conversion from YAML to XML
  if not options.parseToYaml:
    yamlFile = yaml.load(input.read(), Loader=yaml.FullLoader)
    items = yamlFile.items()

    #overwrites file for clean state
    if options.pec:
      output = open(f"{options.pec}.xml", "w") 
    else: stdout
    output.close()

    #appends multiple roots into the same xml file
    file = open(f"{options.pec}.xml", "a+")

    # multiple keys generated at the root level so need to iterate through each of them # since it's not tradiational xml
    for key, setItems in items:
      currRoot = toXML.to_elem(key, setItems)
      file.write(etree.tostring(currRoot, pretty_print=True).decode("utf-8"))
    file.close()
  else:
    with open(args[0], "r") as fobj:
      xml = fobj.read()
    parser = etree.XMLParser(remove_blank_text=True)
    thisRoot = etree.XML(xml, parser)
    print(thisRoot)
        #overwrites file for clean state
    if options.pec:
      output = open(f"{options.pec}.yml", "w") 
    else: stdout
    output.close()

    #appends multiple roots into the same xml file
    file = open(f"{options.pec}.yml", "a+")


if __name__ == "__main__":
  main()