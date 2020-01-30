import glob
from xml.dom import minidom


def aliment_in_category(files):    
    ingredients=[]
    for f in files:
        xml_file = minidom.parse(f)
        ingredients.extend([e.firstChild.nodeValue for e in xml_file.getElementsByTagName("IN")])
    return set(ingredients)

dessert_files = glob.glob("dessert/*")
main_dish_files = glob.glob("main_dish/*")
soup_files  =  glob.glob("soup/*")
starter_files = glob.glob("starter/*")

ing_cat=[aliment_in_category(folder) for folder in [dessert_files,main_dish_files,soup_files,starter_files]]

with open('ingredients.txt',"r") as f:
    ingredients = f.readlines()
    ingredients = set([i.strip() for i in ingredients])






# Header rcf
header  = "[Relational Context]\ningredient_category.rcf\n[Binary Relation]\ningredients\n"
rcf_ingredient = " | ".join([i for i in ingredients]) + " |\n"
rcf_category = " | ".join(["dessert","main_dish","soup","starter"]) + " |"



with open("ingredient_category.rcf","w") as w:
    w.write(header)
    w.write(rcf_ingredient)
    w.write(rcf_category + "\n")
    for i in ingredients:
        w.write(" ".join([str(int(i in label)) for label in ing_cat]))
        w.write("\n")
    w.write("[END Relational Context]")
