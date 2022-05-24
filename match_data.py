
def get_ing_from_meta(metadata):
    return metadata.split(";")[1].split(":")[1]

def get_tipo_from_meta(metadata):
    return metadata.split(";")[0].split(":")[1]

def get_ing_princ_from_meta(metadata):
    return metadata.split(";")[2].split(":")[1]

def input_format(input):
    values_to_replace = ['.','!', '-', '#']
    for elt in values_to_replace:
        input = input.replace(elt, '')
    values = input.split(',')
    values_final = [x.lstrip().rstrip().lower().replace(" ", "") for x in values]
    return values_final

def determine_percentage(user_list_len, match_list):
    val_perc = 100
    true_val = [x for x in match_list if x is True]
    count_true_val = len(true_val)
    if count_true_val == user_list_len:
        return val_perc
    return (count_true_val/user_list_len) * 100


def matching_ingredients(user_list, metadata):
    matching_list = []
    match_percent = 0

    for ing in user_list:
        ing = ing[0:-1]
        if ing in metadata:
            matching_list.append(True)
        else:
            matching_list.append(False)
    match_percent = determine_percentage(len(user_list), matching_list)
    return (matching_list, match_percent)





data = {"metadata": "tipo_piatto:bevande;ingredienti:succo d'arancia-gin-vermouth rosso-angostura-per servire-ciliegina al maraschino-insalata lattuga fresca;ing_principale:gin",
        }
print(get_ing_from_meta(data["metadata"]))


