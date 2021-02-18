import streamlit as st

st.sidebar.title("Calculadora de IMC") #escreva seu título aqui
st.sidebar.write("Informe abaixo seu peso e altura: ") #escreva seu texto aqui7
st.image("calc-guide.png", use_column_width=True)
nome = st.sidebar.text_input('Nome', 'Escreva seu nome')
idade = st.sidebar.number_input('Idade', value = 0)
altura = st.sidebar.slider("Altura", 0.00, 2.50, value = 1.70)
peso = st.sidebar.slider("Peso", 0.0, 300.0, value = 90.0)
botao = st.sidebar.button("Calcular")

if botao:
    IMC = peso/(altura**2)

    if IMC <= 18.5: classificacao = "Abaixo do peso"
    elif IMC <= 24.9: classificacao = "Peso normal"
    elif IMC <= 29.9: classificacao = "Sobrepeso"
    elif IMC <= 34.9: classificacao = "Obesidade (Grau I)"
    elif IMC <= 39.9: classificacao = "Obesidade Severa (Grau II)"
    else: classificacao = "Obesidade Mórbida (Grau III)"
    
    st.title(f"Olá **{nome}**!")
    st.markdown(f"Idade: **{idade}** anos")
    st.markdown(f"Peso: **{peso}** Kg")
    st.markdown(f"Altura: **{altura}** m")
    st.markdown("De acordo com os valores informados:")
    st.markdown(f"Seu IMC é: **{round(IMC,2)}**")
    st.markdown(f"Você está na faixa de: **{classificacao}**")