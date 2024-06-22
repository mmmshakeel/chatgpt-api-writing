from openai import OpenAI
from dotenv import load_dotenv
import sys
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv('API_KEY'),
)

user_prompt = """
Help me with improving my writing for general purposes such as messages in whatsapp, slack or online chat. 
Always keep the text simple, grammatically correct and easy to understand. 
The text should be written in a friendly and in an engaging tone.
Improve only the given text and do not add extra information such as Subect lines and greetings. 
Improve the following text:\n\n
"""

def improve_text(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an english assistant."},
            {"role": "user", "content": f"{user_prompt}{text}"}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    input_text = sys.argv[1]
    improved_text = improve_text(input_text)
    print(improved_text)