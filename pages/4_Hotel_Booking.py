import streamlit as st

def main():
    st.set_page_config(page_title="Hotel Booking - AI-TravelMate", page_icon="🏨")
    
    st.title("🏨 Hotel Booking")
    st.markdown("### 🚧 Coming Soon")
    
    st.markdown(
        "Complete your perfect itinerary with seamless hotel bookings! "
        "Our upcoming hotel integration will ensure you have a comfortable place to stay at every stop."
    )
    
    st.markdown("#### Future Features Will Include:")
    st.markdown("""
    - **Hotel search:** Browse global hotel listings.
    - **Price comparison:** Find stays that fit your budget.
    - **Ratings & Reviews:** See what other travelers have to say.
    - **Nearby hotels:** Find hotels close to your planned attractions.
    - **Booking:** Secure reservations directly through the app.
    """)
    
    st.divider()
    
    st.markdown("### 📅 Future Integrations")
    st.info("""
    - Booking.com
    - Agoda
    - Expedia
    """)

if __name__ == "__main__":
    main()
