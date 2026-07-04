from security import validate_trip_request, validate_output
from trip_parser import parse_trip_request
from trip_generator import generate_trip
from narrator import narrate_trip

def process_trip_request(source: str, destination: str, days: int, budget: float, travelers: int, interests: list) -> dict:
    """Orchestrates the trip planning process."""
    
    # 1. Parse and sanitize input
    trip_data = parse_trip_request(source, destination, days, budget, travelers, interests)
    
    # 2. Validate input
    is_valid, error_msg = validate_trip_request(trip_data)
    if not is_valid:
        raise ValueError(f"Input Validation Error: {error_msg}")
        
    # 3. Generate trip
    raw_plan = generate_trip(trip_data)
    
    # 4. Narrate trip
    final_plan = narrate_trip(raw_plan)
    
    # 5. Validate output
    is_valid_out, error_msg_out = validate_output(final_plan)
    if not is_valid_out:
        raise ValueError(f"Output Validation Error: {error_msg_out}")
        
    return final_plan
