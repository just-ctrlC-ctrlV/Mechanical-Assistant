from pinecone import Pinecone, ServerlessSpec
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import StorageContext
from llama_index.vector_stores.base import VectorStoreIndex




def load_index(pinecone_api_key, db_index_name):
    """Loads a VectorStoreIndex from Pinecone.

    Args:
        pinecone_api_key (str): API key for Pinecone.
        db_index_name (str): Name of the Pinecone index.

    Returns:
        VectorStoreIndex: The loaded index.
    """

    pc = Pinecone(api_key=pinecone_api_key)
    pinecone_index = pc.Index(db_index_name)
    pinecone_vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
    storage_context = StorageContext.from_defaults(vector_store=pinecone_vector_store)

    index = VectorStoreIndex.from_vector_store(
        pinecone_vector_store,
        storage_context=storage_context
    )

    return index



def create_index(pinecone_api_key, db_index_name, all_docs):
    """Create a VectorStoreIndex from Pinecone.

    Args:
        pinecone_api_key (str): API key for Pinecone.
        db_index_name (str): Name of the Pinecone index.
        all_docs : Array of docs to be stored in Pinecone index.

    Returns:
        VectorStoreIndex: The created index.
    """

    pc = Pinecone(api_key=pinecone_api_key)
    pinecone_index = pc.Index(db_index_name)
    pinecone_vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
    storage_context = StorageContext.from_defaults(vector_store=pinecone_vector_store)

    # Store your data to vector store index(data will be automatically converted to vector embeddings)
    index = VectorStoreIndex.from_documents(
        all_docs,
        storage_context=storage_context
    )

    return index