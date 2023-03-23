import openai
from PyPDF2 import PdfReader
import csv
def pdf_to_text(file_path):
    # creating a pdf reader object
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)

        # extracting text from all pages
        pdf_data = ""
        for page in reader.pages:
            text = page.extract_text()
            pdf_data += text

        return pdf_data


def textCollector(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data


# Send the extracted text to ChatGPT-3.5


def ask_chatgpt(text, temperature):
    openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = temperature,
        messages=[
            {"role": "user", "content": "identify key insights, trends and their implications for investment decisions. focus on fact, future events and the corresponding date or time range. please be concise but don't important ignore fact."},
            {"role": "user", "content": "help me to extract fact, ignore opinions. for facts, give me the most acurate date. also help me on extract future actions, if there is a date or time range, that would be great."},
            {"role": "user", "content": "extract data into 2 tables. the first table contains the date and the past event happend. the second table contains future action or future event and the corresponding date or estiamted date"},
            {"role": "user", "content": "the following are the real data " + text}
        ],
    )

    return response.choices[0].message.content


text_data = textCollector('./mysite/openai/transcript.txt')
batch_size = 10000
batch_n = round(len(text_data) / batch_size) 
if batch_n == 0:
    batch_n = 1
answer_container = ''

for i in range(batch_n):
    lower_range = i * batch_size
    higher_range = lower_range + batch_size
    print('about to enter the sub session')
    sub_str = text_data[lower_range:higher_range]
    answer = ask_chatgpt(sub_str, 0.2)
    print(answer)
    answer_container = answer_container + answer

final_answer = ask_chatgpt(answer_container, 1)
print(final_answer)

# Split the string into rows
rows = final_answer.split("\n")

# Split each row into columns
data = [row.split(",") for row in rows]

# Open a new CSV file
with open("output.csv", "w", newline="") as csvfile:

    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the data to the CSV file
    for row in data:
        writer.writerow(row)

print("CSV file exported successfully!")







