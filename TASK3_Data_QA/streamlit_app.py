import streamlit as st
import pandas as pd

st.title("ChatGPT for Data Q&A")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")

    st.dataframe(df)

    question = st.text_input(
        "Ask a Question About Dataset"
    )

    if st.button("Get Answer"):

        question_lower = question.lower()

        if "highest" in question_lower and "math" in question_lower:

            top_student = df.loc[df["Math"].idxmax()]

            answer = f"{top_student['Student']} scored highest in Math with {top_student['Math']} marks."

        elif "lowest" in question_lower and "math" in question_lower:

            low_student = df.loc[df["Math"].idxmin()]

            answer = f"{low_student['Student']} scored lowest in Math with {low_student['Math']} marks."

        elif "average" in question_lower and "math" in question_lower:

            avg = df["Math"].mean()

            answer = f"Average Math marks are {avg:.2f}"

        elif "highest" in question_lower and "science" in question_lower:

            top_student = df.loc[df["Science"].idxmax()]

            answer = f"{top_student['Student']} scored highest in Science with {top_student['Science']} marks."

        else:

            answer = "Question not recognized."

        st.success(answer)