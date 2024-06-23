"""
Module to improve email writing using OpenAI API.
"""

import sys
from openai_client import improve_text

USER_PROMPT = """
Help me with improving my writing for email. Always keep the text simple, grammatically correct and easy to understand. 
The improved text should be written in a friendly, professional and engaging tone. Improve the following text:\n\n
"""

SYSTEM_PROMPT = "You are an english writing assistant."

if __name__ == "__main__":
    input_text = sys.argv[1]
    improved_text = improve_text(
        text=input_text,
        user_prompt=USER_PROMPT,
        system_prompt=SYSTEM_PROMPT,
        max_tokens=400)
    print(improved_text)
