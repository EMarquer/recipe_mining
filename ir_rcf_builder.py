import glob
from xml.dom import minidom
import os.path 


recipe_files  = glob.glob("*/*.xml")
recipes = [os.path.basename(r) for r in recipe_files]



def aliment_in_recipe(f):    
    xml_file = minidom.parse(f)
    ingredients = ([e.firstChild.nodeValue for e in xml_file.getElementsByTagName("IN")])
    return set(ingredients)

ing_r = [aliment_in_recipe(r) for r in recipe_files]

with open('ingredients.txt',"r") as f:
    ingredients = f.readlines()
    ingredients = set([i.strip() for i in ingredients])


header  = "[Relational Context]\ningredient_recipe.rcf\n[Binary Relation]\nthe_ingredients\n"
rcf_ingredient = " | ".join([i for i in ingredients]) + " |\n"
rcf_recipe = " | ".join(recipes) + " |"


with open("ingredient_recipe.rcf","w") as w:
    w.write(header)
    w.write(rcf_ingredient)
    w.write(rcf_recipe + "\n")
    for i in ingredients:
        w.write(" ".join([str(int(i in r)) for r in ing_r]))
        w.write("\n")
    w.write("[END Relational Context]")
