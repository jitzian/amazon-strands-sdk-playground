import os
import json
import tweepy
import argparse
from dotenv import load_dotenv
from strands import Agent
from strands.models.ollama import OllamaModel

# Load environment variables from .env file
load_dotenv()

def authenticate_twitter():
    """Authenticate with Twitter API using credentials from environment variables"""
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    
    if not all([consumer_key, consumer_secret, access_token, access_token_secret, bearer_token]):
        raise ValueError("Twitter API credentials are missing from environment variables")
    
    # Authentication with Twitter API v2
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    
    return client

def setup_ai_agent(model_name="llama3.2:latest"):
    """Setup the Strands AI agent"""
    import importlib
    
    print(f"Setting up AI agent with model: {model_name}")
    
    # Get strands version
    strands_version = importlib.import_module('strands').__version__ if hasattr(importlib.import_module('strands'), '__version__') else "unknown"
    print(f"Using strands version: {strands_version}")
    
    # Get ollama package version
    try:
        ollama_pkg = importlib.import_module('ollama')
        ollama_version = ollama_pkg.__version__ if hasattr(ollama_pkg, '__version__') else "unknown"
        print(f"Using ollama package version: {ollama_version}")
    except ImportError:
        print("Ollama package not found")
    
    # Create a configured Ollama model with simplified options
    try:
        # Create an Ollama model with compatibility settings
        ollama_model = OllamaModel(
            host="http://localhost:11434",
            model_id=model_name,
            # Pass minimal parameters to avoid incompatibilities
            options={}  # Empty options to avoid potential compatibility issues
        )
        
        # Create an agent with the configured model
        return Agent(model=ollama_model)
    except Exception as e:
        print(f"Error initializing agent: {str(e)}")
        raise

def should_delete_tweet(agent, tweet_text, keywords):
    """Use the AI agent to decide if a tweet should be deleted based on keywords"""
    prompt = f"""
    Please analyze the following tweet and determine if it contains or relates to any of these keywords: {', '.join(keywords)}.
    
    Tweet: "{tweet_text}"
    
    Respond with only "YES" if the tweet should be deleted (contains or strongly relates to any keyword), or "NO" if it should be kept.
    """
    
    # Try direct Ollama access first as a backup approach
    try:
        import ollama
        print(f"Using direct Ollama API for tweet analysis...")
        model_name = "llama3.2:latest"  # Use the same model that the agent was configured with
        response = ollama.generate(model=model_name, prompt=prompt)
        result = response['response']
        print(f"Ollama direct API response: {result[:20]}...")
        return "YES" in result.upper()
    except Exception as e:
        print(f"Direct Ollama API failed: {str(e)}, falling back to agent")
        
        # Fall back to using the agent (which might fail depending on compatibility)
        try:
            response = agent(prompt)
            return "YES" in response.upper()
        except Exception as e:
            print(f"Agent-based analysis failed: {str(e)}")
            # If everything fails, be conservative and don't delete
            return False

def fetch_user_tweets(client, max_results=100):
    """Fetch recent tweets from the authenticated user"""
    try:
        user_id = client.get_me().data.id
        tweets = client.get_users_tweets(
            id=user_id,
            max_results=max_results,
            tweet_fields=["created_at", "text"]
        )
        return tweets.data if tweets.data else []
    except tweepy.errors.TooManyRequests:
        print("Twitter API rate limit reached. Please wait a few minutes and try again.")
        return []
    except Exception as e:
        print(f"Error fetching tweets: {str(e)}")
        return []

def delete_tweets_with_keywords(keywords, dry_run=True, max_tweets=100):
    """Delete tweets containing specified keywords"""
    try:
        # Authenticate with Twitter
        print("Authenticating with Twitter API...")
        client = authenticate_twitter()
        print("Authentication successful!")
        
        # Setup AI agent
        print("Setting up AI agent...")
        agent = setup_ai_agent()
        print("AI agent ready!")
        
        # Fetch user tweets
        print(f"Fetching up to {max_tweets} recent tweets...")
        tweets = fetch_user_tweets(client, max_results=max_tweets)
        
        if not tweets:
            print("No tweets were found or there was an error fetching tweets.")
            return
            
        print(f"Found {len(tweets)} tweets")
        
        # Process tweets
        deleted_count = 0
        for tweet in tweets:
            print(f"Analyzing tweet: {tweet.text[:50]}...")
            try:
                should_delete = should_delete_tweet(agent, tweet.text, keywords)
                if should_delete:
                    if dry_run:
                        print(f"Would delete tweet (ID: {tweet.id}): {tweet.text}")
                    else:
                        client.delete_tweet(tweet.id)
                        print(f"Deleted tweet (ID: {tweet.id}): {tweet.text}")
                    deleted_count += 1
            except Exception as e:
                print(f"Error analyzing tweet: {str(e)}")
                continue
        
        # Summary
        action = "Would delete" if dry_run else "Deleted"
        print(f"\nSummary: {action} {deleted_count} out of {len(tweets)} tweets based on keywords: {keywords}")
        
    except tweepy.errors.Unauthorized:
        print("Error: Twitter API authentication failed. Please check your credentials in the .env file.")
    except tweepy.errors.TooManyRequests:
        print("Error: Twitter API rate limit reached. Please wait a few minutes and try again.")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Delete tweets containing specified keywords')
    parser.add_argument('--keywords', nargs='+', required=True, help='Keywords to search for in tweets')
    parser.add_argument('--execute', action='store_true', help='Actually delete tweets. Without this flag, runs in dry-run mode.')
    parser.add_argument('--max', type=int, default=100, help='Maximum number of recent tweets to analyze')
    
    args = parser.parse_args()
    
    delete_tweets_with_keywords(args.keywords, not args.execute, args.max)

if __name__ == "__main__":
    main()
