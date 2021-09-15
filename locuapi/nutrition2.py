import requests

def welcome_screen():
    print('WELCOME IN RECIPE SEARCH!')

def recipe_search(ingredient):
    app_id = '552ff3b8'
    app_key = 'd13fac5c413e5e3fcac0ee52e558f343'
    result = requests.get(
        ' https://api.edamam.com/search?q={}&diet=balanced&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def find_recipe():
    return recipe_search(ingredient)

def run():

    min_of_calories = int(input('Enter the MIN range of calories: '))
    max_of_calories = int(input('Enter the MAX range of calories: '))
    results = find_recipe()

    for result in results:
        recipe = result['recipe']
        calories = int(recipe['calories'])

        if calories<max_of_calories and calories>min_of_calories:
            print(recipe['label'])
            print(recipe['uri'])
            print(recipe['cuisineType'])
            print('{} kcal'.format(calories))
            print()

    saverecipes = input('Do you want to save these recipes into a file?')
    if saverecipes == 'yes':
        with open("recipetext.txt", "w") as recipe_file:
            recipe_file.write(str(recipe))
            recipe_file.close()


welcome_screen()
ingredient = input('Enter an ingredient:')
find_recipe()
run()
