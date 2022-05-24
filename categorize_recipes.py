# coding=utf-8

import json


with open('ricette.json', 'r') as json_file:
    data = json.load(json_file)


def define_categories(data):
    s = set()
    for elt in data:
        s.add(elt["tipo_piatto"])
    return s


def define_main_ing(data):
    s = set()
    for elt in data:
        s.add(elt["ing_principale"])
    return s

def define_all_ing(data):
    s = set()
    for elt in data:
        for ing in elt["ingredienti"]:
            s.add(ing["ingrediente"])
    return s

def categorize_ids_categories(data, category):
    cat_json = {}
    for each_category in category:
        cat_json[each_category] = []
    for elt in data:
        cat_json[elt["tipo_piatto"]].append(elt["id"])
    return cat_json

s = define_categories(data)
s1 = define_main_ing(data)
s2 = define_all_ing(data)
cat = categorize_ids_categories(data, s)
print(s)

