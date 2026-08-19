# Product Requirements Document (PRD)
# Workout Plan Generator

## 1. Product Overview

### 1.1 Product Name
Workout Plan Generator

### 1.2 Product Vision
A single-page Streamlit application that generates personalized workout plans using AI, providing users with actionable, constraint-aware fitness guidance comparable to what they would receive from a personal trainer.

### 1.3 Target Audience
- Fitness enthusiasts seeking structured workout plans
- Beginners looking for guidance on starting their fitness journey
- Intermediate and advanced users wanting customized training programs
- Users with specific constraints (equipment limitations, injuries, time availability)

## 2. Product Objectives

### 2.1 Primary Goals
- Deliver personalized, usable workout plans based on user-specific inputs
- Demonstrate effective prompt engineering for LLM-based applications
- Provide a reliable, error-resistant user experience
- Generate structured, day-by-day workout schedules that users can immediately follow

### 2.2 Success Criteria
- Application runs without crashes on invalid or empty inputs
- Generated plans respect all user-specified constraints
- Plans are structured and immediately actionable
- Graceful error handling for all failure scenarios

## 3. Functional Requirements

### 3.1 User Input Collection
The application must collect the following structured inputs:

#### 3.1.1 Required Inputs
- **Fitness Goal** (Dropdown selection)
  - Options: Build muscle / Lose fat / General fitness / Improve endurance
  
- **Experience Level** (Dropdown selection)
  - Options: Beginner / Intermediate / Advanced
  
- **Days Available Per Week** (Slider or number input)
  - Range: 1-7 days
  
- **Equipment Access** (Dropdown or multiselect)
  - Options: No equipment / Home dumbbells / Full gym

#### 3.1.2 Optional Inputs
- **Injuries or Limitations** (Free text field)
  - Examples: "bad knees", "no overhead pressing"
  - Should trigger appropriate disclaimers in output

### 3.2 Plan Generation

#### 3.2.1 Generate Plan Button
- Triggers the workout plan generation process
- Sends all collected inputs to the LLM via Groq API
- Displays results in a clearly formatted area

#### 3.2.2 Output Format
- Weekly breakdown structure
- Day-by-day schedule
- Exercise details including sets and reps
- Structured, not wall-of-text format

### 3.3 Core Function Requirements

#### 3.3.1 Plan Generation Function
Must include:
- Type hints for all parameters
- Structured input parameters matching user inputs
- Well-designed prompt construction
- Groq API integration
- try/except error handling wrapper
- Return formatted response

### 3.4 Error Handling Requirements

#### 3.4.1 Input Validation
- Handle missing inputs with friendly messages
- Validate invalid inputs (e.g., 0 days selected)
- Prevent application crashes from bad input

#### 3.4.2 API Error Handling
- Handle bad API keys gracefully
- Manage network issues with user-friendly messages
- Handle rate limiting scenarios
- Provide fallback messages for API failures

#### 3.4.3 Response Validation
- Detect empty LLM responses
- Handle malformed responses
- Provide friendly fallback messages

## 4. Non-Functional Requirements

### 4.1 Prompt Design Requirements
The system prompt must:
- Enforce constraint respect (equipment, injuries, days/week)
- Generate structured output format
- Maintain appropriate scope (no medical claims)
- Include disclaimers for injury-related inputs
- Be iteratively tested and refined

### 4.2 Code Quality Requirements
- Python functions with type hints
- Proper function separation and modularity
- Readable, maintainable code structure
- Comprehensive try/except blocks

### 4.3 User Experience Requirements
- Single-page application design
- Clear, intuitive input interface
- Formatted output display area
- Friendly error messages (no technical jargon)

## 5. Technical Stack

### 5.1 Required Technologies
- **Python**: Core programming language
- **Streamlit**: UI framework
- **Groq API**: LLM integration

### 5.2 Key Libraries
- Type hints (typing module)
- Exception handling (try/except)
- Streamlit components

## 6. Optional Features (Stretch Goals)

### 6.1 Plan Regeneration
- "Regenerate" button for alternative plan variations
- Maintains same constraints, generates different exercises

### 6.2 Session Persistence
- Store generated plan in st.session_state
- Persist across application reruns

### 6.3 Export Functionality
- Download plan as .txt file
- Download plan as .md file

### 6.4 Exercise Swap Feature
- Allow users to swap individual exercises
- Maintain overall plan structure

## 7. Acceptance Criteria

### 7.1 Weighted Evaluation Criteria

| Criteria | Weight | Requirements |
|----------|--------|--------------|
| Crash Prevention | 20% | App runs without crashing on empty or invalid input |
| Input Structure | 25% | Inputs are structured and correctly passed into prompt |
| Prompt Design | 30% | Plan respects constraints, is well-structured, and genuinely usable |
| Error Handling | 15% | Handles API failures and malformed responses |
| Code Quality | 10% | Type hints, function separation, readability |

### 7.2 Minimum Viable Product (MVP)
- All required inputs implemented
- Generate Plan button functional
- Basic error handling for all scenarios
- Structured output format
- Type-hinted Python function
- Groq API integration

## 8. Delivery Requirements

### 8.1 Submission Format
- Public GitHub repository
- Repository link submitted via course platform
- Session: Session 2 – LLMs, Embeddings & Transformer Architecture

### 8.2 Repository Contents
- Complete Streamlit application code
- Requirements.txt or dependencies file
- README with setup instructions
- Any necessary configuration files

## 9. Constraints and Assumptions

### 9.1 Constraints
- Single-page application only
- Must use Groq API (not other LLM providers)
- Must use Streamlit for UI

### 9.2 Assumptions
- Users have valid Groq API access
- Users have basic understanding of fitness terminology
- Internet connectivity available for API calls

## 10. Future Considerations
- Multi-week progressive plans
- Integration with fitness tracking apps
- User accounts and plan history
- Community sharing features
- Video demonstrations for exercises
