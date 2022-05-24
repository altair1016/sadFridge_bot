import re
import json
import uuid

json_dict = list()

origin_file = open("ricette.txt", "r")
arr_lines = origin_file.readlines()
key = ""
val = ""
json_inner_dict = {}
ing_list = []
pattern = '[^0-9a-zA-Z\' ]+'
meta_string= ""
json_main_dict = dict()

def format_ingredient(text):
    meta_string = ""
    text_dict = dict()
    if '===' in text:
        text = text.split("===")
    elif '====' in text:
        text = text.split("====")
    else:
        text = text.split(" ")
        text_arr = []
        text_arr.append(text[0])
        text_arr.append("".join(text_arr[1:]))
    text_dict["ingrediente"] = re.sub(pattern, '', text[1]).rstrip().lstrip()
    text_dict["quantita"] = text[0].rstrip().lstrip()
    meta_string = text_dict["ingrediente"].rstrip().lstrip() + "-"
    return text_dict, meta_string


for line in arr_lines:

    if line[0:8] == ":Ricette":
        my_id = str(uuid.uuid4())
        json_main_dict[my_id] = json_inner_dict
        ing_principale = ""
        if 'ing_principale' in json_inner_dict.keys():
            ing_principale = "ing_principale:" + json_inner_dict["ing_principale"].lower()
        json_inner_dict["metadata"] = meta_string.lower()[0:-1] + ";" + ing_principale
        json_dict.append(json_inner_dict)
        json_inner_dict = {}
        json_inner_dict["id"] = my_id
        meta_string= ""

    if line[0:8] != ":Ricette":
        if line[0] == '-':
            l = line.replace("-", "")
            key = l.lstrip().rstrip().replace("\r\n", "").replace("\xe8", "e").lower().decode('latin-1')
            ing_list = []
            single_ing = {}
        else:
            val = line.lstrip().rstrip().replace("\r\n", "").replace("\xe8", "e").decode('latin-1')
            if key == 'ingredienti':
                val, meta = format_ingredient(val)
                if 'decorare' not in val['ingrediente'].lower():
                    ing_list.append(val)
                    json_inner_dict[key] = ing_list
            else:
                json_inner_dict[key] = val

            if key == 'tipo_piatto' :
                meta_string = meta_string + "tipo_piatto:" + val + ';ingredienti:'
            elif key == 'ingredienti':
                meta_string = meta_string + meta



with open('ricette.json', 'w') as json_file:
    json.dump(json_dict[1:], json_file, indent=4, sort_keys=True)
