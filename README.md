Medibot <br>
🌟 Your Personal Health & Wellness AI Tutor
Medibot is an AI-powered chatbot that provides actionable advice on health, fitness, nutrition, and mental well-being. Powered by OpenAI GPT-4o-mini and built with Streamlit, Medibot delivers personalized wellness insights at your fingertips.
##
🚀 About the Project
Medibot is designed to act as a personal tutor for health and wellness. Whether you want to:

Improve your fitness with effective workout suggestions,
Get tips on a balanced diet,
Discover mindfulness techniques for stress management,
Or optimize your sleep,
Medibot has the answers! 🧠
##
🎯 Features
🧠 AI-Powered Responses:
Leverages OpenAI's GPT-4o-mini for precise and actionable answers.

🏋️ Fitness Advice:
Get tailored workout and yoga suggestions.

🥗 Nutritional Guidance:
Learn about balanced diets, hydration, and healthy habits.

🧘 Mental Wellness Support:
Discover meditation, mindfulness, and stress-relief techniques.

😴 Sleep Optimization:
Improve your sleep patterns with science-backed advice.
##
🛠️ Technology Stack
Technology	Purpose
Streamlit	User Interface for interaction.
OpenAI GPT-4o	Generates AI-powered responses.
Python-dotenv	Manages environment variables securely.
Poetry	Dependency and package management.
Python 3.12+	Core programming language.
##
📂 Project Structure
plaintext
Copy code
medibot/
│<br>
├── medibot.py           # Main chatbot logic and Streamlit app
<br>
├── app.py               # Navigation setup for multi-page app
<br>
├── .env                 # Environment variables (API key)
<br>
├── pyproject.toml       # Poetry dependencies and configuration
<br>
├── README.md            # Project documentation
<br>
└── poetry.lock          # Lock file for dependency management
##
⚙️ Setup Instructions
Follow these steps to run Medibot on your local machine:

1️⃣ Clone the Repository
bash <br>
Copy code <br>
git clone https://github.com/your-username/medibot.git<br>
cd medibot<br>
<br>
2️⃣ Set Up Environment Variables<br>
Create a .env file in the root directory and add your OpenAI API key:
env<br>
Copy code<br>
OPENAI_API_KEY=your_openai_api_key<br>
<br>
3️⃣ Install Dependencies
Use Poetry to install the required libraries:<br>
bash<br>
Copy code<br>
poetry install<br>
If you don't have Poetry installed, run:<br>
bash<br>
Copy code<br>
pip install poetry<br>
<br>
4️⃣ Run the Application
Start the Streamlit application:<br>
bash<br>
Copy code<br>
poetry run streamlit run medibot.py<br><br>
💡 How to Use Medibot<br>
Launch the app using the steps above.<br>
Enter any health or wellness-related question in the input box.<br>
Click on "Get Response".<br>
Medibot will provide a detailed, AI-generated response tailored to your query.<br>
##
📝 Example<br>
User Input:<br>
"What are the benefits of meditation?"<br>

Medibot Response:<br>
"Meditation helps reduce stress, improve concentration, and promote emotional well-being by calming the mind and encouraging mindfulness."<br>
##
Example Response

🔮 Future Enhancements<br>
✅ Integration with nutrition and fitness APIs for real-time data.<br>
✅ User authentication for personalized advice tracking.<br>
✅ Visualizations for progress and health goals.<br>
✅ Enhanced AI features for improved responses.<br>
##
🤝 Contributing<br>
Contributions are always welcome!<br>
Fork the repository.<br>
Create a new branch: git checkout -b feature/YourFeatureName.<br>
Make your changes and commit: git commit -m "Add some feature".<br>
Push the changes: git push origin feature/YourFeatureName.
Submit a pull request.<br><br>
⭐ Support<br>
If you find this project helpful, don't forget to ⭐ star the repository!
