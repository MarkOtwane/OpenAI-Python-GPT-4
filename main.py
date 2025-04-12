import openai
import os
import sys

# Load API key from environment
api_key = os.environ.get('OPEN-AI-KEY')

if not api_key:
    sys.stderr.write("""
    You haven't set up your API key yet.

    If you don't have an API key yet, visit:

    https://platform.openai.com/signup

    1. Make an account or sign in
    2. Click "View API Keys" from the top right menu.
    3. Click "Create new secret key"

    Then, set OPENAI_API_KEY as an environment variable.
    """)
    sys.exit(1)

# Set API key
client = openai.OpenAI(api_key=api_key)

# Make the chat completion request
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

# Print the assistant's reply
print(response.choices[0].message.content)
