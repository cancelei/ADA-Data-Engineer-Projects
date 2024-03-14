import pandas as pd
import re
from datetime import datetime

# Sample line
line = "2024-03-01T20:36:16.2060895Z 254 examples, 6 failures"

# Regular expression to extract the datetime, number of examples, and failures
pattern = re.compile(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\.\d+Z (\d+) examples, (\d+) failures')

# Match the pattern to the line
match = pattern.match(line)

if match:
    # Extract and transform data
    dt_str = match.group(1)
    examples = int(match.group(2))
    failures = int(match.group(3))
    
    # Convert datetime string to datetime object
    dt_obj = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S")
    
    # Convert datetime object to desired date and hour format
    date = dt_obj.strftime("%d/%m/%Y")
    hour = dt_obj.strftime("%H:%M:%S")
    
    # Creating a DataFrame
    data = {
        'date': [date],
        'hour': [hour],
        'total examples': [examples],
        'failures': [failures]
    }
    
    df = pd.DataFrame(data)
else:
    print("No match found.")

df

print(df)

df.to_csv('output.csv', index=False)