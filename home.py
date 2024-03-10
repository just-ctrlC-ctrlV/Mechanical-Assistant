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
from streamlit_chat import message
from public.urls.gear_url import GEAR_URL
from public.urls.fire_url import FIRE_URL
from public.urls.gear1_url import GEAR1_URL


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
set_emebed_model()
llm = connect_llm()

# docs = load_documents("./book")
# upsert_data(pinecone_api_key, db_index_name, docs)

index = load_index(db_index_name)


HUG = 'https://em-content.zobj.net/source/microsoft-teams/363/hugging-face_1f917.png'
ANGRY = 'https://em-content.zobj.net/source/microsoft-teams/363/pouting-face_1f621.png'
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

# Sidebar selection
st.sidebar.title("Select functionality")
selected_option = st.sidebar.selectbox("Choose an option", ("Question Answering", "Summarization", "More (coming soon)"), key="option")


# Title and introduction
st.markdown("""
    <h2 style="text-align: center; color: white; font-size: 3em">Your Mechanical Assistant 👩‍🔧</h2>
""", unsafe_allow_html=True) 
st.markdown("""
    <h4 style="text-align: center; color: #333; padding-bottom: 2.5em">Ask me anything and I'll try my best to answer!</h4>
""", unsafe_allow_html=True)  # Style based on selected theme


st.session_state.value = ''
placeholder = st.empty()
if "question_history" not in st.session_state:
  st.session_state.question_history = []
if "answer_history" not in st.session_state:
  st.session_state.answer_history = []

user_query = st.text_input("", key="text", value=st.session_state.value)
st.session_state.question_history.append(user_query)
if (user_query == ""):
  st.session_state.answer_history.append("")
  pass
else:
  resp = query_index(index, user_query, llm)
  st.session_state.answer_history.append(resp.response)
  user_query = ""
  st.session_state.value = ''
  # message(resp.response, is_user=False, logo=GEAR_URL)
  # query = st.text_input("")
  # st.session_state["text"] = ""
  
n = len(st.session_state.question_history)
for i in range(n):
  if st.session_state.question_history[n-1-i] != "":
    message(st.session_state.question_history[n-1-i], is_user=True, logo=FIRE_URL) # display all the previous questions
  if st.session_state.answer_history[n-1-i] != "":
    message(st.session_state.answer_history[n-1-i], is_user=False, logo=GEAR1_URL) # display all the previous answers
# with placeholder.container():
#   message(st.session_state.question_history[-1], is_user=True) # display the latest message



# Functionality selection
if selected_option == "Question Answering":
  pass
elif selected_option == "Summarization":
  st.write("Summarization functionality is under development.")
else:
  st.write("Stay tuned for more features in the future!")


st.write("<p style='text-align: center; color: #888'>No copyright issue</p>", unsafe_allow_html=True)
