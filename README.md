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

### License

MIT License

For more information about the PHI library and its capabilities, please refer to the official documentation.