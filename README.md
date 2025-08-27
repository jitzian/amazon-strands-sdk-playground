# Strands AI Project

This project demonstrates how to use the Strands AI framework with the Ollama model provider to create AI agents for various purposes.

## Features

- Basic AI text generation with Ollama models
- Twitter/X tweet management with keyword-based deletion

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally
- Internet connection (for pulling models)
- Twitter Developer Account (for Twitter functionality)

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
   pip install -r requirements.txt
   ```

4. **Start Ollama**
   
   Make sure Ollama is running on your system. You can start it with:
   ```bash
   ollama serve
   ```

5. **Configure Twitter API credentials**

   Create a Twitter Developer account at https://developer.twitter.com and create a project and app with:
   - Read and Write permissions
   - OAuth 1.0a and OAuth 2.0 authentication

   Then copy `.env.example` to `.env` and fill in your Twitter API credentials:
   ```
   TWITTER_CONSUMER_KEY=your_consumer_key
   TWITTER_CONSUMER_SECRET=your_consumer_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   TWITTER_BEARER_TOKEN=your_bearer_token
   ```

## Running the Examples

### Basic AI Text Generation

```bash
python agent.py
```

### Twitter Tweet Cleaner

This tool uses AI to analyze your tweets and delete those containing specific keywords.

#### Command-line Usage

First, run in dry-run mode to see what would be deleted:

```bash
python twitter_cleaner.py --keywords politics complaint negative --max 50
```

When you're ready to actually delete tweets:

```bash
python twitter_cleaner.py --keywords politics complaint negative --execute --max 50
```

Parameters:
- `--keywords`: List of keywords to search for in tweets
- `--execute`: Actually delete tweets (without this flag, runs in dry-run mode)
- `--max`: Maximum number of recent tweets to analyze (default: 100)

#### Interactive Tweet Cleaner

For a more user-friendly experience, try the interactive tweet cleaner:

```bash
python interactive_tweet_cleaner.py
```

This script will guide you through the process with interactive prompts.

#### Quick Demo

To run a quick demonstration that shows how the tweet cleaner works:

```bash
python tweet_deletion_demo.py
```

This will analyze your tweets for common keywords like "politics", "negative", etc. and show which ones would be deleted without actually deleting them until you confirm.

## Troubleshooting

### Ollama Issues
- Make sure Ollama is running (`ollama serve`)
- Check available models (`ollama list`)
- Try pulling the model manually (`ollama pull <model-name>`)

### Twitter API Issues
- Verify your API credentials are correct in the `.env` file
- Ensure your Twitter Developer app has the correct permissions
- Check that your access tokens are valid and not expired
