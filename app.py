import pandas as pd
import streamlit as st

import random
import pickle

mobile_data = pd.DataFrame(pickle.load(open("mobiles.pkl", "rb")))
similarity = pickle.load(open("similarity.pkl", "rb"))


def user_interface():
    st.set_page_config(page_title="Mobile Recommender System", page_icon="📲", layout="wide",
                       initial_sidebar_state="expanded")

    st.title("Mobile Recommender System")

    selected_mobile = st.selectbox("Search Mobile Here", mobile_data["name"])

    if st.button("Recommend"):
        recommended_mobiles = recommend_mobiles(selected_mobile)
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.markdown(f"<p style='text-align: center;'>{recommended_mobiles[0][0]}<br/>"
                        f"Rating: {recommended_mobiles[0][1]}<br/>"
                        f"Price: {recommended_mobiles[0][2]}",
                        unsafe_allow_html=True)
            st.image(recommended_mobiles[0][3])
        with col2:
            st.markdown(f"<p style='text-align: center;'>{recommended_mobiles[1][0]}<br/>"
                        f"Rating: {recommended_mobiles[1][1]}<br/>"
                        f"Price: {recommended_mobiles[1][2]}",
                        unsafe_allow_html=True)
            st.image(recommended_mobiles[1][3])
        with col3:
            st.markdown(f"<p style='text-align: center;'>{recommended_mobiles[2][0]}<br/>"
                        f"Rating: {recommended_mobiles[2][1]}<br/>"
                        f"Price: {recommended_mobiles[2][2]}",
                        unsafe_allow_html=True)
            st.image(recommended_mobiles[2][3])
        with col4:
            st.markdown(f"<p style='text-align: center;'>{recommended_mobiles[3][0]}<br/>"
                        f"Rating: {recommended_mobiles[3][1]}<br/>"
                        f"Price: {recommended_mobiles[3][2]}",
                        unsafe_allow_html=True)
            st.image(recommended_mobiles[3][3])
        with col5:
            st.markdown(f"<p style='text-align: center;'>{recommended_mobiles[4][0]}<br/>"
                        f"Rating: {recommended_mobiles[4][1]}<br/>"
                        f"Price: {recommended_mobiles[4][2]}",
                        unsafe_allow_html=True)
            st.image(recommended_mobiles[4][3])

        st.markdown("---")
        st.markdown("## Other Suggestions")
        st.markdown("---")

        random_recommendation = random_suggestion(selected_mobile)
        col6, col7, col8, col9, col10 = st.columns(5)

        with col6:
            st.markdown(f"<p style='text-align: center;'>{random_recommendation[0][0]}<br/>"
                        f"Rating: {random_recommendation[0][1]}<br/>"
                        f"Price: {random_recommendation[0][2]}",
                        unsafe_allow_html=True)
            st.image(random_recommendation[0][3])
        with col7:
            st.markdown(f"<p style='text-align: center;'>{random_recommendation[1][0]}<br/>"
                        f"Rating: {random_recommendation[1][1]}<br/>"
                        f"Price: {random_recommendation[1][2]}",
                        unsafe_allow_html=True)
            st.image(random_recommendation[1][3])
        with col8:
            st.markdown(f"<p style='text-align: center;'>{random_recommendation[2][0]}<br/>"
                        f"Rating: {random_recommendation[2][1]}<br/>"
                        f"Price: {random_recommendation[2][2]}",
                        unsafe_allow_html=True)
            st.image(random_recommendation[2][3])
        with col9:
            st.markdown(f"<p style='text-align: center;'>{random_recommendation[3][0]}<br/>"
                        f"Rating: {random_recommendation[3][1]}<br/>"
                        f"Price: {random_recommendation[3][2]}",
                        unsafe_allow_html=True)
            st.image(random_recommendation[3][3])
        with col10:
            st.markdown(f"<p style='text-align: center;'>{random_recommendation[4][0]}<br/>"
                        f"Rating: {random_recommendation[4][1]}<br/>"
                        f"Price: {random_recommendation[4][2]}",
                        unsafe_allow_html=True)
            st.image(random_recommendation[4][3])


def recommend_mobiles(mobile_name):
    mobile_index = mobile_data[mobile_data["name"] == mobile_name].index[0]
    distances = similarity[mobile_index]
    mobiles_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    recommended_mobiles = []

    for i in mobiles_list:
        recommended_mobiles.append(mobile_data.iloc[i[0]])

    return recommended_mobiles


def random_suggestion(mobile_name):
    mobile_index = mobile_data[mobile_data["name"] == mobile_name].index[0]
    distance = similarity[mobile_index]
    mobiles_list = random.sample(list(enumerate(distance)), k=5)
    recommended_mobiles = []

    for i in mobiles_list:
        recommended_mobiles.append(mobile_data.iloc[i[0]])

    return recommended_mobiles


user_interface()
