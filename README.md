# Strands AI Project

This project demonstrates how to use the Strands AI framework with the Ollama model provider to create an AI agent.

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally
- Internet connection (for pulling models)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd strandsAI
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install strands
   ```

4. **Start Ollama**
   
   Make sure Ollama is running on your system. You can start it with:
   ```bash
   ollama serve
   ```
   
   In a separate terminal window, you can verify it's running with:
   ```bash
   ollama list
   ```

## Running the Example

Execute the agent script to interact with the AI:

```bash
python agent.py
```

The script will:
1. List available Ollama models
2. Pull the specified model (currently `llama3.2:latest`)
3. Create an agent using this model
4. Send a request to generate a short story about an AI assistant
5. Display the response

## Customizing

To use a different model, modify the `model_name` variable in `agent.py`. Available models depend on what you've pulled with Ollama.

## Troubleshooting

If you encounter errors:

1. Make sure Ollama is running (`ollama serve`)
2. Check available models (`ollama list`)
3. Try pulling the model manually (`ollama pull <model-name>`)
4. Verify your network connection if pulling new models

## Future Enhancements

This is a simple demonstration that will be enhanced with additional features in future updates.
