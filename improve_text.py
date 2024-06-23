"""
Module to improve general writing text using OpenAI API.
"""

import sys
from openai_client import improve_text

USER_PROMPT = """
Help me with improving my writing for general purposes such as messages in whatsapp, slack or online chat. 
Always keep the text simple, grammatically correct and easy to understand. 
The text should be written in a friendly and in an engaging tone.
Improve only the given text and do not add extra information such as Subject lines and greetings. 
Improve the following text:\n\n
"""

SYSTEM_PROMPT = "You are an english writing assistant."

if __name__ == "__main__":
    input_text = sys.argv[1]
    improved_text = improve_text(
        text=input_text,
        user_prompt=USER_PROMPT,
        system_prompt=SYSTEM_PROMPT,
        max_tokens=150)
    print(improved_text)
