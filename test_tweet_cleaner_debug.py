#!/usr/bin/env python3
"""
Test Script for Tweet Cleaner with Debug Info
This script tests the tweet cleaner with verbose logging.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def run_test():
    """Run a basic test of the tweet cleaner functionality"""
    print("Running tweet cleaner test with debug info...")
    
    # Import after setup to avoid any initialization issues
    from twitter_cleaner import setup_ai_agent, should_delete_tweet
    
    # Sample tweets
    test_tweets = [
        "I love politics and discussing the latest political news!",
        "Had a great day at the beach with my family. So relaxing!"
    ]
    
    # Test keywords
    keywords = ["politics", "negative"]
    
    try:
        # Setup AI agent
        print("\nSetting up AI agent...")
        agent = setup_ai_agent()
        print("AI agent setup complete!")
        
        # Test tweet analysis
        for i, tweet in enumerate(test_tweets):
            print(f"\nAnalyzing test tweet {i+1}: {tweet}")
            result = should_delete_tweet(agent, tweet, keywords)
            action = "DELETE" if result else "KEEP"
            print(f"Decision: {action}")
            
        return True
    except Exception as e:
        print(f"\nError in test: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
        
if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
