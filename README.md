# ai_agent_groq
# README.txt

## PHI AI Agents Demo Collection

This repository contains three Python scripts demonstrating different uses of PHI AI agents with Groq and OpenAI models. Creating AI agents with this framework is straightforward and free to get started - all you need is an API key!

### Key Benefits
- **Simple Setup**: Create powerful AI agents in just a few lines of code
- **Free to Start**: No upfront costs - just bring your API key
- **Flexible**: Works with both Groq and OpenAI models
- **Ready-to-Use Examples**: Three working examples from basic to advanced usage

### Requirements

```
pip install phi-model
pip install yfinance
pip install python-dotenv
pip install fpdf
```

### Environment Setup

1. Create a 

.env

 file in the root directory
2. Add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

### Scripts Overview

#### 1. Simple Story Generator (1_simple_groq_agent.py)
- Basic implementation of Groq model
- Generates creative short stories
- Includes error handling and logging

Usage:
```python
python 1_simple_groq_agent.py
```

#### 2. Financial Analysis Agent (2_finance_agent_llama.py)
- Uses YFinance tools for financial data
- Compares stock recommendations and fundamentals
- Displays data in formatted tables
- Includes company symbol lookup functionality

Usage:
```python
python 2_finance_agent_llama.py
```

#### 3. Multi-Agent System (3_agent_teams_openai.py)
- Implements a team of specialized agents:
  - Web Agent: Uses DuckDuckGo for web searches
  - Finance Agent: Handles financial data analysis
- Combines multiple data sources
- Generates comprehensive reports

Usage:
```python
python 3_agent_teams_openai.py
```

### Features

- Error handling and logging
- Markdown formatting support
- Table-based data presentation
- Multiple model support (Groq, OpenAI)
- Built-in tools for finance and web searching
- Source attribution in results

### Notes

- Each script can be run independently
- Make sure to have valid API keys before running
- Internet connection required for web and finance tools
- Results are displayed in real-time with streaming support

### Why Choose Phidata?

Phidata addresses the challenge of adapting general-purpose LLMs to meet specific use-case requirements effectively by enhancing LLMs with three critical components:

- **Memory**: Allows LLMs to store chat history in a database, facilitating long-term conversations and context retention.
- **Knowledge**: Utilizes a vector database to access relevant business context, making interactions more meaningful.
- **Tools**: Equips LLMs with the ability to perform actions, such as pulling data from APIs or sending emails, thereby increasing their autonomy.

### Implementation Steps

1. **Create an Assistant**: Set up your AI Assistant using Phidata's framework.
2. **Add Tools and Knowledge**: Incorporate necessary tools (functions) and knowledge (vector database) to enhance functionality.
3. **Deployment**: Use frameworks like Streamlit, FastAPI, or Django to serve your AI application effectively.

### Integrations

Phidata supports various integrations that expand its capabilities:

- **LanceDB**: A powerful database solution for managing vector data.
- **SingleStore**: For high-performance data storage and retrieval.
- **Pinecone**: A vector database that enhances search and retrieval functionalities.
- **GitHub**: Access the source code and contribute to the Phidata project.

For detailed documentation, visit the [Phidata Documentation](https://docs.phidata.com).