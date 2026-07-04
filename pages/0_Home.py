import streamlit as st

# ── Hero Section ──────────────────────────────────────────────────────────────
st.markdown("<h1 style='text-align: center; font-size: 4rem;'>🌍 AI-TravelMate</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.5rem; color: gray;'>Your Personal AI Travel Companion</p>", unsafe_allow_html=True)
st.divider()

# ── Introduction + Inspiring Visual ──────────────────────────────────────────
col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("### 🚀 Welcome to AI-TravelMate")
    st.markdown(
        "Plan your dream vacation effortlessly with our advanced AI-powered platform. "
        "Whether you're looking for a relaxing beach retreat, a thrilling adventure, or a deep dive into history, "
        "AI-TravelMate handles all the heavy lifting to create the perfect itinerary just for you."
    )
    st.info("👈 Use the sidebar navigation to explore destinations, plan your trip, or leave feedback!")

with col2:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 20px;
        padding: 28px 24px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    ">
        <div style="font-size: 3rem; margin-bottom: 8px;">🏔️ 🌊 🌿 🌅</div>
        <p style="font-size: 1.1rem; font-style: italic; color: #a8dadc; margin-bottom: 16px;">
            "The world is a book, and those who do not travel read only one page."
        </p>
        <p style="font-size: 0.85rem; color: #ccc; margin-bottom: 20px;">— Saint Augustine</p>
        <hr style="border-color: #ffffff22; margin: 12px 0;">
        <div style="display: flex; justify-content: space-around; margin-top: 14px;">
            <div>
                <div style="font-size: 1.6rem;">🏝️</div>
                <div style="font-size: 0.75rem; color: #90e0ef;">Beaches</div>
            </div>
            <div>
                <div style="font-size: 1.6rem;">🧗</div>
                <div style="font-size: 0.75rem; color: #90e0ef;">Adventure</div>
            </div>
            <div>
                <div style="font-size: 1.6rem;">🌲</div>
                <div style="font-size: 0.75rem; color: #90e0ef;">Nature</div>
            </div>
            <div>
                <div style="font-size: 1.6rem;">🏛️</div>
                <div style="font-size: 0.75rem; color: #90e0ef;">Culture</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── Wow Factor: Travel Inspiration Banners ────────────────────────────────────
st.markdown("<h2 style='text-align: center;'>🌐 The World Awaits You</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Every journey begins with a single step. Let us plan yours.</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

wow1, wow2, wow3 = st.columns(3)

with wow1:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #2d6a4f, #52b788);
        border-radius: 16px; padding: 24px; color: white; text-align: center;
        box-shadow: 0 4px 15px rgba(45,106,79,0.4);
    ">
        <div style="font-size: 2.5rem;">🌿</div>
        <h3 style="color: white; margin: 10px 0 6px 0;">Into the Wild</h3>
        <p style="font-size: 0.88rem; color: #d8f3dc;">
            Misty forests, cascading waterfalls, and trails that lead to breathtaking viewpoints.
            Nature's silence is the loudest adventure.
        </p>
    </div>
    """, unsafe_allow_html=True)

with wow2:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #023e8a, #0096c7);
        border-radius: 16px; padding: 24px; color: white; text-align: center;
        box-shadow: 0 4px 15px rgba(0,150,199,0.4);
    ">
        <div style="font-size: 2.5rem;">🌊</div>
        <h3 style="color: white; margin: 10px 0 6px 0;">Coastal Dreams</h3>
        <p style="font-size: 0.88rem; color: #ade8f4;">
            Sun-drenched shores, turquoise lagoons, and the rhythmic sound of waves.
            Every beach holds a story — find yours.
        </p>
    </div>
    """, unsafe_allow_html=True)

with wow3:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #7b2d8b, #c77dff);
        border-radius: 16px; padding: 24px; color: white; text-align: center;
        box-shadow: 0 4px 15px rgba(123,45,139,0.4);
    ">
        <div style="font-size: 2.5rem;">🏔️</div>
        <h3 style="color: white; margin: 10px 0 6px 0;">Peak Seekers</h3>
        <p style="font-size: 0.88rem; color: #e7c6ff;">
            Conquer summits, breathe rarified air, and witness the world from the top.
            Mountains teach patience and reward courage.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Travel Stats ─────────────────────────────────────────────────────────────
st.markdown("<h3 style='text-align: center;'>🌟 Why Travelers Love Us</h3>", unsafe_allow_html=True)

stat1, stat2, stat3, stat4 = st.columns(4)
with stat1:
    st.metric("🗺️ Destinations", "50+", "In our knowledge base")
with stat2:
    st.metric("🤖 AI Agents", "4", "Working for you")
with stat3:
    st.metric("📴 Offline", "100%", "No internet needed")
with stat4:
    st.metric("⚡ Generation", "Instant", "Real-time planning")

st.divider()

# ── Feature Highlights ────────────────────────────────────────────────────────
st.markdown("<h2 style='text-align: center;'>✨ Features</h2>", unsafe_allow_html=True)

col_feat1, col_feat2, col_feat3 = st.columns(3)

with col_feat1:
    st.markdown("### ✈️ Trip Planner")
    st.write("Generate personalized itineraries offline based on your budget, travelers, and specific interests.")

with col_feat2:
    st.markdown("### 🗺️ Destination Explorer")
    st.write("Browse beautiful destinations, popular attractions, famous foods, and local tips to inspire your next trip.")

with col_feat3:
    st.markdown("### ⭐ Share & Rate")
    st.write("Share your travel experiences and upload photos to help other travelers, and rate our app!")

st.divider()

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.page_link("pages/1_Trip_Planner.py", label="Start Planning Now", icon="✈️")
st.markdown("</div>", unsafe_allow_html=True)
