import streamlit as st

st.title(":red[DecorAIze]")
st.subheader("LLM Enhanced Visulization for Interior Designs")

json = {"a":1, "b":2}
st.json(json)

code = '''
print("Hello World")
def func(a,b):
    return a+b
'''
st.header("Sample Code")
st.code(code,language = "python")

st.image("image.jpg")

def help():
    print(st.session_state.checker)

st.checkbox("Checkbox",value=True, key = "checker",on_change = help)
radio_btn = st.radio("Which is your county?", options=("India","USA","UK"))