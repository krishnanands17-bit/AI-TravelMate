# AI-TravelMate

AI-TravelMate is a beginner-friendly, offline Smart Travel Planner built to demonstrate the power of a modular multi-agent architecture orchestrated through a Model Context Protocol (MCP) Server. The project was developed for the Agents for Good hackathon to showcase how multiple specialized AI-inspired agents can collaborate to solve a real-world travel planning problem while remaining simple, secure, and easy to extend.

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

```text
Streamlit UI
      │
      ▼
 MCP Server
      │
      ▼
 Trip Parser
      │
      ▼
 Trip Generator
      │
      ▼
 Narrator
```

The Security Agent validates both the input and the generated output throughout the workflow.

## How to Install

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