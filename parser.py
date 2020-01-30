from xml.dom import minidom

import glob

recipe_files  = glob.glob("*/*.xml")
#print(recipe_files)


recipes = []

for recipe in recipe_files:
    print("Parsing : {}".format(recipe))
    xml_file = minidom.parse(recipe)

    current_recipe = dict()

    current_recipe['ingredients'] = [e.firstChild.nodeValue for e in xml_file.getElementsByTagName("IN")]
    current_recipe['tools'] = [e.firstChild.nodeValue for e in xml_file.getElementsByTagName("US")]
    current_recipe['content'] = xml_file.getElementsByTagName("PR")[0].firstChild.nodeValue
    recipes.append(current_recipe)

# Set of ingredients
ingredients = []
for r in recipes:
    ingredients.extend(r['ingredients'])
ingredients = set([i.lower() for i in ingredients])
print("Ingredients size :",len(ingredients))

# set of tools
tools = []
for r in recipes:
    tools.extend(r['tools'])
tools = set(tools)
print("Tools size : ",len(tools))


def get_prep(recipe):
    """Returns the content"""
    return recipe['content']

def generate_table(recipe):
    """Returns 2 dicts """

    
    tools_in_recipe = set(recipe['tools']) 
    ingredient_in_recipe = set(recipe['ingredients'])

    
    tool_matrix =dict()
    ingredient_matrix = dict()
    
    for t in tools:
     tool_matrix[t] = t in tools_in_recipe

    for i in ingredients:
        ingredient_matrix[i] = i in ingredient_in_recipe
     
    return tool_matrix, ingredient_matrix
    

print(generate_table(recipes[0]))


sorted_ingredients = sorted(list(ingredients))
with open("ingredients.txt","w") as f:
    for aliment in sorted_ingredients:
        f.write("{}\n".format(aliment))
