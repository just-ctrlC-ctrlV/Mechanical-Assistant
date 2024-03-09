import streamlit as st
import os
import dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
# from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import ChatPromptTemplate, PromptTemplate
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.readers.github import GitHubRepositoryCollaboratorsReader
from llama_index.readers.github import GitHubRepositoryIssuesReader
from llama_index.readers.github import GithubRepositoryReader
from pinecone import Pinecone, ServerlessSpec
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import StorageContext
from llama_index.core import PromptTemplate
from llama_index.llms.llama_api import LlamaAPI
from llamaindex.loading_data import load_documents
from llamaindex.indexing import load_index, create_index
from llamaindex.llm import connect_llm
from llamaindex.querying import query_index
from llamaindex.embeddings import set_emebed_model


# Configuring env variables
dotenv.load_dotenv()

llama_api_key = os.getenv("LLAMAAPI")
hf_api_key = os.getenv("HUGGING_FACE_TOKEN")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
db_dimension = os.getenv("DB_DIMENSION")
db_index_name = os.getenv("DB_INDEX_NAME")
db_metric = os.getenv("DB_METRIC")
db_env = os.getenv("DB_ENV")
db_region = os.getenv("DB_REGION")


# Llamaindex Configuration
# docs = load_documents("")
set_emebed_model(hf_api_key)
llm = connect_llm(llama_api_key)

docs = load_documents("./book")
index = create_index(pinecone_api_key, "bakchodi", docs)

# index = load_index(pinecone_api_key, db_index_name)


# --------------------------------- Streamlit configuration --------------------------------- #
# Title and introduction
st.title("Your Personal Assistant")
st.write("Ask me anything and I'll try my best to answer!")

# Text input for user query
user_query = st.text_input("What's on your mind?", key="query")
print("User query :", user_query)
if (user_query == ""):
  pass
else:
  print("betichod")
  resp = query_index(index, user_query, llm)
  st.write(resp.response)
  
print("\n")
# print("Answer :", type(resp.response))



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
