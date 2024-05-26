from openai import OpenAI
from dotenv import load_dotenv
import json
import os

from .consts.nutrition import IMPORTANT_MACROS, SUPPORTED_IDENTIFIERS 

load_dotenv()

client = OpenAI(
     api_key=os.environ.get("OPENAI_API_KEY"),
)

def generate_estimate(food_description: str):
    """ 
    Get the nutritional estimate of a food description

    Args:
    food_description (str): The description of the food

    Returns:
    dict: The nutritional estimate of the food
    """

    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": f"You are a nutritional content estimation machine. You are given a description of foods and drinks, and respond only by returning a json object. \nYou will always abide by the following rules:\n1. You will provide a best estimate for the relevant nutritional fields.\n2. You will return a response in valid JSON of the format: \n[ {{ \"identifier\": str , \"value\": number }}, ... ] and you will not include any additional text around the json object such as quotation marks or other strings.\n3. The identifiers in your response will be from this list: {SUPPORTED_IDENTIFIERS}\n4. You will only provide as much detail as is relevant for the food type. (e.g. provide \"Potassium\" for Banana since they're high in potassium, but not for rice, where potassium isn't relevant)\n5. You will ALWAYS provide the following {len(IMPORTANT_MACROS)} values: {IMPORTANT_MACROS}"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": food_description
            }
        ]
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    nutritional_json_string = response.choices[0].message.content
    return json.loads(nutritional_json_string)
