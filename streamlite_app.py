import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Mom\'s New Healthy Dinner') 
streamlit.header ('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) 
fruits_to_show= my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)
#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

#fruit_choice = streamlit.text_input('What fruit would you like to add?')

my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
#streamlit.stop()

streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlite.error("Please select fruit to get information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit" + fruit_chice) 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    steamlit.dataframe(fruityvice_normalized)  
except URLError as e:
    streamlit.error()
                                      
    
