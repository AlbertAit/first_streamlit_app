import streamlit

streamlit.title ('My Mom\'s new healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach and rocket smoothie')
streamlit.text('Hard boiled egg')
streamlit.text('Avocado toast')


streamlit.header ('Build your own Fruit Smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

import requests
fruity_vice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruity_vice_response.json())

fruityvice_normalized = pandas.json_normalize(fruity_vice_response.json())
streamlit.dataframe(fruityvice_normalized)
