Medibot
An AI-Powered Health and Wellness Tutor Bot
Medibot is an interactive, AI-driven chatbot that serves as a health and wellness tutor. Built with Streamlit and powered by OpenAI GPT-4o, it provides personalized advice on fitness, nutrition, mental well-being, and overall wellness.

Features
Interactive Q&A: Users can ask questions about health, fitness, and mental wellness.
AI-Generated Responses: Leveraging OpenAI's GPT-4o-mini for highly accurate and human-like responses.
Focused Health Domain: System instructions ensure Medibot delivers actionable advice related to:
Nutrition: Balanced diets, hydration, and healthy eating.
Exercise: Workouts, yoga, and personalized fitness tips.
Mental Wellness: Stress management, meditation, mindfulness.
Sleep Improvement: Practical tips to improve sleep quality.
Preventive Care: Education on healthy habits and wellness practices.
Technologies Used
Technology	Purpose
Streamlit	UI framework for building interactive apps.
OpenAI API	Provides responses using GPT-4o-mini.
Python-dotenv	Loads environment variables securely.
Poetry	Dependency management and packaging.
Python (3.12+)	Core programming language.
Project Structure
plaintext
Copy code
medibot/
│
├── medibot.py           # Main chatbot application logic
├── app.py               # Navigation setup for multi-page app
├── .env                 # Environment variables (e.g., API key)
├── pyproject.toml       # Project dependencies and configuration
├── README.md            # Project documentation
└── poetry.lock          # Poetry lock file for dependency management
How It Works
User Input:
Users input their health-related questions into the Streamlit interface.

Backend Processing:

The input is sent to OpenAI's GPT-4o-mini model via API.
System instructions ensure responses are focused on practical health advice.
AI Response:
Medibot generates a relevant, human-like response tailored to the user's query.

Display:
The response is displayed on the Streamlit UI for the user.

Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/medibot.git
cd medibot
2. Set Up Environment
Create a .env file in the project directory.
Add your OpenAI API key:
env
Copy code
OPENAI_API_KEY=your_openai_api_key
3. Install Dependencies
Use Poetry for dependency management:

bash
Copy code
poetry install
If Poetry is not installed, install it with:

bash
Copy code
pip install poetry
4. Run the App
Launch the Streamlit application:

bash
Copy code
poetry run streamlit run medibot.py
Example Use Case
Input:
"What are the benefits of meditation?"

Output:
"Meditation reduces stress, enhances focus, and promotes emotional well-being by calming the mind and improving overall mental health."

Future Enhancements
Integration with fitness and nutrition APIs for real-time suggestions.
User authentication for personalized health tracking.
Enhanced visualizations for wellness progress.
License
This project is licensed under the MIT License.

Author
Bhavya Parmar

For inquiries, feel free to connect with me on GitHub or LinkedIn.

