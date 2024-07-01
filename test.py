import json

# Load the JSON data from a file
with open('questions.json', 'r') as file:
    data = json.load(file)

# Use a set to keep track of unique questions
unique_questions = set()
unique_data = []

# Iterate through the list of questions
for item in data:
    question = item['question']
    if question not in unique_questions:
        unique_questions.add(question)
        unique_data.append(item)

# Write the unique questions to a new JSON file
with open('unique_questions.json', 'w') as file:
    json.dump(unique_data, file, indent=2)

print("Unique questions have been saved to 'unique_questions.json'.")
