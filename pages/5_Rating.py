import streamlit as st
import json
import os
from datetime import datetime

DATA_FILE = os.path.join("data", "feedback.json")

def load_feedback():
    if not os.path.exists("data"):
        os.makedirs("data")
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_feedback(data):
    feedback_list = load_feedback()
    feedback_list.append(data)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(feedback_list, f, indent=4)

def main():
    st.set_page_config(page_title="Feedback & Rating - AI-TravelMate", page_icon="⭐")
    
    st.title("⭐ Rate & Feedback")
    st.markdown("We'd love to hear about your experience using AI-TravelMate!")
    
    feedback_list = load_feedback()
    
    # Calculate stats
    total_reviews = len(feedback_list)
    avg_rating = 0.0
    if total_reviews > 0:
        avg_rating = sum([f["overall_rating"] for f in feedback_list]) / total_reviews
        
    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.metric("Average Rating", f"{avg_rating:.1f} / 5.0")
    with col_stat2:
        st.metric("Total Reviews", total_reviews)
        
    st.divider()
    
    with st.form("feedback_form", clear_on_submit=True):
        st.subheader("Submit Your Feedback")
        
        name = st.text_input("Name (optional)")
        email = st.text_input("Email (optional)")
        
        overall = st.selectbox("Overall Rating", [5, 4, 3, 2, 1], format_func=lambda x: f"{x} Star{'s' if x>1 else ''}")
        ease_of_use = st.slider("Ease of Use", 1, 5, 5)
        design = st.slider("Design Rating", 1, 5, 5)
        trip_quality = st.slider("Trip Quality Rating", 1, 5, 5)
        
        comments = st.text_area("Comments")
        suggestions = st.text_area("Suggestions")
        
        would_recommend = st.radio("Would you recommend us?", ["Yes", "No"])
        
        submitted = st.form_submit_button("Submit Feedback")
        
        if submitted:
            feedback_data = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "name": name if name else "Anonymous",
                "email": email,
                "overall_rating": overall,
                "ease_of_use": ease_of_use,
                "design": design,
                "trip_quality": trip_quality,
                "comments": comments,
                "suggestions": suggestions,
                "would_recommend": would_recommend
            }
            save_feedback(feedback_data)
            st.success("Thank you for your valuable feedback.")
            # Reload page basically
            st.rerun()
            
    st.divider()
    
    st.subheader("Recent Feedback")
    if feedback_list:
        for f in reversed(feedback_list[-5:]): # Show last 5
            with st.container():
                st.markdown(f"**{f['name']}** rated it {'⭐'*f['overall_rating']} ({f['date']})")
                if f['comments']:
                    st.write(f"*{f['comments']}*")
                st.divider()
    else:
        st.info("No feedback submitted yet. Be the first!")

if __name__ == "__main__":
    main()
