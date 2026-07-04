def narrate_trip(plan: dict) -> dict:
    """Narrates the trip with a friendly tone and emojis."""
    title = plan.get("title", "Your Trip")
    display_title = f"{title} ✈️"
    
    narrated_itinerary = []
    for day_plan in plan.get("itinerary", []):
        day = day_plan["day"]
        day_text = f"**Day {day}:**\n\n"
        
        day_text += "* 🌅 **Morning**: " + ", ".join(day_plan.get("Morning", [])) + "\n"
        day_text += "* ☀️ **Afternoon**: " + ", ".join(day_plan.get("Afternoon", [])) + "\n"
        day_text += "* 🌙 **Evening**: " + ", ".join(day_plan.get("Evening", []))
        
        narrated_itinerary.append(day_text)
        
    note = "Have a wonderful and safe journey! 🌍"
    if plan.get("is_fallback"):
        note = "⚠️ *This destination is not yet available in the local travel knowledge base, so a general sightseeing itinerary has been generated.*\n\n" + note

    return {
        "display_title": display_title,
        "itinerary": narrated_itinerary,
        "estimated_budget": plan.get("estimated_budget"),
        "travel_tips": plan.get("travel_tips", []),
        "packing_list": plan.get("packing_list", []),
        "safety_tips": plan.get("safety_tips", []),
        "title": title,  # Keep original title for validation
        "note": note
    }
