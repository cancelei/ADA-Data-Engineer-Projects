import pandas as pd
import os
import re
from datetime import datetime

# Define the base path for the logs
base_path = 'C:/Users/glaub/ADA-Github.CI.Run-RSpec.Log.extrator.and.normalizer-PYTHON/logs'


# Define the pattern to extract the data
pattern = re.compile(r'(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2}).*? (\d+) examples, (\d+) failures')

# Placeholder for extracted data
extracted_data = []

# Function to process each file and extract data
def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                date_str, time_str, total_examples, failures = match.groups()
                date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d/%m/%Y')
                extracted_data.append([date, time_str, int(total_examples), int(failures)])

# Iterate through the folder structure
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file == '7_Run rspec.txt':
            process_file(os.path.join(root, file))

# Convert the extracted data into a pandas DataFrame
df = pd.DataFrame(extracted_data, columns=['date', 'hour', 'total examples', 'failures'])

# Show the DataFrame
print(df)
