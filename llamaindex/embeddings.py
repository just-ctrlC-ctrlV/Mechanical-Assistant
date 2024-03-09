from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings


# Setting embedding model
def set_emebed_model():
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"
    )