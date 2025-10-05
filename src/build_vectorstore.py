import os
from pipelines.data_loader import load_local_pdfs, load_webpages
from pipelines.embedding_pipeline import split_documents, get_embeddings
from pipelines.vector_store import save_vectorstore
from langchain_community.document_loaders import TextLoader
import glob

# === CONFIG ===
RACE = "australia_2025"
RAW_DATA_PATH = f"data/raw/{RACE}/"
PROCESSED_TXT_PATH = "notebooks/fastf1_cache/2023/2023-04-02_Australian_Grand_Prix/2023-04-02_Race/"
VECTORSTORE_PATH = f"vectorstore/{RACE}/"

# Example FIA/F1 race report URLs (replace with actual)
URLS = [
    "https://www.fia.com/documents/australia-2025-fp1-report",
    "https://www.fia.com/documents/australia-2025-race-report"
]

def load_txt_files(path):
    """Load all .txt files in a folder into LangChain documents."""
    docs = []
    for file in glob.glob(os.path.join(path, "*.txt")):
        loader = TextLoader(file, encoding="utf-8")
        docs.extend(loader.load())
    return docs

def main():
    print(f"📂 Loading documents for {RACE}...")

    # Load PDFs
    local_docs = load_local_pdfs(RAW_DATA_PATH)

    # Load FIA/F1 web pages
    web_docs = load_webpages(URLS)

    # Load FastF1/Ergast txt exports
    txt_docs = load_txt_files(PROCESSED_TXT_PATH)

    # Combine everything
    all_docs = local_docs + web_docs + txt_docs
    print(f"✅ Loaded {len(all_docs)} documents "
          f"({len(local_docs)} PDFs, {len(web_docs)} web, {len(txt_docs)} txt)")

    # Split into chunks
    chunks = split_documents(all_docs)
    print(f"✂️ Split into {len(chunks)} chunks")

    # Embeddings
    embeddings = get_embeddings()

    # Save vectorstore
    os.makedirs(VECTORSTORE_PATH, exist_ok=True)
    save_vectorstore(chunks, embeddings, VECTORSTORE_PATH)
    print(f"💾 Vectorstore saved to {VECTORSTORE_PATH}")

if __name__ == "__main__":
    main()
