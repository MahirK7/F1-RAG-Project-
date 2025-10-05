from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, WebBaseLoader

def load_local_pdfs(path: str):
    loader = DirectoryLoader(path, glob="*.pdf", loader_cls=PyPDFLoader)
    return loader.load()

def load_webpages(urls: list[str]):
    docs = []
    for url in urls:
        docs.extend(WebBaseLoader(url).load())
    return docs
