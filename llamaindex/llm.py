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
from llama_index.core import Settings
import os
import dotenv


# Configuring env variasbles
dotenv.load_dotenv()

llama_api_key = os.getenv("LLAMAAPI")
hf_api_key = os.getenv("HUGGING_FACE_TOKEN")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
db_dimension = os.getenv("DB_DIMENSION")
db_index_name = os.getenv("DB_INDEX_NAME")
db_metric = os.getenv("DB_METRIC")
db_env = os.getenv("DB_ENV")
db_region = os.getenv("DB_REGION")


def connect_llm():
    """Connects to the Llama language model.

    Args:
        api_key (str): API key for Llama.
    """

    llm = LlamaAPI(api_key=llama_api_key)
    Settings.llm = llm
    return llm