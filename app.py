import streamlit as st
import google.generativeai as genai

import db
messages=[]
apikey = "AIzaSyAnt9SYqPnO7eR7PVf1vulLvvN5Nm8mXdo"
genai.configure(api_key=apikey)
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Herbal Assistant", layout="wide", initial_sidebar_state="collapsed")
option=st.sidebar.selectbox("Select the Page",['Home Page','ChatBot'])

if option=='Home Page':
    import streamlit as st

    # Title and Introduction
    st.title("Getting Started with Herbs 🌿")
    st.subheader("A Beginner's Guide to Understanding the Types, Uses, and Benefits of Herbs")

    # Introduction to Herbs
    st.write("""
    Herbs have been a part of human history, adding flavor, fragrance, and healing properties to our lives. 
    Whether you're a seasoned cook, a health enthusiast, or just curious, this guide will introduce you to 
    the basics of herbs, covering types, uses, and amazing benefits.
    """)

    # Display a featured image of herbs
    st.image("12_medicinal_plants_and_flowers-f.jpg", caption="A Glimpse of Nature's Healing Wonders")

    # Types of Herbs
    st.header("Types of Herbs")
    st.write("""
    Herbs come in many varieties and are used for different purposes. Here’s a look at some popular types:
    - **Culinary Herbs**: Basil, thyme, rosemary - essential for adding flavor to dishes.
    - **Medicinal Herbs**: Echinacea, ginseng, chamomile - known for therapeutic benefits.
    - **Aromatic Herbs**: Lavender, mint, sage - beloved for their calming and refreshing scents.
    """)
    st.image("Herbs-and-Spices-Names-in-English.jpg", caption="Examples of Culinary, Medicinal, and Aromatic Herbs")

    # Detailed Use Cases of Herbs with Interactive Tips
    st.header("Herb Use Cases")
    st.write("""
    Herbs are versatile and can be used across a range of applications:
    1. **Culinary Uses**: Fresh herbs are often added to dishes to enhance flavor and health benefits.
    2. **Medicinal Uses**: Herbs contain active compounds that may support healing and well-being.
    3. **Cosmetic Uses**: Often used in skincare and haircare for their soothing properties.
    4. **Household Uses**: Aromatic herbs are used in natural cleaning solutions, potpourri, and incense.
    """)

    st.image("Cookingwiththyme-GettyImages-645388613-593dcf6b3df78c537b15a281.jpg", caption="Herbs Adding Freshness to Everyday Cooking")

    st.subheader("Did You Know?")
    if st.checkbox("Click to reveal a fascinating fact!"):
        st.write(
            "Many herbs, like rosemary, not only add flavor to dishes but can also support cognitive health and memory!")


    st.header("Benefits of Herbs")
    st.write("""
    Using herbs can transform many aspects of daily life, from food to health. Here are some reasons why herbs are invaluable:
    """)
    benefits = {
        "Natural Ingredients": "Herbs offer a safer, plant-based alternative to artificial products.",
        "Health Benefits": "Certain herbs have anti-inflammatory and immune-boosting properties.",
        "Environmental Benefits": "Growing herbs promotes biodiversity and is often sustainable.",
        "Cost-Effective": "Many herbs are easy to grow at home, reducing the need for store-bought products."
    }
    for benefit, description in benefits.items():
        st.markdown(f"**{benefit}**: {description}")


    st.header("Adoption Rate of Herbs 🌎")
    st.write("""
    As people seek more natural and holistic lifestyles, the popularity of herbs has surged worldwide.
    The adoption rate differs based on purpose and region:
    - **Culinary Herbs**: High global demand, especially in gourmet and health-conscious cuisines.
    - **Medicinal Herbs**: Alternative medicine practices in Asia and Europe show high adoption.
    - **Aromatic Herbs**: Widely used in aromatherapy and personal care.
    """)
    st.image("Africa_Herbs_Map_optimised_720.jpg", caption="Herb Popularity Across Continents")

    # Fun Quiz Section to Engage Users
    st.header("Quick Quiz: Test Your Herb Knowledge!")
    quiz_answer = st.radio("Which of these herbs is known for its calming effect?", ["Choose option","Thyme", "Lavender", "Basil"])
    if quiz_answer=='Choose option':
        st.write("Choose 1")

    elif quiz_answer == "Lavender":
        st.write("Correct! Lavender is known for its relaxing and calming properties.")
    else:
        st.write("Not quite. Try again or explore more about lavender in the Aromatic Herbs section!")

    # Wrap-up with an Inspiring Quote
    st.write("""
    Exploring the world of herbs is like diving into nature’s treasure chest. Whether you’re adding basil to pasta, brewing a calming chamomile tea, or growing lavender at home, herbs offer unique ways to enrich your life.
    """)
    st.markdown("> _“Nature itself is the best physician.” – Hippocrates_")

    # Final Image for Inspiration
    st.image("hq720.jpg", caption="Create Your Own Herb Garden and Embrace Nature’s Benefits")

    st.write("Stay curious, experiment, and let herbs bring flavor, fragrance, and health into your life!")


else:
    chat = model.start_chat(history=messages)

    def display_message(message, sender):
        if sender == "model":
            st.markdown(f"""
                <div style="text-align: left; background-color: #FAF9F6; color: #333; padding: 12px 16px; border-radius: 12px; margin-bottom: 12px; margin-right: 40%; font-size: 16px;">
                    {message}
            
            """, unsafe_allow_html=True)
        else:

            st.markdown(f"""
                <div style="text-align: right; background-color: #4CAF50; color: #fff; padding: 12px 16px; border-radius: 12px; margin-bottom: 12px; margin-left: 40%; font-size: 16px;">
                    {message}
                </div>
            """, unsafe_allow_html=True)

    st.title("Herbal Assistant")
    st.markdown("Ask me anything about herbs, and I'll provide information to the best of my knowledge.")




    st.markdown("""
        <style>
    
        .stTextArea {
            
            width: 90%; 
            height:100px;
            bottom: 20px; 
            z-index: 100;
            position: fixed;
    }
        </style>
    """, unsafe_allow_html=True)

    user_input = st.text_area("What would you like to know?",  placeholder="Enter your question here...", label_visibility="collapsed")

    if user_input:
        response = chat.send_message("Assume you are herbalist and u have indepth knowledge of herbs and now the User is asking "+user_input)
        messages.append({"role": "user", "parts": user_input})
        messages.append({"role": "model", "parts": response.text})


    for msg in messages:
        display_message(msg["parts"], msg["role"])
