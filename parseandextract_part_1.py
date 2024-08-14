import os
import json
import csv

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define the path to the JSON file
json_file_path = os.path.join(script_dir, 'definition.json')

# Check if the JSON file exists
if not os.path.exists(json_file_path):
    print("The JSON file 'definition.json' was not found in the script directory.")
    exit()

# Read the JSON content
with open(json_file_path, 'r') as file:
    json_content = json.load(file)

# Initialize a list to store the datasets and tables
results = []

# Recursively search for datasets and tables in the JSON object
def find_datasets_and_tables(json_object):
    if isinstance(json_object, dict):
        # Check for dataset and table in the current dictionary
        if 'dataset' in json_object and 'table' in json_object:
            dataset = json_object['dataset']
            table = json_object['table']
            results.append({'Dataset': dataset, 'Table': table})
            print(f"Found dataset: {dataset} and table: {table}")
        # Recursively search in nested dictionaries
        for key, value in json_object.items():
            find_datasets_and_tables(value)
    elif isinstance(json_object, list):
        # Recursively search in each item of the list
        for item in json_object:
            find_datasets_and_tables(item)

# Start the search
find_datasets_and_tables(json_content)

# Output the results
if results:
    print("Found datasets and tables:")
    for result in results:
        print(result)
else:
    print("No datasets and tables found in the JSON file.")

# Save the results to a CSV file
csv_file_path = os.path.join(script_dir, 'datasets_and_tables.csv')
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Dataset', 'Table']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print(f"Results saved to {csv_file_path}")

# Remove duplicates by converting to a set and back to a list
unique_results = list({(item['Dataset'], item['Table']) for item in results})

# Save the unique results to a CSV file with additional columns
csv_file_path_unique = os.path.join(script_dir, 'datasets_and_tables_unique.csv')
with open(csv_file_path_unique, 'w', newline='') as csvfile:
    fieldnames = ['Dataset', 'Table', 'DatasetNew', 'TableNew']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for dataset, table in unique_results:
        writer.writerow({
            'Dataset': dataset,
            'Table': table,
            'DatasetNew': "",  # Duplicate or modify as needed
            'TableNew': ""        # Duplicate or modify as needed
        })

print(f"Unique results with new columns saved to {csv_file_path_unique}")