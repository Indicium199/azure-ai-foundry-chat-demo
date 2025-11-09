# Import the os module
import os

# Load .env if present
try:
    from dotenv import load_dotenv # Imports function which can load variables from .env file 
    load_dotenv() # Reads .env and sets those variables
except ImportError: # Ignores error if python-dotenv is not installed
    pass

# Read environment variables
ENDPOINT = os.getenv("AZURE_AI_ENDPOINT")
API_KEY = os.getenv("AZURE_AI_KEY")
DEPLOYMENT = os.getenv("MODEL_DEPLOYMENT")

# Determines if demo mode should be used instead of calling Azure
DEMO_MODE = not (ENDPOINT and API_KEY and DEPLOYMENT)

# Function to collect the prompt
def get_ai_response(prompt):
    if DEMO_MODE:  # If Demo mode is used it will return a fake response
        return f"(demo) AI would respond to: {prompt}"
    else:
        # Placeholder for real Azure AI SDK call
        return "(real mode not implemented yet)"

# This statement starts the program
def main():
    print("Welcome to Azure AI Chat Demo!") # Welcome message to the user
    print("Type 'exit' to quit.\n") # User instructions to exit
   
   # Try statement to handle exceptions (like CTRL+C)
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break
            print("AI:", get_ai_response(user_input))
    except KeyboardInterrupt:
        print("\nExiting chat. Goodbye!")

# This ensures that the main() function runs only when this file is executed directly.
# If this file is imported as a module in another script, main() will NOT run automatically.
if __name__ == "__main__":
    main()



