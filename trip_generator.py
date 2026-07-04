import json
import os
import random

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_json(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def generate_trip(trip_data: dict) -> dict:
    """Generates a trip itinerary using local knowledge base or a fallback rule-based system."""
    destinations = load_json("destinations.json")
    restaurants = load_json("restaurants.json")
    travel_tips = load_json("travel_tips.json")
    packing_lists = load_json("packing_lists.json")
    dest_types = load_json("destination_types.json")

    destination = trip_data["destination"].title()
    days = trip_data["days"]
    interests = trip_data.get("interests", [])
    
    is_fallback = False
    itinerary = []
    
    if destination in destinations:
        dest_data = destinations[destination]
        dest_restaurants = restaurants.get(destination, ["a famous local restaurant"])
        
        # Gather all relevant attractions based on interests
        pool = []
        for interest in interests:
            if interest in dest_data:
                pool.extend(dest_data[interest])
        
        # If pool is empty or user selected no interests, grab some defaults
        if not pool:
            for cat in ["Nature", "Family", "History", "Beaches", "Spiritual", "Wildlife"]:
                if cat in dest_data:
                    pool.extend(dest_data[cat])
        
        # Remove duplicates while preserving order
        pool = list(dict.fromkeys(pool))
        random.seed(hash(destination) + days) # Stable sort for testing but varied by days
        
        attraction_idx = 0
        restaurant_idx = 0
        
        for day in range(1, days + 1):
            day_plan = {"day": day, "Morning": [], "Afternoon": [], "Evening": []}
            
            # Morning
            if attraction_idx < len(pool):
                day_plan["Morning"].append(pool[attraction_idx])
                attraction_idx += 1
            else:
                day_plan["Morning"].append("Relax at the hotel or take a local stroll")
                
            # Afternoon
            if restaurant_idx < len(dest_restaurants):
                day_plan["Afternoon"].append(f"Lunch at {dest_restaurants[restaurant_idx]}")
                restaurant_idx += 1
            else:
                day_plan["Afternoon"].append("Lunch at a popular local cafe")
                
            if attraction_idx < len(pool):
                day_plan["Afternoon"].append(f"Visit {pool[attraction_idx]}")
                attraction_idx += 1
                
            # Evening
            if "Shopping" in interests and "Shopping" in dest_data:
                shop_options = dest_data["Shopping"]
                day_plan["Evening"].append(f"Explore {random.choice(shop_options)} for shopping")
            elif attraction_idx < len(pool):
                day_plan["Evening"].append(f"Visit {pool[attraction_idx]}")
                attraction_idx += 1
            else:
                day_plan["Evening"].append("Enjoy a quiet evening experiencing local culture")
                
            itinerary.append(day_plan)
            
        # Get specific tips
        specific_tips = travel_tips.get(destination, {})
        tips_list = [f"{k.replace('_', ' ').title()}: {v}" for k, v in specific_tips.items()] if specific_tips else ["Carry local currency.", "Keep emergency contacts handy."]
        
        # Get specific packing list based on destination type
        dtype = dest_types.get(destination, "City")
        pack_list = packing_lists.get(dtype, ["Comfortable clothing", "Power bank", "Camera"])
        
    else:
        is_fallback = True
        # Generate balanced generic sightseeing itinerary in Morning/Afternoon/Evening format
        for day in range(1, days + 1):
            day_plan = {"day": day, "Morning": [], "Afternoon": [], "Evening": []}
            day_plan["Morning"].append(f"Visit the most famous landmarks in {destination}")
            day_plan["Afternoon"].append("Lunch at a popular local restaurant")
            day_plan["Afternoon"].append("Explore cultural and historical spots")
            day_plan["Evening"].append("Enjoy the local markets and evening ambiance")
            itinerary.append(day_plan)
            
        tips_list = ["Carry local currency.", "Keep emergency contacts handy.", "Stay hydrated."]
        pack_list = ["Comfortable shoes", "Weather-appropriate clothing", "Camera", "Power bank"]

    return {
        "title": f"Trip to {destination}",
        "itinerary": itinerary,
        "estimated_budget": trip_data["budget"],
        "travel_tips": tips_list,
        "packing_list": pack_list,
        "safety_tips": ["Stay in well-lit areas at night.", "Keep your belongings secure.", "Be aware of your surroundings."],
        "is_fallback": is_fallback
    }
