# AI-TravelMate

A beginner-friendly Streamlit app that takes travel details from user input and generates a personalized travel itinerary using a multi-agent architecture orchestrated by an MCP Server.

## Features
- Interactive Streamlit UI
- Multi-agent architecture (Parser, Generator, Narrator, Security)
- Validates user input and generated output
- Suggests customized itineraries based on travel interests

## File Structure
- `app.py`: Streamlit User Interface
- `mcp_server.py`: Orchestrates the flow
- `trip_parser.py`: Parses and sanitizes input
- `trip_generator.py`: Generates the itinerary
- `narrator.py`: Adds friendly tone and emojis
- `security.py`: Validates inputs and outputs
- `sample_trip.txt`: Sample input data
- `requirements.txt`: Project dependencies
- `SPECS.md`: Project architecture and specs
- `AGENTS.md`: Descriptions of agents
- `skills/`: Capabilities of the agents

## Architecture
Streamlit UI -> MCP Server -> Trip Parser -> Trip Generator -> Narrator

Security Agent runs in parallel throughout the workflow for validation.

## How to Install
1. Ensure you have Python installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run
```bash
streamlit run app.py
```

## Sample Input
- **Source:** Kochi
- **Destination:** Munnar
- **Days:** 3
- **Budget:** 12000
- **Travelers:** 2
- **Interests:** Nature, Food
