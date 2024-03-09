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
from llamaindex.indexing import load_index, create_index, upsert_data
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
# PINECONE_API_KEY=8df36291-9b0f-4081-95fc-3d4dbe03b6ff

# Llamaindex Configuration
# docs = load_documents("")
set_emebed_model()
llm = connect_llm()

# docs = load_documents("./book")
# upsert_data(pinecone_api_key, db_index_name, docs)

index = load_index(db_index_name)

# --------------------------------- Streamlit configuration --------------------------------- #
st.set_page_config(
    page_title="Mech Assistant",
    page_icon="👩‍🔧",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.sidebar.title("Select functionality")
selected_option = st.sidebar.selectbox("Choose an option", ("Question Answering", "Summarization", "More (coming soon)"), key="option")


# Title and introduction
st.markdown("""
    <h2 style="text-align: center; color: white; font-size: 3em">Your Mechanical Assistant 👩‍🔧</h2>
""", unsafe_allow_html=True) 
st.markdown("""
    <h4 style="text-align: center; color: #333; padding-bottom: 2.5em">Ask me anything and I'll try my best to answer!</h4>
""", unsafe_allow_html=True)  # Style based on selected theme


# Text input for user query
user_query = st.text_input("What's on your fucking mind?", key="query")
if (user_query == ""):
  pass
else:
  print("betichod")
  resp = query_index(index, user_query, llm)
  st.write(resp.response)


if selected_option == "Question Answering":
  pass
elif selected_option == "Summarization":
  st.write("Summarization functionality is under development.")
else:
  st.write("Stay tuned for more features in the future!")


st.write("<p style='text-align: center; color: #888'>No copyright issue</p>", unsafe_allow_html=True)
