import glob
import glob
from xml.dom import minidom
import os.path 


def basenames(files):
    return [os.path.basename(f) for f in files]




dessert_files = basenames(glob.glob("dessert/*"))
main_dish_files = basenames(glob.glob("main_dish/*"))
soup_files  =  basenames(glob.glob("soup/*"))
starter_files = basenames(glob.glob("starter/*"))

recipes = set(dessert_files +main_dish_files + soup_files +starter_files)

header  = "[Relational Context]\nrecipe_cat.rcf\n[Binary Relation]\nrecipes\n"
rcf_recipes = " | ".join([r for r in recipes]) + " |\n"
rcf_cat = " | ".join(["dessert","main_dish","soup","starter"]) + " |"


with open("recipe_cat.rcf","w") as w:
    w.write(header)
    w.write(rcf_recipes)
    w.write(rcf_cat + "\n")
    for i in recipes:
        w.write(" ".join([str(int(i in c)) for c in [dessert_files,main_dish_files,soup_files,starter_files]]))
        w.write("\n")
    w.write("[END Relational Context]")


