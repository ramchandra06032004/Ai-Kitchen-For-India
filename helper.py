def get_diet_index(user_diet):
    dietary_preferences = ['Diabetic Friendly', 'Vegetarian', 'Eggetarian', 'Vegan',
                           'High Protein Vegetarian', 'No Onion No Garlic (Sattvic)',
                           'Non Vegetarian', 'High Protein Non Vegetarian', 'Gluten Free',
                           'Sugar Free Diet']
    return dietary_preferences.index(user_diet)

def get_course_index(user_course):
    type_of_course = ['Side Dish', 'Main Course', 'Snack', 'Lunch', 'Appetizer', 'Dessert',
                      'Dinner', 'World Breakfast']
    return type_of_course.index(user_course)

def get_cuisine_index(user_cuisine):
    cuisine_options = ['Indian', 'South Indian Recipes', 'North Indian Recipes',
                       'Italian Recipes', 'Continental']
    return cuisine_options.index(user_cuisine)