import os
import pprint


def parse_ingredients(line: str):
    """
    Parses a line of ingredients and returns a dictionary with the structure:
    {
        'ingredient_name': ...,
        'quantity': ...,
        'measure': ...
    }
    """
    i, q, m = line.split(" | ")
    return {
        'ingredient_name': i.strip(),
        'quantity': int(q.strip()),
        'measure': m.strip()
    }


def read_cook_book(file_path):
    """
    Returns a dictionary with the structure:
    { 
      'Dish': [
          {'ingredient_name': ..., 'quantity': ..., 'measure': ...}, 
          ...
      ],
      ...
    }
    """
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    cook_book, i = {}, 0
    while i < len(lines):
        dish, i = lines[i], i + 1
        c, i = int(lines[i]), i + 1
        ingredients = []
        for _ in range(c):
            ingredients.append(parse_ingredients(lines[i]))
            i += 1
        cook_book[dish] = ingredients
    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count, file_path="recipes.txt"):
    """
    Returns dictionary with name of ingredients and their quantity for the given dishes and person count.
    {
        'ingredient_name': {
            'measure': ...,
            'quantity': ...
        },
        ...
    }
    """
    shop_list = {}
    cook_book = read_cook_book(file_path)
    for dish in dishes:
        ingredient_list = cook_book[dish]
        for ingr in ingredient_list:
            name = ingr['ingredient_name']
            if name not in shop_list:
                shop_list[name] = {
                'quantity': ingr['quantity'] * person_count, 
                'measure': ingr['measure']}
            else:
                curr_q = shop_list[name]['quantity']
                q = curr_q + ingr['quantity'] * person_count
                s_l = shop_list[name]
                s_l['quantity'] = q   
    return shop_list


if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "recipes.txt")
    get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2, file_path)
