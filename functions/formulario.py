import streamlit as st
def formInicial():
    placeholder = st.empty()

    with placeholder.form("my_form"):
        st.write("cambiao")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")
        submitButton= st.form_submit_button("enviar")
        if submitButton:
            placeholder.empty()

