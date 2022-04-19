import streamlit

streamlit.title ('My Mom\'s new healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach and rocket smoothie')
streamlit.text('Hard boiled egg')
streamlit.text('Avocado toast')


streamlit.header ('Build your own Fruit Smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
