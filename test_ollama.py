#!/usr/bin/env python3
"""
Test Script for Ollama
This script tests the Ollama API directly to ensure it's working properly.
"""

import ollama
import sys

def test_ollama_directly():
    """Test the Ollama API directly"""
    print("Testing Ollama API directly...")
    
    # Test model we're using
    model_name = "llama3.2:latest"
    
    # Sample prompt
    prompt = "Write a short response: Is this tweet about politics? Tweet: 'I love discussing the latest political news!'"
    
    try:
        # List available models
        print(f"Checking available models...")
        models = ollama.list()
        print(f"Available models: {[m['name'] for m in models['models']]}")
        
        # Check if our model is available
        model_available = any(m['name'] == model_name for m in models['models'])
        if not model_available:
            print(f"Model {model_name} not available. Please pull it with 'ollama pull {model_name}'")
            return
            
        print(f"Model {model_name} is available!")
        
        # Generate a response
        print(f"\nSending prompt to {model_name}...")
        response = ollama.generate(model=model_name, prompt=prompt)
        
        print("\nResponse from Ollama:")
        print("-" * 40)
        print(response['response'])
        print("-" * 40)
        
        print("\nOllama API is working correctly!")
        return True
    except Exception as e:
        print(f"Error testing Ollama: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_ollama_directly()
    sys.exit(0 if success else 1)
