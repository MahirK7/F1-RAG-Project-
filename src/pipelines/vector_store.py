from langchain_community.vectorstores import FAISS

def save_vectorstore(docs, embeddings, path: str):
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(path)
    return db

def load_vectorstore(path: str, embeddings):
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
