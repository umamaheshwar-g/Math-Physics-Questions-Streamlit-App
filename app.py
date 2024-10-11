import os
import streamlit as st  # Import Streamlit for web app interface
from main import MathPhysicsRAG, setup_environment_variables  # Import necessary components from main.py
import json
# from dotenv import load_dotenv
# from mathretrieve import MathPhysicsQuestionDatabase

def main():
    """Main function to run the Streamlit application."""
    setup_environment_variables()  # Set up environment variables
    # load_dotenv()
    openai_api_key = os.environ['OPENAI_API_KEY']  # Get OpenAI API key
    rag_system = MathPhysicsRAG(openai_api_key)  # Initialize the RAG system

    st.title("Math and Physics Question Generator")  # Set the title of the app

    # Sidebar for navigation with styled buttons
    st.sidebar.title("Navigation")
    if st.sidebar.button("Question Generator"):
        st.session_state.page = "question_generator"  # Set the current page
    if st.sidebar.button("Questions Playground"):
        st.session_state.page = "questions_playground"  # Set the current page
    if st.sidebar.button("Custom Question"):
        st.session_state.page = "custom_question"  # Set the current page

    # Render the appropriate page based on the session state
    if 'page' not in st.session_state:
        st.session_state.page = "question_generator"  # Default page

    if st.session_state.page == "question_generator":
        question_generator(rag_system)
    elif st.session_state.page == "questions_playground":
        questions_playground(rag_system)
    elif st.session_state.page == "custom_question":
        custom_question_page(rag_system)

def question_generator(rag_system):
    """Function for the main question generation interface."""
    # User inputs for grade level and topic
    subject = st.selectbox("Subject:", ["Mathematics", "Physics", "Chemistry", "Python"])
    grade_level = st.selectbox("Select Grade Level:", ["Elementary", "Middle School", "High School", "Bachelors", "Masters"])  # Dropdown for grade level
    topic = st.text_input("Enter Topic:", "Python - Monkey Patching Example")  # Text input for topic
    toughness_level = st.selectbox("Select Toughness:", ["Easy", "Moderate", "Tough", "Very Tough"])
    num_variations = st.number_input("Number of Answer Variations:", min_value=1, max_value=10, value=3)  # Input for number of variations

    if st.button("Generate Question Set"):  # Button to trigger question generation
        question_set = rag_system.generate_question_set(subject, grade_level, topic, toughness_level, num_variations)  # Generate question set
        
        # Debug: Check the output of the question set
        st.write("Debug: Generated Question Set:", question_set)

        if not question_set:  # Check if the question set is empty
            st.error("No question set generated. Please try again.")
            return
        
        # Display the question set in a more structured format
        st.subheader("Generated Question Set")
        st.json(question_set)  # Display the generated question set in JSON format

        # Display each part of the question set separately for better clarity
        st.write("### Question:")
        st.write(question_set['question'])
        
        st.write("### Numericals:")
        st.json(question_set['numericals'])
        
        st.write("### Solving Script:")
        st.code(question_set['solving_script'], language='python')
        
        st.write("### Correct Answer:")
        st.json(question_set['correct_answer'])

        answer_variations = question_set['answer_variations']
    
        st.write("#### Incorrect Variations:")
        for variation in answer_variations:
            st.json(variation)  # Display each incorrect variation

def questions_playground(rag_system):
    """Function for the Questions Playground interface."""
    st.subheader("Questions Playground")
    subject = st.selectbox("Subject:", ["Mathematics", "Physics", "Chemistry", "Python"])
    grade_level = st.selectbox("Select Grade Level:", ["Elementary", "Middle School", "High School"])  # Dropdown for grade level
    topic = st.text_input("Enter Topic:", "Physics - Kinematics")  # Text input for topic
    toughness_level = st.selectbox("Select Toughness:", ["Easy", "Moderate", "Tough", "Very Tough"])

    if st.button("Generate Question"):  # Button to trigger question generation
        question = rag_system.generate_question(subject, grade_level, topic, toughness_level)  # Generate a single question
        st.write("### Generated Question:")
        st.write(question)  # Display the generated question

def custom_question_page(rag_system):
    """Function for the Custom Question interface."""
    st.subheader("Custom Question Processing")
    user_question = st.text_area("Enter your question:", height=150)  # Input for user question as a text box

    if st.button("Process Question"):  # Button to trigger processing
        if user_question:
            # Process the question using rag_system
            numericals = rag_system.extract_numericals(user_question)  # Extract numericals
            solving_script = rag_system.generate_solving_script(user_question, numericals)  # Generate solving script
            correct_answer = rag_system.execute_solving_script(solving_script, numericals)  # Execute script to get answer
            
            # Display results
            st.write("### Generated Solving Script:")
            st.code(solving_script, language='python')
            st.write("### Correct Answer:")
            st.json(correct_answer)  # Display the correct answer
        else:
            st.warning("Please enter a question.")  # Warning for empty input

if __name__ == "__main__":
    main()  # Run the main function
