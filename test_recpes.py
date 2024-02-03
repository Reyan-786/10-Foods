from recpes import recipes
from classes_of_food import class_name
# print(recipes.keys())
set_recpes = set(recipes.keys())

missing_items = [item for item in class_name if item not in set_recpes]

print(len(missing_items))

print("Missing recipes for the following classes:")
for item in missing_items:
    print(item)
