import json
import time
import os
from datetime import datetime

import training_module  # Import your training module

# File containing new intents to be added
NEW_INTENTS_FILE = "new_intents.json"
# File containing existing intents
INTENTS_FILE = "intents.json"
# File to save the model
MODEL_FILE = "chatbot_model.model"

def check_new_intents():
    """
    Check if there are any new intents in the new_intents.json file.
    If there are, add them to the intents.json file and train the model.
    """
    if os.path.exists(NEW_INTENTS_FILE):
        with open(NEW_INTENTS_FILE, "r") as f:
            new_intents = json.load(f)
            if len(new_intents) > 0:
                print(f'[{datetime.now()}] New intents found. Updating intents and retraining model...')
                with open(INTENTS_FILE, "r") as intents_f:
                    intents = json.load(intents_f)
                intents["intents"].extend(new_intents)
                with open(INTENTS_FILE, "w") as intents_f:
                    json.dump(intents, intents_f)
                training_module.train_model(INTENTS_FILE, MODEL_FILE)
                os.remove(NEW_INTENTS_FILE)
            else:
                print(f'[{datetime.now()}] No new intents found.')
    else:
        print(f'[{datetime.now()}] No new intents file found.')

if __name__ == "__main__":
    while True:
        check_new_intents()
        time.sleep(3600)  # Check for new intents every hour
