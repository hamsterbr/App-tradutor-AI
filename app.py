import streamlit as st
from deep_translator import GoogleTranslator

# NOVO CÓDIGO PARA O BACKGROUND
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://get.wallhere.com/photo/anime-Love-Live-Minami-Kotori-bikini-anime-girls-1375151.jpg?q=80&w=1974&auto=format&fit=crop");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Chamada da função para aplicar o background
add_bg_from_url()
# FIM DO NOVO CÓDIGO

st.title("🌍 Tradutor do Ratão")

#Área de textos
texto = st.text_area(" Digite sua frase em português:", 
                     "Olá! não sei oque estou fazendo da vida.")

# Seleção de idiomas
linguas = {
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Italiano": "it"
    "Japones": "ja"
}

idiomas_escolhidos = st.multiselect("Selecione os idiomas de destino:", list(linguas.keys()), ["Japones","Inglês", "Espanhol","Alemão"])

#traduzir
if st.button("Traduzir"):
    if texto.strip() == "":
        st.warning("Digite uma frase para traduzir!")
    else:
        for nome in idiomas_escolhidos:
            codigo = linguas[nome]
            traducao = GoogleTranslator(source='pt', target=codigo).translate(texto)
            st.subheader(f'➡ Tradução para {nome} ({codigo})')
            st.write(f'**Original:** {texto}')
            st.write(f'**Traduzido:** {traducao}')
            st.write("---")

