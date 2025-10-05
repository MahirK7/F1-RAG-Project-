🏎️ F1 Race Strategy & Regulations Assistant

Ever wondered if an AI could explain Formula 1 race results, penalties, and strategy calls like an engineer in the paddock?
This project does exactly that.

It’s an end-to-end Retrieval-Augmented Generation (RAG) system that mixes:

📄 FIA documents (stewards’ decisions, scrutineering, race classifications)

⏱️ FastF1 live timing & strategy data (laps, stints, weather, safety cars)

🤖 Large Language Models (Mistral-7B via HuggingFace)

Together, it can answer complex F1 questions — whether it’s about regulations or on-track performance.

🚀 What it can do

Ask about race results
→ “Who finished top 3 in Australia 2025?”
✅ Gets data straight from FastF1.

Ask about FIA decisions
→ “Were there any yellow flag penalties?”
✅ Reads and retrieves from FIA PDFs.

Ask about driver performance
→ “Show Hamilton’s lap times during the Safety Car.”
✅ Combines FIA context + lap-by-lap FastF1 timing.

🧩 How it works (in plain English)

Collect data

FIA PDFs (official docs per race)

FastF1 telemetry (laps, stints, results, weather)

(Optional) Ergast API for historical stats

Build knowledge base

PDFs are converted into text chunks → embedded with HuggingFace MiniLM

Everything is stored in a FAISS vector database

Ask questions

The query engine decides:

If it’s about results/telemetry → FastF1

If it’s about rules/penalties → FIA PDFs via RAG

If it’s mixed → combines both

Get natural answers

Mistral-7B Instruct generates an answer

Always backed by real FIA or FastF1 data

Example Queries
Q: Who finished top 3 in Australia 2025?
A: Lando Norris (McLaren), Max Verstappen (Red Bull), George Russell (Mercedes).

Q: Were there any penalties for yellow flag infringements?
A: Stewards investigated Alexander Albon and Lewis Hamilton. No further action was taken.
(Source: FIA docs)

Q: Show Hamilton’s lap times during the Safety Car.
A: Lap 12–16 all ~1:52s (safety car pace).

🛠️ Tech Behind the Scenes

LLM / Embeddings: HuggingFace, Mistral-7B Instruct, MiniLM-L6-v2

Vector DB: FAISS for semantic search

Data Sources: FastF1 timing feed, FIA PDFs, Ergast API

Frameworks: Python, LangChain, Pandas, Matplotlib

🔮 What’s next

A Streamlit dashboard to make it interactive (tables, charts, chatbot)

Multi-race comparisons (“Who won Australia and Japan 2025?”)

Auto-scraping FIA PDFs for live race weekends

Local model fallback (Flan-T5, Falcon) to avoid API limits

🎯 Why this project matters

This project is more than F1 geekery.
It’s a real-world example of how AI engineers can:

Blend unstructured text (regulations) with structured telemetry

Build trustworthy, explainable hybrid AI systems

Apply RAG techniques to solve domain-specific problems

Think of it as a blueprint for AI systems that can be both smart and reliable.
