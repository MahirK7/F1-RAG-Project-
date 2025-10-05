🏎️ F1 Race Strategy & Regulations Assistant (RAG + LLM + FastF1)

An end-to-end Retrieval-Augmented Generation (RAG) system that combines official FIA documents, live timing/strategy data via FastF1, and historical results to answer complex Formula 1 questions.

This project showcases AI engineering, data engineering, and sports analytics, blending LLMs, vector databases, and structured APIs into one hybrid query system.

🚀 Features

Document Retrieval (RAG)

FIA scrutineering reports, stewards’ decisions, and race classification PDFs.

Preprocessed into text chunks and embedded with HuggingFace models.

Stored in FAISS vectorstore for semantic search.

Structured Data (FastF1)

Official race results (classification, DNFs, penalties).

Lap-by-lap timing data for any driver.

Tyre stint analysis and pit stop strategies.

Weather conditions and safety car / VSC phases.

Hybrid Query Engine

Routes questions intelligently:

“Who finished top 3 in Australia 2025?” → FastF1

“Were there any yellow flag penalties?” → FIA PDFs (via RAG)

“Show Hamilton’s lap times during the Safety Car” → Combined

Powered by Mistral-7B Instruct via HuggingFace Inference API.

Multi-Race Support

Currently supports Australia, China, and Japan 2025.

Modular design to easily add new GPs.

Processed Exports

FIA PDFs → fia_docs_*.txt

FastF1 race results → ergast_clean.csv

FastF1 laps → fastf1_laptimes.parquet

Ergast / historical results (optional)


data/
 ├── raw/           # FIA PDFs per race
 ├── processed/     # Cleaned .txt, .csv, .parquet outputs
 └── vectorstore/   # FAISS indexes (per race)

src/
 ├── build_vectorstore.py   # Builds embeddings + FAISS
 ├── query_vectorstore.py   # Interactive Q&A
 └── pipelines/             # Modular pipeline components
      ├── data_loader.py
      ├── embedding_pipeline.py
      ├── rag_pipeline.py
      ├── vector_store.py
      └── fastf1_pipeline.py


🛠️ Tech Stack

LLM / Embeddings

HuggingFace Transformers

Mistral-7B-Instruct (via HuggingFace Inference API)

all-MiniLM-L6-v2 embeddings

Vector Database

FAISS
 for semantic search

Data Sources

FastF1
 for official timing, stints, weather

FIA PDFs (scrutineering reports, stewards’ decisions, race results)

Ergast API (optional historical data)

Frameworks / Tools

Python 3.11

LangChain for document loaders & splitting

Pandas for data wrangling

Matplotlib for lap time & stint charts


⚙️ How It Works

Build Phase (build_vectorstore.py)

Load FIA PDFs (data/raw/<race>/*.pdf).

Load processed .txt, .csv, .parquet from FastF1/Ergast pipelines.

Split into text chunks with RecursiveCharacterTextSplitter.

Embed with HuggingFace MiniLM.

Save FAISS vectorstore to vectorstore/<race>/.

Query Phase (query_vectorstore.py)

Load FAISS vectorstore(s).

Accept user query.

If query matches race results / stints / timing / weather → call FastF1 pipeline.

Else → retrieve docs from FAISS and query Mistral LLM.

Combine answers into one natural language response with sources.

📊 Example Queries

Q: Who finished top 3 in Australia 2025?
A: Lando Norris (McLaren), Max Verstappen (Red Bull), George Russell (Mercedes).

Q: Were there any penalties for yellow flag infringements?
A: FIA stewards investigated Alexander Albon and Lewis Hamilton. No further action was taken. (source: fia_docs_australia2025.pdf)

Q: Show Hamilton’s lap times during the Safety Car.
A: (Table of lap times 12–16 with reduced pace, pulled from FastF1 + FIA context).

🔮 Possible Extensions

Streamlit dashboard with tabs:

FIA Doc Q&A (chatbot)

Race Results (tables)

Lap Charts (matplotlib/plotly)

Tyre Strategy Visuals (stint charts)

Multi-GP comparisons (“Who won Australia and Japan 2025?”).

Automated FIA scraping for live updates.

Local model fallback (Flan-T5, Falcon) to bypass HuggingFace quota.

🎯 Skills Demonstrated

LLM Applications: Retrieval-Augmented Generation (RAG), prompt design, hallucination control.

Vector Search: FAISS indexing, HuggingFace embeddings, document chunking.

Data Engineering: Pipeline building, PDF parsing, text serialization, cache management.

APIs & External Data: FastF1 timing feed, FIA PDFs, Ergast API.

MLOps Awareness: Caching, error handling, quota management, scalability.

Visualization: Lap time charts, stint plots, weather overlays.

📌 Why This Project

This project demonstrates how AI engineers can blend LLMs with structured data to solve domain-specific problems. By combining regulatory text retrieval (RAG) with live telemetry APIs, it shows how to build a trustworthy, hybrid AI system that is accurate, explainable, and production-ready.