from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
import torch

# Load Hugging Face model pipeline
model_id = "Gensyn/Qwen2.5-0.5B-Instruct"
model = pipeline(
    task="text-generation",
    model=model_id,
    device=0 if torch.cuda.is_available() else -1,
    max_new_tokens=256
)

# Wrap with LangChain
llm = HuggingFacePipeline(pipeline=model)

# Simple prompt template (no history)
template = PromptTemplate.from_template(
    """You are Jarvis, a highly knowledgeable and reliable assistant created to help Deepika.

Your role:
- Always give factual, accurate answers.
- If you are not sure, say "I'm not fully sure about that" instead of guessing.
- Keep your tone friendly, helpful, and respectful.
- Avoid going off-topic or giving unrelated suggestions.

Formatting rules:
- Answer in 3–5 clear sentences.
- Do not recommend movies, books, or random things unless the user asks.
- Structure answers logically: introduction → explanation → conclusion.

User: {input}
Jarvis:"""
)


# Conversation chain setup
chain = template | llm


def huggingfacemodel(output_text):
    user_input = output_text

    if user_input.lower() in ['exit', 'quit', 'bye']:
        return "Jarvis: Goodbye Deepu! See you soon 😄"

    # Invoke the chain
    response = chain.invoke({"input": user_input})

    # Handle pipeline output correctly
    if isinstance(response, list) and "generated_text" in response[0]:
        response_text = response[0]["generated_text"]
    else:
        response_text = str(response)

    # --- CLEAN THE OUTPUT ---
    if "Jarvis:" in response_text:
        response_text = response_text.split("Jarvis:")[-1].strip()
    if "User:" in response_text:
        response_text = response_text.split("User:")[0].strip()

    return f"Jarvis: {response_text}"






