import streamlit as st
import json
import os

def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def main():
    st.set_page_config(page_title="Destination Explorer - AI-TravelMate", page_icon="🗺️")
    st.title("🗺️ Destination Explorer")
    st.markdown("Browse our top travel destinations and discover what makes them special.")
    
    destinations = load_json(os.path.join("data", "destinations.json"))
    
    if not destinations:
        st.warning("No destination data available.")
        return
        
    search_query = st.text_input("Search Destinations", "")
    
    for dest_name, details in destinations.items():
        if search_query and search_query.lower() not in dest_name.lower():
            continue
            
        with st.container():
            st.markdown(f"### {dest_name}")
            col1, col2 = st.columns([1, 2])
            
            with col1:
                img_url = details.get("image_placeholder", "https://via.placeholder.com/400x300?text=No+Image+Available")
                st.image(img_url, use_container_width=True)
                
            with col2:
                if "best_time_to_visit" in details:
                    st.markdown(f"**☀️ Best time to visit:** {details['best_time_to_visit']}")
                if "popular_attractions" in details:
                    st.markdown(f"**📸 Popular attractions:** {', '.join(details['popular_attractions'])}")
                if "famous_food" in details:
                    st.markdown(f"**🍔 Famous food:** {details['famous_food']}")
                if "shopping_places" in details:
                    st.markdown(f"**🛍️ Shopping places:** {details['shopping_places']}")
                if "adventure_activities" in details:
                    st.markdown(f"**🧗 Adventure activities:** {details['adventure_activities']}")
                if "local_tips" in details:
                    st.markdown(f"**💡 Local tips:** {details['local_tips']}")
            st.divider()

if __name__ == "__main__":
    main()
