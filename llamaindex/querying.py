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


def query_index(index, query, llm):
    """Queries the index with the given query.

    Args:
        index (VectorStoreIndex): The index to query.
        query (str): The query to perform.
        llm (LlamaAPI): The connected Llama language model.

    Returns:
        dict: The query response.
    """
    
    qa_prompt_tmpl_str = (
        "Context information is below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Use the context information if the user query is related to it, else use your prior knowledge to answer user query. Only give the answer, dont write anything else"
        "Query: {query_str}\n"
        "Answer: "
    )
    qa_prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)
    
    print("Hello bsdwaalon")
    query_engine = index.as_query_engine(text_qa_template=qa_prompt_tmpl, llm=llm)
    response = query_engine.query(query)
    print("Response :", response)
    return response