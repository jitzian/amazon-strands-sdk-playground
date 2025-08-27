#!/usr/bin/env python3
"""
Tweet Deletion Demo Script
This script demonstrates how to use the twitter_cleaner.py script to delete tweets based on keywords.
"""

from twitter_cleaner import delete_tweets_with_keywords

def main():
    """
    Demo of tweet deletion with AI analysis
    """
    print("==== Twitter/X Tweet Cleaner Demo ====")
    print("This demonstration will scan your recent tweets and identify those containing specified keywords.")
    
    # List of keywords to look for in tweets
    keywords = ["politics", "negative", "complaint", "controversial"]
    print(f"Looking for tweets containing or related to: {', '.join(keywords)}")
    
    # First run in dry-run mode (doesn't actually delete)
    print("\n--- Dry Run (no tweets will be deleted) ---")
    delete_tweets_with_keywords(keywords=keywords, dry_run=True, max_tweets=50)
    
    # Ask user if they want to proceed with deletion
    response = input("\nDo you want to proceed with tweet deletion? (yes/no): ").lower().strip()
    
    if response == "yes":
        print("\n--- Executing Tweet Deletion ---")
        delete_tweets_with_keywords(keywords=keywords, dry_run=False, max_tweets=50)
        print("\nDeletion complete!")
    else:
        print("\nDeletion canceled. No tweets were deleted.")

if __name__ == "__main__":
    main()
