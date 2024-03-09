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


def load_repo_data(repo_path, required_exts=[".tsx", ".ts", ".jsx", ".json"]):
    """Loads documents from the specified directory.

    Args:
        repo_path (str): Path to the directory containing the documents.
        required_exts (list[str], optional): List of required file extensions. Defaults to [".tsx", ".ts", ".jsx", ".json"].

    Returns:
        list: A list of loaded documents.
    """

    reader = SimpleDirectoryReader(
        input_dir=repo_path,
        required_exts=required_exts,
        recursive=False,
    )

    all_docs = []
    for docs in reader.iter_data():
        try:
            all_docs.extend(docs)
        except FileNotFoundError:
            pass

    return all_docs



def load_documents(directory_path, file_types=None, recursive=True, exclude=None):
  """
  Loads documents from a directory using SimpleDirectoryReader, filtering by file types.

  Args:
      directory_path: Path to the directory containing documents.
      file_types: List of file extensions to include (e.g., [".pdf", ".docx"]).
                  If none specified, all supported file types are loaded.
      recursive: Whether to read files from subdirectories (default: False).
      exclude: List of file paths to exclude (default: None).

  Returns:
      List of Document objects loaded from the directory.
  """

  required_exts = file_types if file_types else None  # Set required extensions based on input

  reader = SimpleDirectoryReader(
      input_dir=directory_path,
      recursive=recursive,
      exclude=exclude,
      required_exts=required_exts,  # Pass the extensions to the reader
  )

  # Load documents using either load_data or iter_data depending on use case
  all_docs = []
  for docs in reader.iter_data():
    try:
        all_docs.extend(docs)
    except FileNotFoundError:
        pass

  return all_docs
