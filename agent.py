import subprocess
import json
from strands import Agent
from strands.models.ollama import OllamaModel

# Function to list available models
def list_available_models():
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, check=True)
        print("Available models:")
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Failed to list models: {e}")
        return None

# First check what models are available
list_available_models()

# Use a model that's likely to be available
# model_name = "llama2"  # Change from llama3 to llama2, which is more commonly available
model_name = "llama3.2:latest"

# Ensure the model is pulled before using it
try:
    subprocess.run(["ollama", "pull", model_name], check=True)
    print(f"Successfully pulled {model_name} model")
except subprocess.CalledProcessError:
    print(f"Failed to pull {model_name} model. Make sure Ollama is running.")
    exit(1)

# Create a configured Ollama model
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id=model_name
)

# Create an agent with the configured model
agent = Agent(model=ollama_model)

# Use the agent
print(f"Sending request to {model_name}...")
response = agent("Write a short story about an AI assistant.")
print(response)