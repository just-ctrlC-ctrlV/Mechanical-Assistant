from llama import LlamaAPI, Settings


def connect_llm(api_key):
    """Connects to the Llama language model.

    Args:
        api_key (str): API key for Llama.
    """

    llm = LlamaAPI(api_key=api_key)
    Settings.llm = llm
    return llm