#!/usr/bin/env python

"""Adds id element with filename as value (without file extension) to all files within the given folder path (hardcoded)"""

from glob import glob
import os
import xml.etree.ElementTree as etree
import ntpath

__author__ = "Nikola Tanjga"
__copyright__ = "Copyright 2020, HL7Austria"
__credits__ = ["Nikola Tanjga"]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Nikola Tanjga"
__email__ = "nikola.tanjga@elga.gv.at"
__status__ = "Production"


files_list = glob(os.path.join("Y:\FHIR\github\hl7-at-fhir-profiles\AustrianPatient", '*.xml')) #change path to the location of your local resources

for file in sorted(files_list):
  
  with open(file, "r") as in_file:
    buf = in_file.readlines()

  with open(file, "w") as out_file:
    for line in buf:
        if line == "<StructureDefinition xmlns=\"http://hl7.org/fhir\">\n":
            line = line + "  <id value=\""+ ntpath.basename(file)[:-4] +"\"/>\n"
        out_file.write(line)

  
  #following xml way got problematic with loading namespaces and resorting randomly all elements, changed method to filewriter (see above)
  
  #data = etree.parse(file, etree.XMLParser(encoding='utf-8'))
  #structureDefinition = data.getroot() # find('./StructureDefinition')
  #id = etree.SubElement(structureDefinition, 'id')
  #structureDefinition.insert(0, id) #moves id subelement to the first position
  #id.set('value', ntpath.basename(file)[:-4]) #-4 for removing ".xml" in the basename of the whole filepath
  #data.write(file)
  