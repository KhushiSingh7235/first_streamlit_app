import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 omega 3 & blueberry oatmeal')
streamlit.text('🥗 kale,spinach & rocket smoothie')
streamlit.text('🐔 hard-boiled free-range egg')
streamlit.text(' 🥑🍞 avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
def grt_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized =pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#new display
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information.")
  else:
    back_from_function = grt_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def grt_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
#Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=grt_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    
#Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values ('from streamlit')")
       return "Thanks for adding" +new_fruit
       
add_my_fruit=streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the List'):
    my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"]
    back_from_function=insert_row_snowflake(add_my_fuit)
    streamlit.text(back_from_function)
                                       
