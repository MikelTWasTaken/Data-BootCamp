import json

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

json_file = "my_file.json"

#Convert a Python dictionary to JSON string
with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj)
   #json.dump(obj2save , destination_file)

json_my_family = json.dumps(my_family)
print(json_my_family)

json_file = "index.json"

#Convert a Python dictionary to JSON string : Pretty Print
with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj, indent = 2, sort_keys=True)