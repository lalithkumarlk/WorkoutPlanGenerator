import streamlit as st
from FitnessPlanGenerator import (
    WorkoutPlanGenerationError,
    FitnessProfile,
    generate_plan,
)

# Configure the page to use wide layout for full screen experience
st.set_page_config(layout="centered")

st.title("Workout Plan Generator")
# This application generates personalized workout plans based on your fitness goals, experience level, available days, equipment access, and any physical limitations you may have


def create_fitness_form():
    """Create and return fitness form inputs."""
    # Select your primary fitness objective to tailor the workout plan to your goals
    # This field is mandatory
    fitness_goal = st.selectbox(
        "Fitness Goal *",
        ["Build Muscle", "Lose Fat", "General Fitness", "Improve Endurance"],
    )
    # Choose your current fitness experience level to ensure appropriate exercise difficulty
    # This field is mandatory
    level = st.selectbox("Experience Level *", ["Beginner", "Intermediate", "Advanced"])
    # Specify how many days per week you can commit to working out
    # This field is mandatory
    days = st.slider("Days Available Per Week *", 1, 7, 3)
    # Select all equipment you have access to for your workouts
    # This field is mandatory
    equipment = list(
        st.multiselect(
            "Equipment Access *", ["No Equipment", "Home Dumbbells", "Full Gym"]
        )
    )
    # Mention any injuries or physical limitations to avoid exercises that may cause discomfort or injury
    # This field is optional
    limitations = st.text_input(
        "Injuries or Limitations (optional)",
        placeholder="e.g. bad knees, no overhead pressing",
    )

    return fitness_goal, level, days, equipment, limitations


def validate_form(fitness_goal, level, days, equipment, limitations):
    """Validate all form fields."""
    # Checks if all mandatory fields (fitness_goal, level, days, equipment) have been filled in
    if not fitness_goal or not level or not days or not equipment:
        st.error("Please fill in all mandatory fields.")
        return False
    return True


def create_fitness_profile(fitness_goal, level, days, equipment, limitations):
    """Create FitnessProfile object from form inputs."""
    # Creates a FitnessProfile object by converting form inputs to uppercase format and organizing them into the required structure
    return FitnessProfile(
        fitness_goal=fitness_goal.upper(),
        level=level.upper(),
        days_per_week=days,
        equipments=[item.upper() for item in equipment],
        limitations=limitations or "",
    )


def display_download_options():
    """Display download format options and download button."""
    # Initialize download format in session state if not present to prevent form resubmission
    # Provides options to download the generated workout plan in either TXT or MD format

    plan = st.session_state.last_generated_plan
    if plan is not None:
        st.success("Your workout plan has been generated successfully!")
        if "download_format" not in st.session_state:
            st.session_state.download_format = "TXT"

        # Use session state to store the selected format without triggering form resubmission
        download_format = st.radio(
            "Select download format:",
            ["TXT", "MD"],
            horizontal=True,
            key="download_format_radio",
        )

        st.session_state.download_format = download_format

        extension = download_format.lower()
        mime_type = "text/plain" if download_format == "TXT" else "text/markdown"

        st.download_button(
            label="Download Workout Plan",
            data=plan,
            file_name=f"workout_plan.{extension}",
            mime=mime_type,
        )


def generate_and_display_plan(fitness_goal, level, days, equipment, limitations):
    """Generate and display the workout plan."""
    # Validates the form inputs, creates a fitness profile, and generates a personalized workout plan using the FitnessPlanGenerator module
    with st.spinner("Generating your personalized workout plan..."):
        try:
            if validate_form(fitness_goal, level, days, equipment, limitations):
                fitnessprofile = create_fitness_profile(
                    fitness_goal, level, days, equipment, limitations
                )
                plan = generate_plan(fitnessprofile)
                if plan:
                    st.session_state.last_generated_plan = plan
        except WorkoutPlanGenerationError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"An error occurred while generating the plan")


# Main form for collecting user fitness information and generating workout plans
with st.form("fitness_form"):
    fitness_goal, level, days, equipment, limitations = create_fitness_form()
    submitted = st.form_submit_button(
        "Generate Plan", disabled=st.session_state.get("generating", False)
    )
    # Process the form submission and generate a personalized workout plan
    if submitted:
        generate_and_display_plan(fitness_goal, level, days, equipment, limitations)

# Display download options outside the form to avoid st.download_button() error
# Shows the generated workout plan and provides download options if a plan has been successfully generated
if "last_generated_plan" in st.session_state and st.session_state.last_generated_plan:
    st.write(st.session_state.last_generated_plan)
    display_download_options()
