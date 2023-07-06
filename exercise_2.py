from exercise_1 import ReadFile

def get_shop_list_by_dishes(list_dish, people):
    '''
    функция принимет на входе список блюд из cook_book и количество персон для кого мы будем готовить, возвращает словарь с названием ингредиентов и его количества.
    '''
    cook_book = ReadFile('cooking_recipes.txt')
    products = {}
    for dish in list_dish:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in products:
                    products[consist['ingredient_name']]['quantity'] += consist['quantity'] * people
                else:
                    products[consist['ingredient_name']] = {'measure': consist['measure'], 'quantity': consist['quantity'] * people}
        else:
            print('Такого блюда нет в книге, ознакомьтесь с книгой лучше') 
    return products


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))