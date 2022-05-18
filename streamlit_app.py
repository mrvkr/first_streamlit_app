import streamlit 

streamlit.title('My Parents New Healthy Diner') 

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal') 
streamlit.text('🍈Kale, Spinach & Rocket Smoothie') 
streamlit.text('🐔Hard-Boiled Free-Range Egg') 
streamlit.text('🥑🍞Avocado Toast')
streamlit.text('🍌🍋Build Your Own Smoothie 🥝🍇')


import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table
streamlit.dataframe(fruits_to_show)



#New Section to Display
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

#take json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#Output in table format
streamlit.dataframe(fruityvice_normalized)
