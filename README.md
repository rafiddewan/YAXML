# YAXML
YAML to XML Converter

## Purpose
Currently working at Ciena, I noticed there weren't many good open-sourced libraries of YAML to XML scripts. This script includes properties of XML such as namespaces and YAML properties such as lists. YAML is so much easier and readable than XML it will reduce approximately 50% of development time to create automated templates or manifests for their products.

## How to Use
Simply type ```python3 YAXML.py <template.yml file> -p  NTT862NA ```

## Version 1.0
- Uses Python
- Uses a recursive solution to generate the xml document

## Future Releases
- Will be using C for better and more robust performance
- Will use algorithms to optimize the run-time of the script

## Libraries Used
- PyYAML
- lxml
- OptionParser
- Sys
