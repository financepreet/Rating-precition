import streamlit as st
import json
from langchain_groq import ChatGroq

# 1. Set up your Groq API key (replace with your actual key or use environment variables)
# For demonstration, directly including the key, but using environment variables is recommended for production.
GROQ_API_KEY = "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" # Replace with your actual key

# 2. Initialize the ChatGroq LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b", # Use the same model as in previous steps
    temperature=0,
    groq_api_key=GROQ_API_KEY
)

# 3. Create a Streamlit application with a title
st.title("Review Sentiment Analyzer")
st.markdown("Enter a review below and get a predicted star rating and explanation from the LLM.")

# 4. Add a text area widget for users to input their review text 
review_text = st.text_area("Enter your review here:", height=200)

# 5. Add a button that, when clicked, will trigger the LLM prediction
if st.button("Analyze Review"):
    if review_text:
        with st.spinner("Analyzing sentiment..."):
            # a. Construct a prompt for the LLM
            prompt = f"Review: {review_text}\n\nAnalyze this review and provide a summary of the sentiment in JSON format with the keys \"predicted_stars\" (an integer from 1 to 5 based on the sentiment) and \"explanation\" (a brief reasoning for the assigned rating)."

            # b. Invoke the LLM with the constructed prompt
            response = llm.invoke(prompt)

            try:
                # c. Parse the LLM's JSON response
                llm_output = json.loads(response.content)
                predicted_stars = llm_output.get("predicted_stars")
                explanation = llm_output.get("explanation")

                # d. Display the predicted stars and explanation
                st.subheader("Analysis Result:")
                st.metric(label="Predicted Stars", value=f"{predicted_stars} / 5")
                st.info(f"**Explanation:** {explanation}")

            except json.JSONDecodeError:
                st.error("Failed to parse LLM response. Please try again or check the response format.")
                st.code(response.content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.code(response.content)
    else:
        st.warning("Please enter a review to analyze.")

# To run this Streamlit app, save the code as a .py file (e.g., app.py) and run `streamlit run app.py` in your terminal.