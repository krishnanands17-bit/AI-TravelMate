from security import sanitize_input

def parse_trip_request(source: str, destination: str, days: int, budget: float, travelers: int, interests: list) -> dict:
    """Parses and sanitizes the user trip request."""
    return {
        "source": sanitize_input(source),
        "destination": sanitize_input(destination).title(),
        "days": int(days),
        "budget": float(budget),
        "travelers": int(travelers),
        "interests": [sanitize_input(i) for i in interests] if interests else []
    }
