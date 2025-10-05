import os
import fastf1
from pipelines.embedding_pipeline import get_embeddings
from pipelines.vector_store import load_vectorstore
from pipelines.rag_pipeline import ask_mistral

# HuggingFace token (use env var in production!)
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# === CONFIG ===
RACE = "australia_2025"
VECTORSTORE_PATH = f"vectorstore/{RACE}/"

# Ensure FastF1 cache
os.makedirs("fastf1_cache", exist_ok=True)
fastf1.Cache.enable_cache("fastf1_cache")

def main():
    print(f"🔎 Loading vectorstore for {RACE}...")
    embeddings = get_embeddings()
    db = load_vectorstore(VECTORSTORE_PATH, embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 4})

    print(f"💬 Ask questions about {RACE} FIA docs (type 'exit' to quit)")
    while True:
        q = input("❓ Your question: ")
        if q.lower() == "exit":
            break

        # Retrieve context
        docs = retriever.invoke(q)
        context = "\n\n".join([d.page_content for d in docs])

        # Ask Mistral
        answer = ask_mistral(q, context, HF_TOKEN)
        print(f"👉 {answer}\n")

if __name__ == "__main__":
    main()
