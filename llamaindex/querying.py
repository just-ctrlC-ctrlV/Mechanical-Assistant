from llama_index import QueryEngine


def query_index(index, query, llm):
    """Queries the index with the given query.

    Args:
        index (VectorStoreIndex): The index to query.
        query (str): The query to perform.
        llm (LlamaAPI): The connected Llama language model.

    Returns:
        dict: The query response.
    """

    query_engine = index.as_query_engine(llm=llm)
    response = query_engine.query(query)
    return response