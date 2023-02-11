import json, os, sys
import openai as ai

if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/../config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/../config.json") as file:
        config = json.load(file)

ai.api_key = config["openai_token"]

def generate_gpt3_response(user_text, print_output=False):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    completions = ai.Completion.create(
        engine='text-davinci-003', 
        temperature=0.777,   
        prompt=user_text,         
        max_tokens=1024            
    )

    if print_output:
        print(completions)
		
    return completions["choices"][0]["text"]