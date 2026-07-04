# Agents Overview

## Trip Parser
- **Purpose**: Cleans and normalizes user input.
- **Inputs**: Raw user strings and numbers.
- **Outputs**: Structured dictionary.
- **Responsibilities**: Trimming, sanitizing, and formatting data.

## Trip Generator
- **Purpose**: Creates the actual travel plan.
- **Inputs**: Structured trip data.
- **Outputs**: Base trip itinerary dictionary.
- **Responsibilities**: Applying rule-based logic to map interests to activities.

## Narrator
- **Purpose**: Makes the output user-friendly.
- **Inputs**: Base trip itinerary.
- **Outputs**: Formatted trip itinerary dictionary.
- **Responsibilities**: Adding emojis, friendly titles, and conversational text.

## Security Agent
- **Purpose**: Ensures data validity and safety.
- **Inputs**: Raw inputs or generated outputs.
- **Outputs**: Validation boolean and error messages.
- **Responsibilities**: Checking constraints, sanitizing strings, preventing invalid states.
