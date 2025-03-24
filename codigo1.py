import streamlit as st

st.title("Inversor de Frases")

# Entrada de texto
frase = st.text_input("Digite uma frase:")

# Botão para inverter a frase
if st.button("Inverter"):
    if frase:
        frase_invertida = frase[::-1]
        st.write("Frase invertida:", frase_invertida)
