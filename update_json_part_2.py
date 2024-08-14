import pandas as pd
import json

# Paths to the files
csv_file_path = 'datasets_and_tables_unique.csv'
json_file_path = 'definition.json'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Create a dictionary to map old dataset/table names to new ones
mapping = {}
for _, row in df.iterrows():
    old_dataset = row['Dataset'].strip() if pd.notna(row['Dataset']) else None
    old_table = row['Table'].strip() if pd.notna(row['Table']) else None
    new_dataset = row['DatasetNew'].strip() if pd.notna(row['DatasetNew']) else None
    new_table = row['TableNew'].strip() if pd.notna(row['TableNew']) else None
    
    if old_dataset and old_table:
        mapping[(old_dataset, old_table)] = (new_dataset, new_table)

# Function to update dataset and table names
def update_names(data, mapping):
    if isinstance(data, dict):
        dataset = data.get('dataset', '')
        table = data.get('table', '')
        
        if (dataset, table) in mapping:
            new_dataset, new_table = mapping[(dataset, table)]
            if 'dataset' in data:
                data['dataset'] = new_dataset
            if 'table' in data:
                data['table'] = new_table
        
        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, list):
                update_names(value, mapping)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict) or isinstance(item, list):
                update_names(item, mapping)

# Load the existing JSON data
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Update the dataset and table names
update_names(data, mapping)

# Save the updated data back to the JSON file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Definition file updated successfully.")



