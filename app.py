import streamlit as st

st.set_page_config(page_title="Neurologia Equina", page_icon="🐎")

st.title("🐎 Simulador de Lesões da Medula Espinhal em Equinos")

regiao = st.selectbox(
    "Região Medular",
    ["C1–C5","C6–T2","T3–L3","L4–S2","S1–Cd"]
)

lesao = st.selectbox(
    "Tipo de Lesão",
    ["Compressiva","Inflamatória/Infecciosa","Traumática","Degenerativa"]
)

grau = st.select_slider(
    "Grau da Lesão",
    options=["Leve","Moderada","Grave"]
)

if st.button("Gerar Simulação"):

    st.write("### Resultado")

    st.write("**Região:**", regiao)
    st.write("**Tipo:**", lesao)
    st.write("**Grau:**", grau)