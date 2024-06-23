from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

load_dotenv()

client = OpenAI(
    api_key=os.getenv('API_KEY'),
)

user_prompt = """
I have written an academic essay and would like you to enhance its quality. 
Please revise the text to improve its clarity, coherence, and academic tone while preserving the original meaning. 
I need to ensure that the text is free of grammatical errors, awkward phrasing, and inconsistencies, and that it maintains a formal, academic tone.
Ensure that the language appropriate for a Master's level paper. Here is the text:\n\n
"""


def improve_text(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an english academic writing assistant."},
            {"role": "user", "content": f"{user_prompt}{text}"}
        ],
        max_tokens=400,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    input_text = sys.argv[1]
    improved_text = improve_text(input_text)
    print(improved_text)
