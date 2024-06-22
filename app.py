import streamlit as st
from vanna.remote import VannaDefault
import os
# Set your Vanna API key 
api_key = os.environ.get("VANNA_API_KEY")
vanna_model_name = 'chinook'  # Assuming 'chinook' is your model name

# Initialize Vanna
vn = VannaDefault(model=vanna_model_name, api_key=api_key)

vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')

my_question = st.session_state.get("my_question", default=None)
if my_question is None:
    #st.image("chinook.png", use_column_width=True)
    my_question = st.text_input("Ask me a question that I can turn into SQL", key="my_question")
else:
    st.title(my_question)
    sql = vn.generate_sql(my_question)
    st.code(sql, language='sql')
    df = vn.run_sql(sql)    
    st.dataframe(df, use_container_width=True)
    fig = vn.get_plotly_figure(plotly_code=vn.generate_plotly_code(question=my_question, sql=sql, df=df), df=df)
    st.plotly_chart(fig, use_container_width=True)
    st.button("Ask another question", on_click=lambda: st.session_state.clear())
