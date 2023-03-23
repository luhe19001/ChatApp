import pandas as pd
import wikipedia


#whisper-1 testing. It can get english and Japanese.
import openai
openai.api_key = "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"

audio_file= open("/Users/elainezhao/Downloads/ytmp3free.cc_learn-japanese-minna-no-nihongo-lesson-30-grammar-youtubemp3free.org.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
#

# fine tuning
import jsonlines

data = [
    {'prompt': 'The quick brown fox', 'completion': 'jumps over the lazy dog.'},
    {'prompt': 'In a galaxy far, far away', 'completion': 'there is a war raging between the forces of good and evil.'},
    {'prompt': 'Once upon a time', 'completion': 'there was a beautiful princess who lived in a castle in the middle of a forest.'},
    {'prompt': 'To be or not to be', 'completion': 'that is the question.'},
    {'prompt': 'It was a dark and stormy night', 'completion': 'and the wind was howling through the trees.'},
    {'prompt': 'The cat in the hat', 'completion': 'came back for more mischief and mayhem.'},
    {'prompt': 'I have a dream', 'completion': 'that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."'},
    {'prompt': 'Roses are red', 'completion': 'violets are blue, sugar is sweet, and so are you.'},
    {'prompt': 'All work and no play', 'completion': 'makes Jack a dull boy.'},
    {'prompt': 'We hold these truths to be self-evident', 'completion': 'that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.'},
]

with jsonlines.open('prompts.jsonl', mode='w') as writer:
    writer.write_all(data)

# fine tuning cli:
# export OPENAI_API_KEY=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
# openai api fine_tunes.create -t prompts.jsonl -m ada --suffix "helu_test"
# openai api fine_tunes.results -i ft-WjDrBHaX3cDtW85wT6PDSYaX



model_id = 'ada'

response = openai.FineTune.create(
    model=model_id,
    epochs=10,
    prompt=data,
)


openai api completions.create -m ada -p "All work and no play"

openai api completions.create -m ada:ft-personal:helu-test-2023-03-10-03-41-24 -p "All work and no play"


