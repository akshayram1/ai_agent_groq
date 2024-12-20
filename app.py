from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API Key (Replace with your actual API key)
GROQ_API_KEY = "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"

# Web agent to fetch and summarize news
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY),
    tools=[DuckDuckGo()],  # Use DuckDuckGo for web searches
    instructions=[
        "Search for the latest AI news.",
        "Summarize the main points clearly and concisely.",
        "Always include sources for all information.",
        "Format the response in Markdown for clarity."
    ],
    show_tool_calls=True,  # Enable logging of tool usage
    markdown=True  # Format the output in Markdown
)

# Function to fetch the latest AI news
import json

# Function to fetch the latest AI news
def fetch_latest_ai_news():
    query = "Find the latest news about Artificial Intelligence and summarize it."
    print("\nFetching the latest AI news...\n")
    response = web_agent.get_response(query)  # Assuming get_response method exists
    response_json = json.loads(response)
    print(json.dumps(response_json, indent=4))

# Main entry point
if __name__ == "__main__":
    fetch_latest_ai_news()

# Main entry point

