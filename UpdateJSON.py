import subprocess
import os
import time

# Function to run a script
def run_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")
        exit(1)

# Run the first script
print("Running ParseandExtract_1.py...")
run_script('parseandextract_part_1.py')

# Prompt user to update the CSV file
input("Press Enter to continue and update the datasets_and_tables_unique file.")

# Check if the CSV file has been modified after running the first script
csv_file = 'datasets_and_tables_unique.csv'
csv_mod_time = os.path.getmtime(csv_file)

while True:
    time.sleep(5)  # Wait for 5 second before checking again
    new_mod_time = os.path.getmtime(csv_file)
    if new_mod_time > csv_mod_time:
        print("CSV file has been updated.")
        break
    else:
        print("Waiting for CSV file to be updated...")

# Run the second script
print("Running update_json_1.py...")
run_script('update_json_part_2.py')

print("Both scripts have been successfully executed.")
