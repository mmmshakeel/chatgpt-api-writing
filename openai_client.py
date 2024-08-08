"""
Module to set up OpenAI client.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv('API_KEY'),
)

# Read the model from the .env file or use the default value 'gpt-4o' if not provided
DEFAULT_MODEL = "gpt-4o"
model = os.getenv('MODEL', DEFAULT_MODEL)

def improve_text(text, user_prompt, system_prompt, max_tokens, model=model, temperature=0.7):
    """
    Improve the given text using OpenAI API.

    Args:
        text (str): The text to be improved.
        user_prompt (str): The user prompt to guide the text improvement.
        system_prompt (str): The system prompt to set the context.
        max_tokens (int): The maximum number of tokens in the response.
        model (str): The model to be used for text improvement. Default is 'gpt-4o'.
        temperature (float, optional): The temperature for the response. Defaults to 0.7.

    Returns:
        str: The improved text.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"{user_prompt}{text}"}
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].message.content.strip()
