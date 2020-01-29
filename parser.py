from xml.dom import minidom

import glob

recipe_files  = glob.glob("*/*.xml")
#print(recipe_files)


recipes = []

for recipe in recipe_files:
    print("Parsing : {}".format(recipe))
    xml_file = minidom.parse(recipe)

    current_recipe = dict()

    current_recipe['ingredients'] = xml_file.getElementsByTagName("IN")
    current_recipe['tools'] = xml_file.getElementsByTagName("US")
    
    current_recipe['content'] = xml_file.getElementsByTagName("PR")[0]

