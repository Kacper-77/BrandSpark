import streamlit as st
import openai


def generate_plan(api_key, user_text):
    openai.api_key = api_key
    messages = [
        {"role": "system", "content": "Jesteś ekspertem w zakresie marketingu, opracowujesz profesjonalnie całe kampanie marketingowe i udzielasz wartościowych porad"},
        {"role": "user", "content": f"Sprawdź opis kampanii marketingowej i opracuj cały plan działania który pozwoli wypromować produkt klienta. Oto opis{user_text}"}
    ]
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content


st.set_page_config(layout='wide')

with st.sidebar:
    st.header('to be added')
   

# if "generated_plan" not in st.session_state:
#         st.session_state.generated_plan= ""

_, c, _ = st.columns([2, 2, 2])
with c:
    st.header("Generate your dreams")
    with st.expander("info"):
        st.write("to be added...")
    
    api_key = st.text_input("wprowadź swój klucz API OpenAI", key='api', type='password')

    description = st.text_area("Opisz dokładnie jaką kampanie mamy ci wygenerować")
    if st.button("Generuj"):
        plan = generate_plan(api_key, description)

        st.write(plan)