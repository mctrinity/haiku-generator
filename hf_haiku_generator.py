from transformers import pipeline
import os

# Set your Hugging Face API key (make sure it's available in your environment)
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Ensure authentication with the correct token
generator = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-v0.1",  # Using Mistral 7B
    token=HUGGINGFACE_API_KEY  # Authenticate API requests
)

def generate_haiku(topic):
    """Generates a haiku using Hugging Face models."""
    prompt = f"Write a haiku about {topic}:"
    response = generator(prompt, max_length=30, do_sample=True)
    
    return response[0]["generated_text"].strip()

# Get user input
topic = input("Enter a topic for your haiku: ")
haiku = generate_haiku(topic)

# Print the generated haiku
print("\nGenerated Haiku:\n", haiku)
