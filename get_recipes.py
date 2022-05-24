import json
import random as rm
import sys
import match_data as md


def random_receipe(data):
    rand_in = rm.randint(0, len(data))
    return(data[rand_in])

def recipe_from_ing(value, data):
    recipes_match = []
    values = md.input_format(value)
    for elt in data:
        metadata_ing = md.get_ing_from_meta(elt["metadata"])
        match = md.matching_ingredients(values, metadata_ing)
        if match[1] > 60:
            recipes_match.append(elt)
    len_recipes_match = len(recipes_match)
    if len_recipes_match > 0:
        return recipes_match[rm.randint(0, len(recipes_match))]
    return False


def get_formatted(elt):
    ing_text = ""
    if elt == False:
        text_msg = "Qualcosa non va! Riprova con un nuovo inserimento"
    else:
        text_msg = "*Ho trovato una possibile ricetta per i tuoi ingredienti:*\n " \
                    "\n*{}*: {}" \
                    "\n*{}*: {}" \
                    "\n*{}*: {}" \
                    "\n*{}*: {}" \
                    "\n*{}*: {}" \
                    "\n\n*{}*: {}" . format("Nome", elt["nome"].encode('utf-8'),
                                      "Tipologia", elt["tipo_piatto"].encode('utf-8'),
                                      "Ingrediente principale", elt["ing_principale"].encode('utf-8'),
                                      "Note particolari", elt["note"].replace("Luogo:", "").encode('utf-8'),
                                      "N. persone", elt["persone"],
                                      "Preparazione", elt["preparazione"].encode('utf-8')
                                      )
        for ing in elt["ingredienti"]:
            ing_text = ing_text + ing["ingrediente"]
            if len(ing["quantita"].lstrip().rstrip()) > 0:
                ing_text = ing_text + " (" + ing["quantita"] +"), "
            else:
                ing_text = ing_text + ", "

        text_msg = text_msg + "\n*{}*: {}".format("Ingredienti (dosi)", ing_text[0:-2].encode('utf-8'))
    return text_msg.decode('utf-8')


class RecipeBookInstance:
    def __init__(self):
        with open('ricette.json', 'r') as json_file:
            self.__data__ = json.load(json_file)
    def get_data_instance(self):
        return self.__data__

RECIPEBOOK = RecipeBookInstance()
print(get_formatted(recipe_from_ing("pomodori, patate, zucchine", RECIPEBOOK.get_data_instance())))
