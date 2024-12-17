# MediBot
Medibot is an interactive, AI-driven chatbot that serves as a health and wellness tutor. Built with Streamlit and integrated with the OpenAI GPT-4o model, Medibot provides personalized advice on topics such as fitness, nutrition, and mental well-being. Below is a detailed breakdown of the project's components and technology stack:

Core Functionalities:
User Interaction:

Users can input health, fitness, and wellness-related questions into the Streamlit interface.
Upon submission, Medibot provides concise, GPT-powered responses tailored to practical advice.
AI Integration:

The chatbot leverages OpenAI's GPT-4o-mini model for generating human-like and contextually relevant answers.
A system prompt ensures Medibot stays focused on providing actionable and health-focused information.
Practical Advice Areas:

Nutrition tips (e.g., balanced diets, hydration).
Exercise guidance (e.g., workouts, yoga).
Mental health advice (e.g., mindfulness, meditation, stress management).
Sleep improvement suggestions.
Preventive care and wellness education.
Technologies Used:
Streamlit (UI Framework):

Provides a simple and clean user interface for interacting with the Medibot.
Users can input queries, click buttons to trigger responses, and see answers instantly.
Streamlit Pages allows navigation within the app (handled via app.py).
OpenAI GPT API:

Medibot communicates with the OpenAI API via the openai library to fetch responses.
The GPT-4o-mini model is specifically used for optimized performance and enhanced responses.
Environment variables securely store the API key in a .env file.
Python-Dotenv:

Used to load sensitive environment variables such as the OPENAI_API_KEY securely.
Poetry (Dependency Management):

The project dependencies (e.g., openai, streamlit, python-dotenv) are managed through Poetry.
The pyproject.toml file includes clear definitions of all required packages.
Session State:

Handled in app.py for managing page navigation within the Streamlit application.
File Structure Overview:
medibot.py:

The main application logic for the chatbot.
Handles user input, API communication, and response display.
Includes health-related system instructions for GPT to maintain domain relevance.
app.py:

Handles multi-page navigation and session management.
Provides structure for integrating the Medibot into a broader app environment.
.env:

Stores the OpenAI API key securely.
Prevents hardcoding sensitive information into the script.
pyproject.toml:

Defines project dependencies and metadata.
Ensures a clean and reproducible environment for the project.
README.md:

Provides a brief overview of the Medibot project and its purpose.
How It Works:
User Experience:

The user opens the Streamlit app and sees a clean, welcoming interface.
Inputs a health-related question (e.g., "How can I improve my sleep?").
Clicks "Get Response" to fetch advice.
Backend Processing:

The input is sent to the OpenAI GPT API with Medibot's system instructions.
GPT-4o processes the query and generates a relevant response.
Output Display:

The generated advice is displayed in the Streamlit app for the user.
Example Use Case:
User Input: "What are the benefits of meditation?"
Medibot Response: "Meditation reduces stress, enhances focus, and promotes emotional well-being by calming the mind and improving overall mental health."
Target Audience:
Individuals seeking practical and reliable health advice.
Users interested in wellness topics such as diet, fitness, and mental health.
Those looking for instant, AI-powered guidance in a user-friendly format.
Conclusion:
Medibot combines modern AI technology with an intuitive user interface to provide users with accessible and actionable health advice. This project leverages the strengths of OpenAI GPT-4o, Streamlit, and Poetry, creating a scalable, efficient, and interactive wellness tool.
