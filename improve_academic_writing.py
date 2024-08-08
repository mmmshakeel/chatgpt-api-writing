"""
Module to improve academic writing using OpenAI API.
"""

import sys
from openai_client import improve_text

USER_PROMPT = """
I have written an academic essay and would like you to enhance its quality. 
Please revise the text to improve its clarity, coherence, and academic tone while preserving the original meaning. 
I need to ensure that the text is free of grammatical errors, awkward phrasing, and inconsistencies, and that it maintains a formal, academic tone.
Ensure that the language is appropriate for a Master's level paper with an academic tone. 
Do not expand any abbreviations in the text.
Generated text should have English (UK) language output.
Output only the improved text and do not add extra information or explanation about the improvement. 
Here is the text:\n\n
"""

SYSTEM_PROMPT = "You are an english academic writing assistant."

if __name__ == "__main__":
    input_text = sys.argv[1]
    improved_text = improve_text(
        text=input_text,
        user_prompt=USER_PROMPT,
        system_prompt=SYSTEM_PROMPT,
        max_tokens=400)
    print(improved_text)
