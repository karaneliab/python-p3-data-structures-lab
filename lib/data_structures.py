spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names
 
result = get_names(spicy_foods)
print(result)

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food['heat_level']>5:
            spiciest_foods.append(food)
       
    return spiciest_foods
 
result = get_spiciest_foods(spicy_foods)
print(result)


# printing spicy foods
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
print_spicy_foods(spicy_foods)


# getting spicy foods
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None


result = get_spicy_food_by_cuisine(spicy_foods, "American")
print(result)

result = get_spicy_food_by_cuisine(spicy_foods, "Thai")
print(result)


def print_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest_foods.append(food)

    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


print_spiciest_foods(spicy_foods)


  

# average heat level
def get_average_heat_level(spicy_foods):
    heat_levels = []

    for food in spicy_foods:
        heat_levels.append(food['heat_level'])

    total_heat = sum(heat_levels)
    num_foods = len(heat_levels)

    if num_foods > 0:
        average = total_heat // num_foods
        return average
    else:
        return 0  



result = get_average_heat_level(spicy_foods)
print(result)


   
# creting a new spicy food
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}
result = create_spicy_food(spicy_foods,spicy_food)
print(result)
