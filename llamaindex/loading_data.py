from simple_directory_reader import SimpleDirectoryReader


def load_data(repo_path: str, required_exts: list[str] = [".tsx", ".ts", ".jsx", ".json"]) -> list:
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