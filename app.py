from openai import OpenAI
import streamlit as st

st.title("AI Python Debugger")
bg="""
<style>
[data-testid="stAppViewContainer"]{
  background-color: pink;
}
</style>
"""
st.markdown(bg,unsafe_allow_html=True)


f=open("keys\.demo_key.txt")
key=f.read()
client=OpenAI(api_key=key)


label="Enter your python code"
prompt=st.text_area(label)


if st.button("Generate")==True:
  response= client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
      {'role':'system','content':"""You are a helpful AI assistant.
            The given python code contains some error identify that error and debug the code and give the correct code as output"""},
      {'role':'user','content':prompt}
      ]
  )
  st.write(response.choices[0].message.content)

