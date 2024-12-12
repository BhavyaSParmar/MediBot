import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")



# Set up OpenAI client using environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

client = OpenAI(api_key=api_key)

# Define a function to interact with OpenAI API using the latest GPT-4o-mini model
def get_medibot_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Use the available model
            messages=[
                {"role": "system", "content": "You are Medibot, a health and wellness tutor focused on providing practical advice about nutrition, exercise, and mental well-being."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=300,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"






# Streamlit UI for medibot
st.markdown("<h1 style='text-align: center;'>Welcome to Medibot</h1>", unsafe_allow_html=True)
st.write("Ask me anything about health, fitness, nutrition, and mental wellness! I'm using the latest GPT-4o model for enhanced responses.")

# Input box for user to ask questions
user_input = st.text_input("Enter your question about health & wellness:")

# Button to get response from medibot
if st.button("Get Response"):
    if user_input:
        # Fetch response from OpenAI
        response = get_medibot_response(user_input)
        # Display the response
        st.write("**Medibot:**")
        st.write(response)
    else:
        st.warning("Please enter a question to get started.")

# Additional section to provide context about what medibot can do
st.write("---")
st.write("**What can you ask Medibot?**")
st.write("- Learn about balanced diets, exercise routines, and mental wellness tips.")
st.write("- Understand the benefits of meditation and stress management techniques.")
st.write("- Get personalized advice on improving sleep, hydration, and fitness.")
st.write("- Explore the science behind healthy habits and preventive care.")
st.write("- Learn about mindfulness, yoga, and nutrition for overall well-being.")