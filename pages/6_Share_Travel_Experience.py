import streamlit as st
import json
import os
from datetime import datetime

DATA_FILE = os.path.join("data", "travel_reviews.json")
UPLOAD_DIR = "uploads"

def load_reviews():
    if not os.path.exists("data"):
        os.makedirs("data")
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_review(data):
    reviews = load_reviews()
    reviews.append(data)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=4)

def save_uploaded_files(uploaded_files):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    saved_paths = []
    for uploaded_file in uploaded_files:
        if uploaded_file.name.lower().endswith(("jpg", "jpeg", "png")):
            file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            saved_paths.append(file_path)
    return saved_paths

def main():
    st.set_page_config(page_title="Share Experience - AI-TravelMate", page_icon="📝")
    st.title("📝 Share Travel Experience")
    st.markdown("Share your trips, upload photos, and inspire other travelers!")
    
    with st.form("share_experience_form", clear_on_submit=True):
        st.subheader("Tell us about your trip")
        
        destination = st.text_input("Destination")
        date_of_visit = st.date_input("Date of Visit")
        
        overall_rating = st.slider("Overall Rating", 1, 5, 5)
        
        review_title = st.text_input("Review Title")
        detailed_review = st.text_area("Detailed Review")
        
        travel_type = st.selectbox("Travel Type", ["Solo", "Family", "Friends", "Couple", "Business"])
        budget_type = st.selectbox("Budget", ["Budget", "Standard", "Luxury"])
        
        visited_attractions = st.text_input("Visited Attractions (comma separated)")
        favorite_place = st.text_input("Favorite Place")
        tips = st.text_area("Tips for Other Travelers")
        
        would_visit_again = st.radio("Would Visit Again?", ["Yes", "No"])
        
        uploaded_files = st.file_uploader("Upload Images (jpg, jpeg, png)", accept_multiple_files=True, type=["jpg", "jpeg", "png"])
        
        submit = st.form_submit_button("Submit Experience")
        
        if submit:
            if not destination or not review_title:
                st.error("Please fill in the Destination and Review Title.")
            else:
                image_paths = save_uploaded_files(uploaded_files) if uploaded_files else []
                
                review_data = {
                    "destination": destination,
                    "date": date_of_visit.strftime("%Y-%m-%d"),
                    "rating": overall_rating,
                    "title": review_title,
                    "review": detailed_review,
                    "travel_type": travel_type,
                    "budget": budget_type,
                    "visited_attractions": [a.strip() for a in visited_attractions.split(",") if a.strip()],
                    "favorite_place": favorite_place,
                    "tips": tips,
                    "would_visit_again": would_visit_again,
                    "images": image_paths,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                save_review(review_data)
                st.success("Your travel experience has been shared successfully!")
                st.rerun()
                
    st.divider()
    
    st.subheader("Recent Traveler Experiences")
    reviews = load_reviews()
    
    if reviews:
        for r in reversed(reviews): # Newest first
            with st.container():
                st.markdown(f"### {r['title']} {'⭐'*r['rating']}")
                st.markdown(f"**Destination:** {r['destination']} | **Date:** {r['date']} | **Type:** {r['travel_type']}")
                st.write(r['review'])
                
                if r.get("tips"):
                    st.info(f"**Tips:** {r['tips']}")
                
                if r.get("images"):
                    cols = st.columns(min(3, len(r["images"])))
                    for i, img_path in enumerate(r["images"]):
                        if os.path.exists(img_path):
                            cols[i % 3].image(img_path, width=200)
                
                st.divider()
    else:
        st.info("No experiences shared yet. Be the first to share your journey!")

if __name__ == "__main__":
    main()
