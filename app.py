import streamlit as st

# Define all pages with custom display names and icons
# Using st.navigation() removes "app" from the sidebar and gives full control over page labels
pages = [
    st.Page("pages/0_Home.py",                    title="Home",                   icon="🏠"),
    st.Page("pages/1_Trip_Planner.py",             title="Trip Planner",           icon="✈️"),
    st.Page("pages/2_Destination_Explorer.py",     title="Destination Explorer",   icon="🗺️"),
    st.Page("pages/3_Flight_Booking.py",           title="Flight Booking",         icon="✈️"),
    st.Page("pages/4_Hotel_Booking.py",            title="Hotel Booking",          icon="🏨"),
    st.Page("pages/5_Rating.py",                   title="Rating",                 icon="⭐"),
    st.Page("pages/6_Share_Travel_Experience.py",  title="Share Travel Experience",icon="📝"),
    st.Page("pages/7_About_Us.py",                 title="About Us",               icon="ℹ️"),
]

pg = st.navigation(pages)
pg.run()
