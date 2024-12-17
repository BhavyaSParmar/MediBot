Medibot
An AI-Powered Health and Wellness Tutor Bot

##
Medibot is an interactive, AI-driven chatbot designed to offer personalized advice on fitness, nutrition, mental well-being, and overall wellness. Built using Streamlit and powered by the OpenAI GPT-4o-mini model, it delivers actionable health-related insights.
##
🚀 Features
🔹 Interactive Q&A: Ask questions on health, fitness, nutrition, and mental wellness.
🔹 AI-Powered Responses: Uses OpenAI's GPT-4o-mini model for precise, reliable advice.
🔹 Domain-Focused Guidance:
🥗 Nutrition: Balanced diet tips, hydration, and eating habits.
🏋️ Exercise: Workouts, yoga routines, and fitness suggestions.
🧘 Mental Wellness: Meditation, stress management, and mindfulness techniques.
💤 Sleep Improvement: Strategies for better sleep and relaxation.
🩺 Preventive Care: Practical habits for long-term wellness.
🛠 Technologies Used
Technology	Purpose
Streamlit	UI framework for building the interactive app.
OpenAI GPT-4o	AI engine for generating responses.
Python-dotenv	Securely loads environment variables.
Poetry	Dependency management and project packaging.
Python 3.12+	Core programming language.
📂 Project Structure
plaintext
Copy code
medibot/
│
├── medibot.py           # Main chatbot logic and Streamlit app
├── app.py               # Page navigation setup
├── .env                 # Environment variables (API Key)
├── pyproject.toml       # Project dependencies and configuration
├── README.md            # Project documentation
└── poetry.lock          # Dependency lock file
⚙️ How It Works
User Input:
Users type a health-related query into the Streamlit interface.

Processing:

Input is sent to the OpenAI GPT API.
The model processes the query and generates a response.
AI Response:
Medibot responds with practical, domain-specific advice on the user’s query.

Display:
The response is presented interactively within the Streamlit application.

💻 Setup Instructions
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/your-username/medibot.git
cd medibot
2️⃣ Set Up Environment Variables
Create a .env file in the project directory.
Add your OpenAI API key:
env
Copy code
OPENAI_API_KEY=your_openai_api_key
3️⃣ Install Dependencies
Install project dependencies using Poetry:

bash
Copy code
poetry install
If Poetry is not installed, install it using:

bash
Copy code
pip install poetry
4️⃣ Run the Application
Launch the Streamlit app:

bash
Copy code
poetry run streamlit run medibot.py
📝 Example Use Case
User Input:
"What are the benefits of meditation?"

Medibot Response:
"Meditation reduces stress, enhances focus, and promotes emotional well-being by calming the mind and improving overall mental health."

📈 Future Enhancements
✅ Integration with nutrition and fitness APIs for real-time suggestions.
✅ User authentication to save and track personal progress.
✅ Data visualization for user health goals and milestones.
📸 Screenshots
Welcome Screen	Response Example
🛡 License
This project is licensed under the MIT License.

👤 Author
Bhavya Parmar

Connect with me on:

LinkedIn
GitHub
🤝 Contributing
Contributions are welcome!

Fork this repository.
Make your changes.
Open a Pull Request.
🌟 Star this repository if you find it useful!
This structure ensures a clean, visually appealing GitHub README file with appropriate headings, tables, code blocks, and formatting. Replace placeholders like your-username and image paths (path-to-welcome.png) with actual values.
