#!/usr/bin/env python3
"""
Interactive Tweet Deletion Agent
This script provides an interactive interface to delete tweets based on keywords.
"""

import os
from twitter_cleaner import authenticate_twitter, setup_ai_agent, delete_tweets_with_keywords

def check_twitter_credentials():
    """Check if Twitter API credentials are configured"""
    required_vars = [
        "TWITTER_CONSUMER_KEY", 
        "TWITTER_CONSUMER_SECRET",
        "TWITTER_ACCESS_TOKEN", 
        "TWITTER_ACCESS_TOKEN_SECRET",
        "TWITTER_BEARER_TOKEN"
    ]
    
    missing = [var for var in required_vars if not os.getenv(var)]
    
    if missing:
        print("Error: Missing Twitter API credentials in .env file:")
        for var in missing:
            print(f"  - {var}")
        return False
    
    return True

def get_user_keywords():
    """Get keywords from user input"""
    print("\nEnter keywords to search for in tweets (comma-separated):")
    keywords_input = input("> ")
    keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]
    
    if not keywords:
        print("Error: No valid keywords entered")
        return None
    
    return keywords

def get_max_tweets():
    """Get maximum number of tweets to analyze"""
    while True:
        try:
            print("\nEnter maximum number of recent tweets to analyze (10-200):")
            max_tweets = int(input("> "))
            if 10 <= max_tweets <= 200:
                return max_tweets
            print("Please enter a number between 10 and 200")
        except ValueError:
            print("Please enter a valid number")

def interactive_tweet_deletion():
    """Run the interactive tweet deletion process"""
    print("==== Interactive Twitter/X Tweet Deletion Agent ====")
    print("This tool will help you delete tweets based on keywords you specify.")
    
    # Check Twitter credentials
    if not check_twitter_credentials():
        print("\nPlease update your .env file with the required credentials and try again.")
        return
    
    try:
        # Test Twitter authentication
        print("\nVerifying Twitter API credentials...")
        client = authenticate_twitter()
        user = client.get_me().data
        print(f"Successfully authenticated as @{user.username}")
        
        # Set up AI agent
        print("\nSetting up AI agent...")
        agent = setup_ai_agent()
        print("AI agent ready")
        
        # Get keywords from user
        keywords = get_user_keywords()
        if not keywords:
            return
        
        # Get max tweets
        max_tweets = get_max_tweets()
        
        # Dry run first
        print(f"\n--- Analyzing tweets (Dry Run) ---")
        print(f"Searching for tweets containing or related to: {', '.join(keywords)}")
        print(f"Analyzing up to {max_tweets} recent tweets...")
        
        delete_tweets_with_keywords(keywords, dry_run=True, max_tweets=max_tweets)
        
        # Ask for confirmation
        print("\nReady to delete tweets?")
        print("1. Execute deletion")
        print("2. Modify keywords and try again")
        print("3. Cancel")
        
        choice = input("> ").strip()
        
        if choice == "1":
            print("\n--- Executing tweet deletion ---")
            delete_tweets_with_keywords(keywords, dry_run=False, max_tweets=max_tweets)
            print("\nDeletion complete!")
        elif choice == "2":
            print("\nRestarting with new keywords...")
            interactive_tweet_deletion()
        else:
            print("\nDeletion canceled. No tweets were deleted.")
            
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    interactive_tweet_deletion()
