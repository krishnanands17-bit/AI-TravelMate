# Project Specifications

## Architecture
The system uses a multi-agent orchestration architecture mimicking an MCP (Model Context Protocol) Server.
1. **Frontend**: Streamlit provides a simple interface.
2. **Orchestrator**: `mcp_server.py` manages the flow between sub-agents.
3. **Agents**:
   - Trip Parser
   - Trip Generator
   - Narrator
   - Security Agent

## Workflow
1. User enters travel details in `app.py`.
2. Request is passed to `mcp_server.py`.
3. Security Agent validates the raw input.
4. Trip Parser cleans and structures the data.
5. Trip Generator creates a rule-based itinerary.
6. Narrator adds conversational elements and emojis.
7. Security Agent validates the final output before it reaches the user.
8. Streamlit UI displays the final result.

## Functional Requirements
- Gather source, destination, days, budget, travelers, and interests.
- Generate a day-wise itinerary matching selected interests.
- Provide packing list, travel tips, and safety tips.
- Handle invalid inputs gracefully.

## Future Enhancements
- Integrate actual LLM APIs for dynamic content generation.
- Implement real parallel processing for the Security Agent.
- Add map visualizations and budget breakdown charts.
