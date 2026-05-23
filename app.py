# 🌱 App Web: Cidades e Comunidades Sustentáveis (Versão por Link)
# Objetivo: permitir que qualquer pessoa acesse o app apenas clicando em um link
# Tecnologia: Streamlit (deploy web fácil)

import streamlit as st

st.set_page_config(page_title="Cidades Sustentáveis", page_icon="🌱")

st.title("🌱 Cidades e Comunidades Sustentáveis")
st.write("Acesse informações, atividades e ações sustentáveis diretamente pelo navegador.")

menu = st.sidebar.selectbox(
    "Escolha uma seção",
    ["Início", "Educação Ambiental", "Simulador de Resíduos", "Quiz Sustentável", "Ações Comunitárias"]
)

# ---------------- INÍCIO ----------------
if menu == "Início":
    st.header("Bem-vindo 🌍")
    st.write("Este app incentiva práticas sustentáveis, redução de resíduos e conscientização ambiental.")
    st.success("Acesse tudo direto pelo link após o deploy.")

# ---------------- EDUCAÇÃO ----------------
elif menu == "Educação Ambiental":
    st.header("📘 Educação Ambiental")

    st.markdown("- Separe corretamente o lixo reciclável")
    st.markdown("- Reduza o uso de plástico")
    st.markdown("- Economize água e energia")
    st.markdown("- Reutilize materiais")
    st.markdown("- Prefira transporte sustentável")

# ---------------- SIMULADOR ----------------
elif menu == "Simulador de Resíduos":
    st.header("♻️ Simulador de Resíduos")

    lixo = st.number_input("Resíduos gerados por dia (kg)", min_value=0.0, step=0.1)

    if "total" not in st.session_state:
        st.session_state.total = 0

    if st.button("Adicionar"):
        st.session_state.total += lixo

    st.info(f"Total acumulado: {st.session_state.total:.2f} kg")

    if st.button("Resetar"):
        st.session_state.total = 0
        st.warning("Valores resetados!")

# ---------------- QUIZ ----------------
elif menu == "Quiz Sustentável":
    st.header("🧠 Quiz Sustentável")

    score = 0

    q1 = st.radio("Reciclagem significa:",
        ["Reutilizar materiais", "Queimar lixo", "Descartar no rio"])

    q2 = st.radio("Boa prática ambiental:",
        ["Economizar água", "Desperdiçar energia", "Poluir rios"])

    if st.button("Ver resultado"):
        if q1 == "Reutilizar materiais":
            score += 1
        if q2 == "Economizar água":
            score += 1
        st.success(f"Pontuação: {score}/2")

# ---------------- AÇÕES ----------------
elif menu == "Ações Comunitárias":
    st.header("🤝 Ações Sustentáveis")

    acao = st.text_input("Digite uma ação sustentável")

    if "acoes" not in st.session_state:
        st.session_state.acoes = []

    if st.button("Adicionar ação"):
        if acao:
            st.session_state.acoes.append(acao)

    st.write("### Ações registradas:")
    for a in st.session_state.acoes:
        st.write("🌱", a)

st.sidebar.info("ODS 11 - Cidades e Comunidades Sustentáveis")

# ---------------- DEPLOY (LINK) ----------------
st.markdown("""
### 🚀 Como transformar em LINK (acesso pelo navegador):

1. Acesse: https://streamlit.io/cloud
2. Envie este código para um repositório GitHub
3. Clique em **Deploy App**
4. O Streamlit irá gerar um LINK público automático

➡ Exemplo de acesso:
`https://seu-app.streamlit.app`
""")
