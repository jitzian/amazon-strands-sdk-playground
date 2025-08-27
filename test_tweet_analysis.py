#!/usr/bin/env python3
"""
Test Script for Twitter Cleaner
This script tests the tweet cleaner functionality without actually hitting the Twitter API.
"""

import os
from dotenv import load_dotenv
from twitter_cleaner import setup_ai_agent, should_delete_tweet

# Load environment variables
load_dotenv()

def test_should_delete_tweet():
    """Test the should_delete_tweet function with various examples"""
    # Sample tweets
    tweets = [
        "I love politics and discussing the latest political news!",
        "Had a great day at the beach with my family. So relaxing!",
        "This product is terrible, I'm very disappointed with the quality.",
        "Just watching the sunset, beautiful evening!",
        "The customer service was awful, will never shop there again #negative",
        "Starting a new project today, excited about the opportunities!",
        "Can't believe how this government is handling the situation. #politics"
    ]
    
    # Keywords to test
    keywords = ["politics", "negative", "complaint", "disappointed"]
    
    # Setup AI agent
    print("Setting up AI agent...")
    agent = setup_ai_agent()
    print("AI agent ready!")
    
    # Test each tweet
    print("\nTesting tweet analysis...\n")
    for i, tweet in enumerate(tweets, 1):
        print(f"Tweet {i}: {tweet}")
        result = should_delete_tweet(agent, tweet, keywords)
        action = "WOULD DELETE" if result else "would keep"
        print(f"Result: {action}")
        print("-" * 50)
        
    print("\nTest completed!")

if __name__ == "__main__":
    test_should_delete_tweet()
