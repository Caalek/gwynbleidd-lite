import json
import random

def get_random_quote():
    with open("quotes2.json", "r") as f:
        quote_array = json.load(f)
    return random.choice(quote_array)["quote"]