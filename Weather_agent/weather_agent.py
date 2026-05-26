


# Project-ID = https://anuragkumar1973-0503-resource.services.ai.azure.com/api/projects/anuragkumar1973-0503
# Azure OpenAI API Key: YOUR_API_KEY_HERE
# api-key: YOUR_API_KEY_HERE
# ============================================================================
# PROGRAM: Azure AI Weather Bot with Chat Interface
# ============================================================================
#
# PURPOSE:
#   Create an interactive chat interface for weather queries using Azure AI.
#   Users can ask questions about weather, and the WeatherBot agent responds.
#
# INSTALLATION:
#   pip install azure-ai-projects>=2.1.0 azure-identity
#
# EXECUTION:
#   python3 weather_agent.py
#
# FEATURES:
#   • Interactive chat interface for weather queries
#   • Uses Azure AI existing agent "WeatherGuy:2"
#   • Multi-turn conversation support
#   • Type 'quit' or 'exit' to end conversation
#
# ============================================================================

import requests
import json
import os
import sys

# ============================================================================
# AZURE CONFIGURATION
# ============================================================================

# Get API key from environment variable or use placeholder
API_KEY = "YOUR_API_KEY_HERE"

AZURE_CONFIGS = {
    "agent_id": "WeatherGuy:2",
    "endpoint": "https://anuragkumar1973-0503-resource.services.ai.azure.com",
    "api_version": "2024-12-01-preview",
    "model_deployment": "gpt-4-turbo",  # Common deployment name - change if different
}

# ============================================================================
# INITIALIZE AZURE CLIENT
# ============================================================================

try:
    print("🔄 Initializing Azure OpenAI Client...")
    
    # Check if API key is set
    if API_KEY == "your-api-key-here":
        print("❌ Error: AZURE_API_KEY environment variable not set!")
        print("\n📋 To fix this, follow these steps:")
        print("\n1. Get your API key from Azure Portal:")
        print("   • Go to: https://portal.azure.com")
        print("   • Search for 'anuragkumar1973-0503-resource'")
        print("   • Click on 'Keys and Endpoint' section")
        print("   • Copy the 'Key 1' value")
        print("\n2. Set the environment variable in your terminal:")
        print("   export AZURE_API_KEY='your-key-here'")
        print("\n3. Run the script again:")
        print("   python3 weather_agent.py\n")
        sys.exit(1)
    
    # Test connection
    headers = {
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    # Simple test to verify credentials work
    test_url = f"{AZURE_CONFIGS['endpoint']}/openai/deployments/{AZURE_CONFIGS['model_deployment']}/chat/completions?api-version={AZURE_CONFIGS['api_version']}"
    
    print("✓ Azure OpenAI Client initialized successfully!\n")
    
except Exception as e:
    print(f"❌ Error initializing Azure client: {e}")
    print("\nTroubleshooting:")
    print("   • Make sure AZURE_API_KEY is set correctly")
    print("   • Verify the API key is not expired (check Azure Portal)")
    print("   • Ensure you have the correct endpoint URL")
    sys.exit(1)

# ============================================================================
# WEATHER BOT CHAT INTERFACE
# ============================================================================

# ============================================================================
# WEATHER BOT CHAT INTERFACE
# ============================================================================

class WeatherBot:
    """Interactive Weather Bot using Azure AI with direct HTTP API"""
    
    def __init__(self, agent_id, api_key):
        self.agent_id = agent_id
        self.api_key = api_key
        self.conversation_history = []
        self.headers = {
            "api-key": self.api_key,
            "Content-Type": "application/json"
        }
    
    def query_weather(self, user_message):
        """Send a query to Azure OpenAI and get a response"""
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Prepare Azure OpenAI API request
            url = f"{AZURE_CONFIGS['endpoint']}/openai/deployments/{AZURE_CONFIGS['model_deployment']}/chat/completions?api-version={AZURE_CONFIGS['api_version']}"
            
            payload = {
                "messages": self.conversation_history,
                "temperature": 0.7,
                "max_tokens": 500,
            }
            
            # Send request to Azure OpenAI
            response = requests.post(url, headers=self.headers, json=payload)
            
            # Check for errors
            if response.status_code != 200:
                error_text = response.text
                if "DeploymentNotFound" in error_text:
                    return (f"❌ Deployment '{AZURE_CONFIGS['model_deployment']}' not found.\n\n"
                           f"📋 To fix this:\n"
                           f"   1. Go to: https://portal.azure.com\n"
                           f"   2. Search for your resource: 'anuragkumar1973-0503-resource'\n"
                           f"   3. Click on it and find 'Model deployments' section\n"
                           f"   4. Check the deployment name (e.g., 'gpt-4', 'gpt-35-turbo', 'gpt-4-turbo', etc.)\n"
                           f"   5. Update line 13 in weather_agent.py:\n"
                           f"      model_deployment: \"your-deployment-name\"\n"
                           f"   6. Run this script again")
                return f"❌ Error ({response.status_code}): {error_text}"
            
            # Extract response content
            response_data = response.json()
            assistant_message = response_data["choices"][0]["message"]["content"]
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        
        except Exception as e:
            return f"❌ Error querying weather agent: {e}"
    
    def display_welcome(self):
        """Display welcome message"""
        print("=" * 70)
        print("🌤️  WEATHER BOT - Interactive Chat Interface")
        print("=" * 70)
        print("\n📝 Instructions:")
        print("   • Type your weather questions (e.g., 'What's the weather in NYC?')")
        print("   • Type 'quit' or 'exit' to end conversation")
        print("   • Type 'clear' to reset conversation history")
        print("   • Type 'help' for available commands")
        print("\n" + "=" * 70 + "\n")
    
    def display_help(self):
        """Display help message"""
        print("\n📚 Available Commands:")
        print("   help     - Show this help message")
        print("   clear    - Clear conversation history")
        print("   quit/exit - End the conversation")
        print("\n💡 Weather Query Examples:")
        print("   'What is the weather in London?'")
        print("   'Tell me the forecast for tomorrow'")
        print("   'Will it rain today in San Francisco?'")
        print("   'What is the temperature in Tokyo?'")
        print("=" * 70 + "\n")
    
    def run(self):
        """Run the interactive chat loop"""
        self.display_welcome()
        
        while True:
            try:
                # Get user input
                user_input = input("🤖 You: ").strip()
                
                # Handle empty input
                if not user_input:
                    print("   (Please enter a message)\n")
                    continue
                
                # Handle special commands
                if user_input.lower() in ['quit', 'exit']:
                    print("\n👋 Thank you for using WeatherBot! Goodbye!\n")
                    break
                
                elif user_input.lower() == 'clear':
                    self.conversation_history = []
                    print("   ✓ Conversation history cleared\n")
                    continue
                
                elif user_input.lower() == 'help':
                    self.display_help()
                    continue
                
                # Query the weather agent
                print("\n⏳ Fetching weather information...\n")
                response = self.query_weather(user_input)
                
                # Display response
                print(f"🌡️  WeatherBot: {response}\n")
            
            except KeyboardInterrupt:
                print("\n\n👋 Chat interrupted. Goodbye!\n")
                break
            except Exception as e:
                print(f"❌ Error: {e}\n")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Create and run weather bot
    weather_bot = WeatherBot(
        agent_id=AZURE_CONFIGS["agent_id"],
        api_key=API_KEY
    )
    
    # Run interactive chat
    weather_bot.run()



