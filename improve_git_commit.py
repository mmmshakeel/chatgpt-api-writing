"""
Module to improve git commits using OpenAI API.
"""

import sys
from openai_client import improve_text

USER_PROMPT = """
Help me with improving my writing for git commit messages.
Always keep the text simple, grammatically correct and easy to understand.
Keep the commit clear and to the point.
Follow best practices and character counts for git commit message.
Only output the improved git commit message.
Do not remove any tags with []. For example, if the commit message has [Fix],
Then the improved git commit message should contain the [Fix] in the beginning of the improved text.

An example improved git commit message is:
[Feature] Add module to improve git commit messages using OpenAI API

- Implement `improve_git_commit.py` to enhance git commit messages.
- Define user and system prompts for improving commit messages.
- Use `improve_text` function from `openai_client` to process input text.

Improve the git commit text:\n\n
"""

SYSTEM_PROMPT = "You are a seasoned developer and an assistant in writing git commit messages."

if __name__ == "__main__":
    input_text = sys.argv[1]
    improved_text = improve_text(
        text=input_text,
        user_prompt=USER_PROMPT,
        system_prompt=SYSTEM_PROMPT,
        max_tokens=400)
    print(improved_text)
