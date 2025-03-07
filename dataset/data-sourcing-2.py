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


filename = 'intent_recognition_dataset.json'

with open(filename) as jsonfile:
    datareader = json.load(jsonfile)
    # print(len(datareader['intents'][0]['responses']))
    for item in datareader['intents']:
        text = item['text']
        responses = item['responses']
        for i in range(len(text)):
            for j in range(len(responses)):
                y = {
                        "query": text[i],
                        "reply": responses[j]
                    }
                write_json(y)

