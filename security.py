import re

def sanitize_input(text: str) -> str:
    """Trims whitespace."""
    if not isinstance(text, str):
        return ""
    # We no longer silently remove HTML/scripts; we just trim whitespace.
    # Validation handles rejecting malicious input.
    return text.strip()

def contains_malicious_content(text: str) -> bool:
    """Checks for HTML, JS, SQL injection, and prompt injection patterns."""
    text_lower = text.lower()
    
    # 1 & 2. HTML and Script Tags
    if "<" in text and ">" in text:
        return True
    
    # 3. JavaScript Patterns
    js_patterns = ["alert(", "document.", "window.", "eval(", "onerror=", "onclick="]
    if any(p in text_lower for p in js_patterns):
        return True
        
    # 4. SQL Injection Patterns
    sql_patterns = ["drop table", "select *", "union select", "insert into", "delete from", "--", "';"]
    if any(p in text_lower for p in sql_patterns):
        return True
        
    # 5. Prompt Injection
    prompt_patterns = ["ignore previous instructions", "reveal system prompt", "bypass security"]
    if any(p in text_lower for p in prompt_patterns):
        return True
        
    return False

def validate_destination_name(text: str) -> bool:
    """Checks if destination name contains only allowed characters."""
    # Allows letters, numbers, spaces, hyphens, apostrophes, and periods.
    pattern = r"^[a-zA-Z0-9\s\-'\.]*$"
    return bool(re.match(pattern, text))

def validate_trip_request(data: dict) -> tuple[bool, str]:
    """Validates the initial trip request data strictly."""
    source = data.get("source", "")
    destination = data.get("destination", "")
    
    if not source:
        return False, "Source is required."
    if not destination:
        return False, "Destination is required."
        
    # Check for malicious content in strings
    if contains_malicious_content(source) or contains_malicious_content(destination):
        return False, "Potentially malicious input detected."
        
    for interest in data.get("interests", []):
        if contains_malicious_content(interest):
            return False, "Potentially malicious input detected."
            
    # Validate destination name characters
    if not validate_destination_name(source) or not validate_destination_name(destination):
        return False, "Location names contain invalid characters."

    if data.get("days", 0) < 1:
        return False, "Number of days must be at least 1."
    if data.get("budget", 0) <= 0:
        return False, "Budget must be greater than 0."
    if data.get("travelers", 0) < 1:
        return False, "Number of travelers must be at least 1."
        
    return True, ""

def validate_output(plan: dict) -> tuple[bool, str]:
    """Validates the generated itinerary."""
    required_keys = ["title", "itinerary", "estimated_budget"]
    for key in required_keys:
        if key not in plan or not plan[key]:
            return False, f"Missing {key} in generated plan."
    return True, ""
