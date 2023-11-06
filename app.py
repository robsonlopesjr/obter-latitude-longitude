import streamlit as st


st.set_page_config(
    page_title='Obtenção de Latitude e Longitude',
    page_icon='🗺️',
    layout='wide'
)

list_uf = [
    "AC",
    "AL",
    "AP",
    "AM",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MG",
    "MS",
    "MT",
    "PA",
    "PB",
    "PE",
    "PI",
    "PR",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
    "TO",
]

st.title('Formulário para obtenção da Latitude e Longitude de um endereço')
st.subheader('Todos os campos abaixo são obrigatórios')

with st.form(key='my_form'):
    input_address = st.text_input(
        label="Digite o nome da Rua/Avenida"
    )

    input_number = st.number_input(
        label="Digite o número",
        min_value=1,
        step=1
    )

    input_neighborhood = st.text_input(
        label="Digite o nome do Bairro",
    )

    input_city = st.text_input(
        label="Digite o nome da Cidade",
    )

    input_uf = st.selectbox(
        label="UF",
        options=list_uf
    )

    input_button_submit = st.form_submit_button(label="Obter Dados")

    if input_button_submit:
        if not input_address or not input_number or not input_neighborhood or not input_city or not input_uf:
            st.error("Há campos que não foram preenchidos!", icon="🚨")
        else:
            st.success("Todos os campos foram preenchidos!", icon="✅")


