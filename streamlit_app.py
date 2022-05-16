import streamlit 

streamlit.title('My Parents New Healthy Diner') 

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal') 
streamlit.text('🍈Kale, Spinach & Rocket Smoothie') 
streamlit.text('🐔Hard-Boiled Free-Range Egg') 
streamlit.text('🥑🍞Avocado Toast')
streamlit.text('🍌🍋Build Your Own Smoothie 🥝🍇')

import pandas 
my_fruit_list=pandas.read_csv("https://uni-lab-files.se.us.west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
