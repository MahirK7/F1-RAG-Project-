from huggingface_hub import InferenceClient

def ask_mistral(question: str, context: str, hf_token: str):
    client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.2", token=hf_token)
    prompt = f"Context:\n{context}\n\nQuestion:\n{question}\nAnswer using only context."
    response = client.chat_completion(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
        temperature=0.2,
    )
    return response.choices[0].message["content"]
