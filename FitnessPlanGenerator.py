from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.exceptions import LangChainException
from pydantic import BaseModel
from typing import Literal, Optional
import os

load_dotenv()
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")


EquipmentType = Literal["NO EQUIPMENT", "HOME DUMBBELLS", "FULL GYM"]
GoalType = Literal["BUILD MUSCLE", "LOSE FAT", "GENERAL FITNESS", "IMPROVE ENDURANCE"]
LevelType = Literal["BEGINNER", "INTERMEDIATE", "ADVANCED"]


class WorkoutPlanGenerationError(Exception):
    """
    Custom exception raised when workout plan generation fails.
    
    This exception is used to handle errors that occur during the workout plan
    generation process, including LLM API failures, authentication issues,
    rate limiting, connection problems, and other unexpected errors.
    """

    pass


class FitnessProfile(BaseModel):
    """
    Model representing a user's fitness profile with their goals, level, and constraints.
    
    This class encapsulates all the necessary information about a user's fitness preferences
    and constraints to generate a personalized workout plan. It includes their fitness goals,
    experience level, workout frequency, available equipment, and any physical limitations.
    
    Attributes:
        fitness_goal: The user's primary fitness objective (build muscle, lose fat, general fitness, or improve endurance)
        level: The user's experience level (beginner, intermediate, or advanced)
        days_per_week: Number of days per week the user can commit to working out
        equipments: List of equipment types available to the user
        limitations: Optional string describing any physical limitations or injuries
    """

    fitness_goal: GoalType
    level: LevelType
    days_per_week: int
    equipments: list[EquipmentType]
    limitations: Optional[str] = ""


# Generate Plan using LLM
def generate_plan(inputs: FitnessProfile) -> str:
    """
    Generates a personalized workout plan using an LLM based on the user's fitness profile.
    
    This function takes a FitnessProfile containing the user's fitness goals, experience level,
    available workout days, equipment, and any physical limitations, and uses a language model
    to create a customized workout plan. The plan includes day-by-day breakdowns with exercises,
    sets, reps, and rest periods tailored to the user's specific needs and constraints.
    
    The function handles various error scenarios including authentication failures, rate limiting,
    connection issues, and other unexpected errors, raising a WorkoutPlanGenerationError with
    an appropriate user-friendly message.

    Args:
        inputs: The input data to be sent to the LLM

    Returns:
        A formatted plan with weekly breakdown, day by day
    
    Raises:
        WorkoutPlanGenerationError: If the workout plan generation fails due to LLM errors,
            API issues, or other unexpected problems.
    """
    # Send inputs to LLM
    try:
        print(f"Inputs being sent to LLM: {inputs}")
        # Implementation to send inputs to LLM
        llm = ChatGroq(model=GROQ_MODEL, temperature=0)
        system_prompt = """
                    You are a personal fitness trainer.
        
                    Create a personalized workout plan based strictly on the user's profile.
        
                    Requirements:
                    1. Respect the user's fitness goal, experience level, available days, equipment, and limitations.
                    2. Never recommend equipment that the user does not have.
                    3. Avoid exercises that conflict with stated limitations.
                    4. Create a plan for exactly the requested number of workout days.
                    5. Structure the response day by day.
                    6. For each day, include:
                    - Exercises
                    - Sets
                    - Reps
                    - Rest period
                    7. Keep the recommendations practical and appropriately challenging for the user's experience level.
                    8. Do not make medical diagnoses or medical claims.
                    9. If the user provides an injury or physical limitation, include this disclaimer:
                    "Disclaimer: This workout plan is for general fitness purposes and is not medical advice. Consult a qualified healthcare professional before exercising with an injury or medical condition."
        
                    Return the workout plan in a clear, structured format.
                """
        response = llm.invoke(
            [
                SystemMessage(content=system_prompt),
                HumanMessage(content=f"Create a workout plan for: {inputs}"),
            ]
        )
        return response.content
    except LangChainException as e:
        print(f"LangChain error: {e}")
        raise WorkoutPlanGenerationError(
            f"Unable to generate the workout plan. Please try again"
        ) from e
    except Exception as e:
        print(f"Unexpected error: {e}")
        error = str(e).lower()

        if "401" in error or "api key" in error:
            message = "AI service authentication failed. Please check the API key."

        elif "429" in error or "rate limit" in error:
            message = "The AI service is busy. Please try again in a few moments."

        elif "timeout" in error or "connection" in error:
            message = "Unable to connect to the AI service. Please try again."

        else:
            message = "Unable to generate the workout plan. Please try again."

        raise WorkoutPlanGenerationError(message) from e
