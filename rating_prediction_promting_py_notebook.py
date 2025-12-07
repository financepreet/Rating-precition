

import pandas as pd
import numpy as np

!unzip "/content/yelp.csv.zip"

data = pd.read_csv("/content/yelp.csv")

data.head()

pip install -qU langchain-groq

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    groq_api_key = "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"
)

data2 = data[['text', 'stars']]

data2.head()

# Iterate through data2 and pass to the LLM model
print("Processing the first 5 rows of data2:")
for index, row in data2.head(1).iterrows():
    review_text = row['text']
    review_stars = row['stars']

    # Construct the prompt for the LLM, requesting JSON output
    prompt = f"Review: {review_text}\nStars: {review_stars}\n\nAnalyze this review and provide a summary of the sentiment in JSON format with the keys \"predicted_stars\" (an integer from 1 to 5 based on the sentiment) and \"explanation\" (a brief reasoning for the assigned rating)."

    print(f"--- Review {index + 1} ---")
    print(f"Prompt sent to LLM:\n{prompt}")

    # Invoke the LLM
    response = llm.invoke(prompt)
    print(f"LLM Response:\n{response.content}\n")

# Define your custom review and actual star rating
my_review_text = "it was vey bad"
my_review_stars = 5 # This is the actual star rating you would give

# Construct the prompt for the LLM, requesting JSON output
prompt = f"Review: {my_review_text}\nStars: {my_review_stars}\n\nAnalyze this review and provide a summary of the sentiment in JSON format with the keys \"predicted_stars\" (an integer from 1 to 5 based on the sentiment) and \"explanation\" (a brief reasoning for the assigned rating)."

print("--- Your Custom Review ---")
print(f"Prompt sent to LLM:\n{prompt}")

# Invoke the LLM
response = llm.invoke(prompt)
print(f"LLM Response:\n{response.content}\n")

# Define your custom review and actual star rating
my_review_text = "The service was so slow and the food was cold by the time it arrived. A truly terrible experience."
my_review_stars = 0 # This is the actual star rating you would give (for comparison, not for the LLM's input)

# Construct the prompt for the LLM, requesting JSON output
prompt = f"Review: {my_review_text}\n\nAnalyze this review and provide a summary of the sentiment in JSON format with the keys \"predicted_stars\" (an integer from 1 to 5 based on the sentiment) and \"explanation\" (a brief reasoning for the assigned rating)."

print("--- Your Custom Review ---")
print(f"Prompt sent to LLM:\n{prompt}")

# Invoke the LLM
response = llm.invoke(prompt)
print(f"LLM Response:\n{response.content}\n")

# Define your custom review and actual star rating
my_review_text = "Great atmosphere and the staff was very friendly. The appetizer was a little small, but overall a wonderful night out."
my_review_stars = 0 # This is the actual star rating you would give (for comparison, not for the LLM's input)

# Construct the prompt for the LLM, requesting JSON output
prompt = f"Review: {my_review_text}\n\nAnalyze this review and provide a summary of the sentiment in JSON format with the keys \"predicted_stars\" (an integer from 1 to 5 based on the sentiment) and \"explanation\" (a brief reasoning for the assigned rating)."

print("--- Your Custom Review ---")
print(f"Prompt sent to LLM:\n{prompt}")

# Invoke the LLM
response = llm.invoke(prompt)
print(f"LLM Response:\n{response.content}\n")

# Define your custom review and actual star rating
my_review_text = "th food was good and the staff was good but the serving time was very bad"
my_review_stars = 0 # This is the actual star rating you would give (for comparison, not for the LLM's input)

# Construct the prompt for the LLM, requesting JSON output
prompt = f"Review: {my_review_text}\n\nAnalyze this review and provide a summary of the sentiment in JSON format with the keys \"predicted_stars\" (an integer from 1 to 5 based on the sentiment) and \"explanation\" (a brief reasoning for the assigned rating)."

print("--- Your Custom Review ---")
print(f"Prompt sent to LLM:\n{prompt}")

# Invoke the LLM
response = llm.invoke(prompt)
print(f"LLM Response:\n{response.content}\n")



pip show langchain_groq

