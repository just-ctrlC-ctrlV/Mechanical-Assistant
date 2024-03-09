# Mechanical Assistant Repository

This repository serves as a codebase for a mechanical assistant powered by LLAMA LLM which is implemented using RAG. The assistant utilizes Llamaindex and Streamlit for its functionality.

## Folder Structure

```
Mechanical-Assistant/
├── home.py
├── requirements.txt
└── llamaindex/
    ├── embeddings.py
    ├── indexing.py
    ├── llm.py
    ├── loading_data.py
    ├── main.py
    └── querying.py
```

## Overview

The main aim of this repository is to provide a mechanical assistant application that can assist users with various tasks such as question answering and summarization realted to mechanical engineering. It leverages the LLAMA LLM model and RAG implementation for its core functionality.

## Setup

1. Clone this repository:

   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Ensure you have the necessary environment variables set up, including LLAMAAPI, HUGGING_FACE_TOKEN, PINECONE_API_KEY, DB_DIMENSION, DB_INDEX_NAME, DB_METRIC, DB_ENV, and DB_REGION.

## Usage

To run the Mechanical Assistant application, execute the `home.py` file:

```bash
streamlit run home.py
```

## Functionality

The repository consists of the following key files:

- `home.py`: Contains the main Streamlit application for the Mechanical Assistant.
- `llamaindex/`
  - `embeddings.py`: Handles setting up the embedding model.
  - `indexing.py`: Manages the creation and loading of the index.
  - `llm.py`: Connects to the LLAMA language model.
  - `loading_data.py`: Loads documents and repository data.
  - `main.py`: Main functionality for the assistant application.
  - `querying.py`: Handles querying the index with user input.

## Contributing

Contributions to this repository are welcome. If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).
