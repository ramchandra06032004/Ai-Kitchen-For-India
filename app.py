import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import streamlit as st
from sklearn.preprocessing import StandardScaler
from helper import get_diet_index, get_course_index, get_cuisine_index


# Load data
main_data=pd.read_csv("WholeProcessedData.csv")

main_data.reset_index(drop=True, inplace=True)
data = pd.read_csv('processeeData.csv')
y=data.iloc[:,0:5].values
scaler = StandardScaler()
y = scaler.fit_transform(y)
from sklearn.neighbors import NearestNeighbors
model=NearestNeighbors(algorithm="brute")



st.title('Discover Your Next Favorite Dish!')
st.header("Tired of the same old meals? Craving something new and exciting? Look no further! Our food recommendation system is here to spice up your culinary adventures.")
st.write("Tell Us Your Preferences:")
st.header("How Much Time Do You Have to Cook?")

# Assuming 'st' is Streamlit
time_available = st.slider("Select the time you have available to make a dish (in minutes):", min_value=0, max_value=50, value=30)
st.write("You have selected:", time_available, "minutes")

st.header("Number of Servings Needed")
No_Of_Serving = st.slider("How many people are you cooking for?:", min_value=0, max_value=20, value=3)
st.write("You have selected:", No_Of_Serving)

Cuisines=main_data["Cuisine"].unique()
st.header("Preferred Cuisine")
preferred_cuisine = st.selectbox(
    "Which cuisine are you in the mood for?",
    options=Cuisines
)
st.write("You have selected:", preferred_cuisine, "cuisine")


Course=main_data["Course"].unique()
st.header("Type of Course")
selected_course_type = st.selectbox(
    "What type of course are you looking for?",
    options=Course
)
# Display the selected option
st.write("You have selected:", selected_course_type, "course")

st.header("Dietary Preferences")
Diet=main_data["Diet"].unique()
selected_diet_type = st.selectbox(
    "Any specific dietary requirements or preferences?",
    options=Diet
)
# Display the selected option
st.write("You have selected:", selected_diet_type, "diet")

preferred_cuisine=get_cuisine_index(preferred_cuisine)
selected_course_type=get_course_index(selected_course_type)
selected_diet_type=get_diet_index(selected_diet_type)

input_array=[time_available,No_Of_Serving,preferred_cuisine,selected_course_type,selected_diet_type]
input_array=scaler.transform([input_array])

if st.button('Submit'):
    model.fit(y)
    dist,indx=model.kneighbors(input_array,10)
    recipe_names = main_data.iloc[indx[0]]
    for index, row in recipe_names.iterrows():
        st.header("Name of recipe :-"+ str(row[2]))
        st.markdown("**Translated recipe name:** :-" + str(row[3]))
        st.markdown("**Ingredients** :-" + str(row[4]))
        st.markdown("**Translated ingredients:** :-" + str(row[5]))
        st.markdown("**Required time** :-" + str(row[8])+" Minutes")
        st.markdown("**instructions:** :-" + str(row[13]))
        st.markdown("**Number of servings** :-" + str(row[9]))
        st.markdown("**Cuisine** :-" + str(row[10]))
        st.markdown("**Course** :-" + str(row[11]))
        st.markdown("**Diet** :-" + str(row[12]))
        st.markdown("---")
        


    




