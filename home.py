import streamlit as st
from transformers import pipeline
import os
import dotenv
from llamaindex.loading_data import load_documents
from llamaindex.indexing import load_index, create_index
from llamaindex.llm import connect_llm
from llamaindex.querying import query_index


# Configuring env variables
dotenv.load_dotenv()

llama_api_key = os.getenv("LLAMAAPI")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
db_dimension = os.getenv("DB_DIMENSION")
db_index_name = os.getenv("DB_INDEX_NAME")
db_metric = os.getenv("DB_METRIC")
db_env = os.getenv("DB_ENV")
db_region = os.getenv("DB_REGION")


# Llamaindex Configuration
docs = load_documents("")
index = load_index(pinecone_api_key, db_index_name)
llm = connect_llm(llama_api_key)


# --------------------------------- Streamlit configuration --------------------------------- #
# Title and introduction
st.title("Your Personal Assistant")
st.write("Ask me anything and I'll try my best to answer!")

# Text input for user query
user_query = st.text_input("What's on your mind?", key="query")

# Display user query
# st.write("You asked:", user_query)
response = query_index(index, user_query, llm)
st.Write("Answer :\n", response)

# Load pipeline for question answering (replace with desired task)
qa_pipeline = pipeline("question-answering")

# Function to process user query and display response
def process_query(query):
  # Replace with your preferred API call or logic
  if query:
    # Use pipeline for question answering (example)
    context = "This is a sample context for demonstration purposes."
    response = qa_pipeline(query, context)
    answer = response["answer"]
  else:
    answer = "Please enter a question."
  return answer

# Display response
st.write("Here's what I found:", process_query(user_query))

# Additional features
# - Sidebar for selecting different functionalities (e.g., question answering, summarization)
st.sidebar.title("Select functionality")
selected_option = st.sidebar.selectbox("Choose an option", ("Question Answering", "Summarization", "More (coming soon)"), key="option")

# - Implement logic based on user selection
if selected_option == "Question Answering":
  # Functionality already implemented
  pass
elif selected_option == "Summarization":
  # Implement summarization logic using libraries like transformers
  st.write("Summarization functionality is under development.")
else:
  st.write("Stay tuned for more features in the future!")

# Display footer
st.write("Made with Streamlit")
