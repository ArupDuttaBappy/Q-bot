import json
import csv


# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[0]["pairs"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

    # python object to be appended


filename = 'mental_health_faq.csv'

with open(filename, 'r', encoding="utf8") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        y = {
            "query": row[1],
            "reply": row[2]
        }
        write_json(y)
