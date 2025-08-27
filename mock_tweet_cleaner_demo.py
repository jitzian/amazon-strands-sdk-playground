#!/usr/bin/env python3
"""
Mock Tweet Cleaner Demo
This script demonstrates the tweet cleaner functionality using mock tweets,
so we don't hit the Twitter API rate limits.
"""

import os
import ollama
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define some mock tweets
class MockTweet:
    def __init__(self, id, text, created_at=None):
        self.id = id
        self.text = text
        self.created_at = created_at or datetime.now()

MOCK_TWEETS = [
    MockTweet(1, "I love politics and discussing the latest political news!"),
    MockTweet(2, "Had a great day at the beach with my family. So relaxing!"),
    MockTweet(3, "This product is terrible, I'm very disappointed with the quality. #negative"),
    MockTweet(4, "Just watching the sunset, beautiful evening!"),
    MockTweet(5, "The customer service was awful, will never shop there again #complaint"),
    MockTweet(6, "Starting a new project today, excited about the opportunities!"),
    MockTweet(7, "Can't believe how this government is handling the situation. #politics"),
    MockTweet(8, "Just had the best coffee ever at my favorite cafe!"),
    MockTweet(9, "Why does everything have to be so complicated? Frustrated with this process."),
    MockTweet(10, "Celebrating my birthday today! 🎂")
]

def should_delete_tweet(tweet_text, keywords, model_name="llama3.2:latest"):
    """Use Ollama directly to decide if a tweet should be deleted based on keywords"""
    prompt = f"""
    Please analyze the following tweet and determine if it contains or relates to any of these keywords: {', '.join(keywords)}.
    
    Tweet: "{tweet_text}"
    
    Respond with only "YES" if the tweet should be deleted (contains or strongly relates to any keyword), or "NO" if it should be kept.
    """
    
    try:
        print(f"Analyzing: {tweet_text[:50]}...")
        response = ollama.generate(model=model_name, prompt=prompt)
        result = "YES" in response['response'].upper()
        decision = "DELETE" if result else "KEEP"
        print(f"Decision: {decision} - AI says: {response['response'].strip()}")
        return result
    except Exception as e:
        print(f"Error analyzing tweet: {str(e)}")
        return False

def demo_tweet_cleaner(keywords, dry_run=True):
    """Demonstrate the tweet cleaner functionality with mock tweets"""
    print("\n==== Twitter/X Tweet Cleaner Demo ====")
    print(f"Looking for tweets containing or related to: {', '.join(keywords)}")
    
    # Check Ollama
    print("\nChecking Ollama availability...")
    try:
        models = ollama.list()
        print(f"Ollama is available with models: {[m['name'] for m in models['models']]}")
    except Exception as e:
        print(f"Error connecting to Ollama: {str(e)}")
        print("Please make sure Ollama is running with 'ollama serve'")
        return
    
    # Process mock tweets
    print(f"\nAnalyzing {len(MOCK_TWEETS)} tweets...\n")
    
    deleted_count = 0
    for tweet in MOCK_TWEETS:
        should_delete = should_delete_tweet(tweet.text, keywords)
        if should_delete:
            if dry_run:
                print(f"Would delete tweet (ID: {tweet.id}): {tweet.text}")
            else:
                print(f"Deleted tweet (ID: {tweet.id}): {tweet.text}")
            deleted_count += 1
            print("-" * 50)
    
    # Summary
    action = "Would delete" if dry_run else "Deleted"
    print(f"\nSummary: {action} {deleted_count} out of {len(MOCK_TWEETS)} tweets based on keywords: {keywords}")

if __name__ == "__main__":
    try:
        # Define keywords to search for
        keywords = ["politics", "negative", "complaint", "disappointed"]
        
        print("Starting mock tweet cleaner demo with ollama version:", ollama.__version__ if hasattr(ollama, '__version__') else "unknown")
        
        # Run the demo in dry-run mode first
        print("\n--- Dry Run Mode ---")
        demo_tweet_cleaner(keywords, dry_run=True)
        
        # Ask if user wants to simulate actual deletion
        response = input("\nSimulate actual deletion? (yes/no): ").lower().strip()
        
        if response == "yes":
            print("\n--- Simulated Deletion Mode ---")
            demo_tweet_cleaner(keywords, dry_run=False)
        else:
            print("\nSimulated deletion canceled.")
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        import traceback
        traceback.print_exc()
