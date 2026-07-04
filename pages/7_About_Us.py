import streamlit as st

def main():
    st.set_page_config(page_title="About Us - AI-TravelMate", page_icon="ℹ️")
    st.title("ℹ️ About Us")
    
    st.markdown("""
    Welcome to **AI-TravelMate**, your smart and intelligent travel companion. 
    We believe that planning a trip should be as exciting and stress-free as the journey itself.
    
    By utilizing advanced multi-agent AI architecture entirely offline, we guarantee a secure, fast, and highly personalized itinerary planner. Our system works tirelessly to parse your travel constraints, recommend destinations, and build a beautiful day-by-day plan so you can just pack and go!
    """)
    
    st.divider()
    
    st.subheader("Contact Information")
    st.markdown("""
    - **Email:** support@ai-travelmate.local
    - **Phone:** +1 (555) 019-8372
    """)
    
    st.divider()
    
    st.subheader("Follow Us on Social Media")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[📸 Instagram](#)")
    with col2:
        st.markdown("[📘 Facebook](#)")
    with col3:
        st.markdown("[🐦 Twitter](#)")
        
    st.divider()
    
    st.markdown("<p style='text-align: center; color: gray;'>© 2026 AI-TravelMate. All rights reserved.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
