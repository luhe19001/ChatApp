import openai
import requests
from io import BytesIO
from PIL import Image
import base64



# Set up OpenAI API credentials
openai.api_key = "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"

def chat_with_gpt3(prompt, model='text-davinci-002', tokens=150):
    conversation_history = [
        {"role": "system", "content": "You are chatting with an AI."},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=conversation_history,
        max_tokens=tokens,
        n=1,
        temperature=0.8,
    )

    return response['choices'][0]['message']['content'].strip()

response = chat_with_gpt3("could you take photo and tell me a story")
print(f"GPT-3: {response}")