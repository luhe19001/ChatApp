import os
import openai

#pip install openai[datalib]

# Load your API key from an environment variable or secret management service
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
model = "text-davinci-003"
model = "gpt-3.5-turbo-0301" #10% cost of the previous model.
response = openai.Completion.create(model=model, prompt="tell me usa gpd and inflation in a table format", temperature=0, max_tokens=4000)

response



#example 2, probability threshold. 

prompt = "What is the meaning of life?"
model = "text-davinci-002"
temperature = 1
max_tokens = 100
stop = "\n"

response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    stop=stop,
    n=1,
    logprobs=10
)

probability_threshold = 0.05
chosen_index = 0

for i, choice in enumerate(response.choices[0].logprobs.top_logprobs):
    token = choice['token']
    logprob = choice['logprob']
    if logprob < probability_threshold:
        chosen_index = i
        break

if chosen_index == 0:
    print(response.choices[0].text)
else:
    print("I don't know.")

# embedding
response = openai.Embedding.create(
    input="Your text string goes here",
    model="text-embedding-ada-002"
)
embeddings = response['data'][0]['embedding']
embeddings

# example 3
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)


