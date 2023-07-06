def ReadFile(name_file):
    '''
    функция на входе принимет название файла где храниться cook_book, возвращае cook_book в виде словаря.
    '''
    cook_book = {}
    with open(name_file, encoding='utf-8') as file:
        for text in file:
            dish_name = text.strip()
            counter_ingredient = int(file.readline())
            ingredients_list = []
            for _ in range(counter_ingredient):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            cook_book[dish_name] = ingredients_list
            skip_line = file.readline()
    return cook_book


if __name__ == "__main__":
    print(ReadFile('cooking_recipes.txt'))