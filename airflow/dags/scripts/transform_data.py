import os
import pandas as pd
import json

# Define the columns
cols = ['slug', 'name', 'playtime', 'platforms', 'stores', 'released', 'tba', 'rating',
        'rating_top', 'ratings', 'ratings_count', 'reviews_text_count', 'metacritic',
        'tags', 'esrb_rating', 'reviews_count', 'genres']

# Initialize an empty DataFrame
df = pd.DataFrame(columns=cols)

# Get the absolute path to the user's home directory
home_dir = os.path.expanduser("~")

# Path to the folder containing the JSON files (appending the rest of the path to the home directory)
folder_path = os.path.join(home_dir, "temp_data")  # Replace "temp_data" with the folder name containing the JSON files

# print list of files and folders in ~/temp_data/
print(os.listdir(folder_path))

# Get the list of all JSON files in the folder
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

# Process each JSON file and append its data to the DataFrame
for file in json_files:
    file_path = os.path.join(folder_path, file)
    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
            if 'results' in data:
                df_temp = pd.DataFrame.from_dict(data['results'])
                df = pd.concat([df, df_temp[cols]], axis=0)
            else:
                print(f"Error: 'results' key not found in {file}. Skipping file.")
        except Exception as e:
            print(f"Error occurred while processing {file}: {e}")

# Reset the DataFrame index
df.reset_index(drop=True, inplace=True)

# Replace empty values with 0 in the DataFrame
df.fillna(0, inplace=True)

# Save the DataFrame to a CSV file
df.to_csv('~/dataset.csv', index=False)