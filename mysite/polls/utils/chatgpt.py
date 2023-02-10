import openai
api_key = openai.api_key = "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"
# Define the prompt or context for the completion
prompt = "What is the capital of France?"

# Use the completion function to generate completions based on the prompt
completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the first completion from the API response
message = completions.choices[0].text

# Concatenate the previous context and the current completion to form the new prompt
prompt = prompt + " " + message

# Repeat the process to generate a new response based on the previous context
completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the first completion from the API response
message = completions.choices[0].text

# Print the generated completion
print(message)



import requests
import json

# Apply for an API key from OpenAI and paste it below

# Define the API endpoint URL
url = "https://api.openai.com/v1/models"

# Set the API key as a header in the API request
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Send a GET request to the API endpoint
response = requests.get(url, headers=headers)

# Check the status code of the API response
if response.status_code == 200:
    #print(response.json())
    # Write the JSON data to a file
    with open("data.json", "w") as file:
        json.dump(response.json(), file)
    print("success")
else:
    # Print an error message
    print(f"Failed to access API endpoint: {response.status_code}")



