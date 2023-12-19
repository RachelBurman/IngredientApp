import openai
import pandas as pd
import random

keys = {}
with open('keys.txt', 'r') as f:
    for line in f:
        key, value = line.strip().split(' = ')
        if key == 'AUTHDETAILS':
            value = value.strip('()').split(', ')
            value = tuple(v.strip('""') for v in value)
        keys[key] = value

# Now you can access the keys and values like this:
api_key = keys['API KEY']
auth_details = keys['AUTHDETAILS']
bolt = keys['BOLT']
openai.api_key = api_key

recipe_df = pd.read_csv('closest_recipes_pca.csv')
ingredient_df = pd.read_csv('closest_nodes_umap_2.csv')

def generate_random_recipe():
    recipes = []  # Create a list for the recipes
    rand = []
    for index, row in recipe_df.iterrows():
        recipe_name = row['RecipeName']  # Use a different variable for the recipe name
        for index, row in ingredient_df.iterrows():
            ingredient = row['IngredientName']
            closest_nodes = [row[f'Closest_Node_{i}'] for i in range(1, 6)]
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"Could you suggest a novel recipe utilizing {ingredient} and {closest_nodes} based upon {recipe_name}?"}
                    ]
                )
                answer = response['choices'][0]['message']['content'] if response['choices'] else "No response"
                recipes.append(f"Novel recipe using {ingredient} and {closest_nodes} based upon {recipe_name}: {answer}")
                if len(recipes) >= 5:
                    rand = random.sample(recipes, 1)
                    break
            except Exception as e:
                print(f"Error with ingredient {ingredient}: {e}")
        if rand is not None:  # Break the outer loop if a recipe has been selected
            break
    return rand  # Return the selected recipe or None if fewer than 5 recipes are generated