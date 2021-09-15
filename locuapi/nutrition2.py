import requests
from PIL import Image
from io import BytesIO

def welcome_screen():
    print('WELCOME IN RECIPE SEARCH!')
    print('-------------------------')

def calculate_calories():
    answer = input('Do you want to know how many calories you should eat(yes/no)? ')
    if answer == 'yes':
        height = int(input('Please enter your height (cm): '))
        weight = int(input('Please enter your weight (kg): '))
        age = int(input('Please enter your age: '))
        gender = input('Please enter your gender (F/M): ')
        level_of_activity = int(input('How active are you? \n'
                                  ' 1. Sedentary (little or no exercise)\n'
                                  ' 2. Lightly active (exercise 1–3 days/week)\n'
                                  ' 3. Moderately active (exercise 3–5 days/week) \n'
                                  ' 4. Active (exercise 6–7 days/week)\n'
                                  ' 5. Very active (hard exercise 6–7 days/week)\n'
                                  '     Please choose a number(1-5): '))
        if level_of_activity == 1:
            activity = 1.2
        elif level_of_activity == 2:
            activity = 1.375
        elif level_of_activity == 3:
            activity = 1.55
        elif level_of_activity == 4:
            activity = 1.725
        elif level_of_activity == 5:
            activity = 1.9

        BMR = calculate_BMR(gender, weight, height, age)
        ARM = int(BMR * activity)
        print('\n')
        print('**To maintain your weight you should eat {} kcal**'.format(ARM))

    print('-------------------------')
    print('SEARCH FOR A RECIPE! ')

def calculate_BMR(g, w, h, a):
    if g == 'F':
        return 655.1 + (9.563 * w) + (1.850 * h) - (4.676 * a)
    elif g == 'M':
        return 66.47 + (13.75 * w) + (5.003 * h) - (6.755 * a)


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
        image = recipe['image']


        if calories<max_of_calories and calories>min_of_calories:
            print(recipe['label'])
            print(recipe['uri'])
            print(recipe['image'])
            print('Diet Label: {}'. format(recipe['dietLabels']))
            print('Cuisine Type: {}'.format(recipe['cuisineType']))
            print('{} kcal'.format(calories))
            print()
            print_image = input('Do you want to display image? (yes/no)')
            if print_image == 'yes':
                response = requests.get(image)
                img = Image.open(BytesIO(response.content))
                img.show()


    save_recipes = input('Do you want to save these recipes into a file?(yes/no) ')
    if save_recipes == 'yes':
        with open("recipetext.txt", "w") as recipe_file:
            recipe_file.write(str(recipe))
            recipe_file.close()
            print('File saved successfully!')


welcome_screen()
calculate_calories()
ingredient = input('Enter an ingredient: ')
find_recipe()
run()

