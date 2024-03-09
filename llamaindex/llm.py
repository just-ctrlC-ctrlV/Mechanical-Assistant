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


def connect_llm(api_key):
    """Connects to the Llama language model.

    Args:
        api_key (str): API key for Llama.
    """

    llm = LlamaAPI(api_key=api_key)
    Settings.llm = llm
    return llm