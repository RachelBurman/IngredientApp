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

df = pd.read_csv('closest_nodes_umap_2.csv')

def generate_random_pairings():
    pairings = []  # Create a list for the pairings
    rand = None
    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        ingredient = row['IngredientName']
        closest_nodes = [row[f'Closest_Node_{i}'] for i in range(1, 6)]  # get all closest nodes
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"What are some good ingredient pairings for {ingredient} with similarities to {closest_nodes}?"}
                ]
            )
            # Extracting the response text
            answer = response['choices'][0]['message']['content'] if response['choices'] else "No response"
            pairings.append(f"Novel ingredient pairings using {ingredient} and {closest_nodes} : {answer}")
            if len(pairings)>=5:
                rand = random.sample(pairings, 1)
                break
            #print(f"Pairings for {ingredient} with similarities to {closest_nodes}: {answer}")
        except Exception as e:
            print(f"Error with ingredient {ingredient}: {e}")
        if rand is not None:
            break
    return rand  # Return the selected recipe or None if fewer than 5 recipes are generated