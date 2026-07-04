import streamlit as st
from mcp_server import process_trip_request

def main():
    st.set_page_config(page_title="Trip Planner - AI-TravelMate", page_icon="✈️", layout="centered")
    
    st.markdown("<h1 style='text-align: center; font-size: 3rem;'>✈️</h1>", unsafe_allow_html=True)
    st.title("Trip Planner")
    st.markdown("Plan your perfect trip with our AI Multi-Agent System.")
    
    with st.form("trip_form"):
        source = st.text_input("Source")
        destination = st.text_input("Destination")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            days = st.number_input("Number of Days", min_value=1, value=3)
        with col2:
            budget = st.number_input("Budget", min_value=1, value=5000)
        with col3:
            travelers = st.number_input("Number of Travelers", min_value=1, value=2)
            
        interests = st.multiselect("Travel Interests", 
                                   ["Nature", "Adventure", "Food", "Beaches", "History", "Shopping"])
        
        submit = st.form_submit_button("Generate Trip")
        
    if submit:
        try:
            with st.spinner("Planning your perfect trip..."):
                plan = process_trip_request(source, destination, days, budget, travelers, interests)
                
            st.success("Trip generated successfully!")
            
            st.subheader(plan["display_title"])
            
            st.markdown("### Day-wise Itinerary")
            for day_info in plan["itinerary"]:
                st.write(day_info)
                
            st.markdown("### Details")
            st.write(f"**Estimated Budget:** {plan['estimated_budget']}")
            
            col_tips, col_pack, col_safe = st.columns(3)
            with col_tips:
                st.markdown("**Travel Tips**")
                for tip in plan["travel_tips"]:
                    st.write(f"- {tip}")
            with col_pack:
                st.markdown("**Packing List**")
                for item in plan["packing_list"]:
                    st.write(f"- {item}")
            with col_safe:
                st.markdown("**Safety Tips**")
                for tip in plan["safety_tips"]:
                    st.write(f"- {tip}")
                    
            st.info(plan["note"])
            
        except ValueError as e:
            st.error(str(e))
            
if __name__ == "__main__":
    main()
