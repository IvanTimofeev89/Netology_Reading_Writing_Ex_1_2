with open("recipes.txt", encoding="UTF-8") as f:
    data = [[]]
    for row in f:
        if row.strip() == "":
            data.append([])
        else:
            data[-1].append(row.strip())

def book_creation(some_data_list):
    cook_book = {}
    for elem in data:
        cook_book[elem[0]] = []
        for row in elem[2:]:
            temp_dict = {}
            ingredient_name, quantity, measure = row.split("|")
            temp_dict["ingredient_name"] = ingredient_name.strip()
            temp_dict["quantity"] = int(quantity.strip())
            temp_dict["measure"] = measure.strip()
            cook_book[elem[0]].append(temp_dict)
    return cook_book

def get_all_ingredients(dishes):
    cook_book = book_creation(data)
    all_ingredients = []
    for dish in cook_book:
        for ingredients in cook_book[dish]:
            if dish in dishes:
                all_ingredients.append(ingredients)
    return all_ingredients

def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = get_all_ingredients(dishes)
    final_dict = {}
    for ingredient in all_ingredients:
        temp_dict = {}
        temp_dict[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
        for key, value in temp_dict.items():
            if key in final_dict:
                final_dict[key]['quantity'] += temp_dict[key]['quantity']
            else:
                final_dict.update(temp_dict)
    return final_dict

# Задача №1 - Получение cook_book
print(book_creation(data))

# Задача №2 - Проверка функции get_shop_list_by_dishes
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 6))


