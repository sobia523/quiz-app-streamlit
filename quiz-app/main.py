import streamlit as st
import random
import time

st.title("📓 Quiz Application")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"],
        "answer": "Muhammad Ali Jinnah"
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["English", "Arabic", "Punjabi", "Urdu"],
        "answer": "Urdu"
    },
    {
        "question": "In which year did Pakistan gain independence?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": "1947"
    },
    {
        "question": "What is the national flower of Pakistan?",
        "options": ["Rose", "Jasmine", "Tulip", "Sunflower"],
        "answer": "Jasmine"
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee"
    },
]


if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

# Option selection
selected_option = st.radio("Choose your answer", question["options"], key="answer")

# Handle submit button
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.balloons()
    else:
        st.error(f"❌ Incorrect! The correct answer is {question['answer']}")

    # Wait for a short period before changing the question
    time.sleep(3)

    # Select a new random question from the list
    st.session_state.current_question = random.choice(questions)
    
    # Rerun the app to show the next question
    st.rerun()

