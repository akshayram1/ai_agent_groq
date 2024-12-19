from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import logging

# Set up basic logging for debugging
logging.basicConfig(level=logging.INFO)

GROQ_API_KEY = "you need to get your own key from https://groq.dev"

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
)

try:
    response = agent.run("Share a 2 sentence love story between keyboard and mouse")
    # Print the full response for debugging
    logging.info(f"Response: {response}")
    agent.print_response("Share a 2 sentence love story between keyboard and mouse") 
except Exception as e:
    logging.error(f"An error occurred: {e}")