import json

# Load existing intents data
intents = json.loads(open('intents.json').read())

# Collect new data from user
while True:
    user_input = input("Enter a sentence: ")
    tag = input("Enter a tag for this sentence: ")
    # Check if this tag already exists in the intents data
    existing_tags = [intent["tag"] for intent in intents["intents"]]
    if tag in existing_tags:
        # If the tag already exists, add the new sentence to the existing tag's patterns
        for intent in intents["intents"]:
            if intent["tag"] == tag:
                intent["patterns"].append(user_input)
    else:
        # If the tag doesn't exist, create a new intent object with the tag and sentence
        new_intent = {"tag": tag, "patterns": [user_input], "responses": []}
        intents["intents"].append(new_intent)
    # Save the updated intents data
    json.dump(intents, open('intents.json', 'w'), indent=4)
    cont = input("Do you want to enter another sentence? (yes/no)")
    if cont == "no":
        break
