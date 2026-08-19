# Workout Plan Generator

A single-page Streamlit app that generates personalized workout plans using AI via the Groq API.

## Setup

1. Clone the repo and navigate to the project folder:
   ```bash
   cd WorkoutPlanGenerator
   ```

2. Activate the virtual environment:
   ```bash
   source /.venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

4. Create a `.env` file with your Groq API key:
   ```
   GROQ_API_KEY=<your_api_key>
   GROQ_MODEL=<model>
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage

Fill in the form with your fitness profile:

- **Fitness Goal** — Build Muscle, Lose Fat, General Fitness, or Improve Endurance
- **Experience Level** — Beginner, Intermediate, or Advanced
- **Days Available Per Week** — 1 to 7
- **Equipment Access** — No Equipment, Home Dumbbells, or Full Gym
- **Injuries or Limitations** *(optional)* — e.g. "bad knees", "no overhead pressing"

Click **Generate Plan** to get a day-by-day weekly workout plan.

## Tech Stack

- Python
- Streamlit
- Groq API (`langchain-groq`)
- LangChain
