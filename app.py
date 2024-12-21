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
        messages=messages,
    )
    return response.choices[0].message.content


def generate_image_1(api_key, prompt):
    openai.api_key = api_key
    response = openai.images.generate(
        model='dall-e-3',
        prompt=prompt,
        size='1024x1024',
        quality='standard',
        n=1,
    )
    return response.data[0].url


def generate_image_2(api_key, prompt):
    openai.api_key = api_key
    response = openai.images.generate(
        model='dall-e-3',
        prompt=prompt,
        size='1024x1024',
        quality='standard',
        n=1,
    )
    return response.data[0].url


def generate_image_3(api_key, prompt):
    openai.api_key = api_key
    response = openai.images.generate(
        model='dall-e-3',
        prompt=prompt,
        size='1024x1024',
        quality='standard',
        n=1,
    )
    return response.data[0].url


def generate_spot(api_key, user_text):
    openai.api_key = api_key
    messages = [
        {"role": "system", "content": "Jesteś ekspertem od spraw marketingu tworzysz chwytliwe spoty marketingowe które zapadają na długo w pamięci"},
        {"role": "user", "content": f"Na podstawie opisu użytkownika stwórz chwytliwy spot marketingowy, może być krótki, ale konkretny i treściwy oraz wymyśl trzy hasła marketingowe. Oto opis{user_text}"},
    ]
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content


st.set_page_config(layout='wide')

with st.sidebar:
    st.header('to be added')

c1, c2, c3 = st.columns([2, 2, 2])
with c1:
    if "generated_plan" not in st.session_state:
        st.session_state["generated_plan"] = ""
    
    if "api_key" not in st.session_state:
        st.session_state["api_key"] = ""

    if "images" not in st.session_state:
        st.session_state["images"] = []

    if "spot" not in st.session_state:
        st.session_state["spot"] = ""

    st.header(":blue[BrandSpark]✨")
    if not st.session_state["api_key"]:
        api_key = st.text_input("wprowadź swój klucz API OpenAI", key='api', type='password', value=st.session_state["api_key"])
        if api_key:
            st.session_state["api_key"] = api_key
            st.rerun()
        
    if st.session_state["api_key"]:
        description = st.text_area("Opisz dokładnie jaką kampanie mamy ci wygenerować, im :red[więcej szczegółów] tym :green[lepszy rezultat]")
        st.markdown("""
            <style>
            .stRadio > label { display: flex; }
            .stRadio > div { flex-direction: row; }
            </style>
        """, unsafe_allow_html=True)
        option = st.selectbox("Wybierz liczbe plakatów do wygenerowania:", [1, 2, 3])
        if st.button("Generuj"):
            if not st.session_state["api_key"]:
                st.info("Najpierw wprowadź klucz API")
            if not description:
                st.info("Najpierw podaj opis kampanii")
            else:
                plan = generate_plan(st.session_state["api_key"], description)
                st.session_state["generated_plan"] = plan
                
                if option == 1:
                    st.session_state["images"] = (
                        generate_image_1(st.session_state["api_key"], st.session_state["generated_plan"]),
                    )

                if option == 2:
                    st.session_state["images"] = (
                        generate_image_1(st.session_state["api_key"], st.session_state["generated_plan"]),
                        generate_image_2(st.session_state["api_key"], st.session_state["generated_plan"])
                    )

                if option == 3:
                    st.session_state["images"] = (
                        generate_image_1(st.session_state["api_key"], st.session_state["generated_plan"]),
                        generate_image_2(st.session_state["api_key"], st.session_state["generated_plan"]),
                        generate_image_3(st.session_state["api_key"], st.session_state["generated_plan"])
                    )

                spot = generate_spot(st.session_state["api_key"], description)
                st.session_state["spot"] = spot

        if st.session_state["generated_plan"]:
            st.write(st.session_state["generated_plan"])

with c2:
    st.subheader('Tu pojawią się przykładowe :red[plakaty]:')
       
    if st.session_state["images"]:
        st.image(st.session_state["images"])

with c3:
    st.subheader("Proponowane hasła reklamowe oraz krótki spot")

    if st.session_state["spot"]:
        st.write(st.session_state["spot"])
