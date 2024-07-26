import streamlit as st
import openai
from PyPDF2 import PdfReader
import io

# Set your OpenAI API key
openai.api_key = 'sk-proj-hvNsbYsSpZSTE02rQU5zT3BlbkFJPSemFNjQ7UspOmKjz7tc'

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to query OpenAI with document context
def query_openai(question, context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}\nAnswer:"}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].message['content'].strip()
    return answer

# Streamlit app
def main():
    st.title("Document Q&A with OpenAI")
    
    # Upload document
    uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")
    
    if uploaded_file is not None:
        # Extract text from uploaded PDF
        context = extract_text_from_pdf(uploaded_file)
        
        # Display the extracted text (for debugging purposes)
        st.subheader("Extracted Text")
        st.write(context[:2000] + "...")  # Display the first 2000 characters for preview
        
        # Ask questions about the document
        st.subheader("Ask a Question")
        question = st.text_input("Enter your question about the document")
        
        if st.button("Get Answer"):
            if question:
                # Query OpenAI with the question and document context
                answer = query_openai(question, context)
                # Display the result
                st.subheader("Answer")
                st.write(answer)
            else:
                st.warning("Please enter a question.")
    
if __name__ == "__main__":
    main()
