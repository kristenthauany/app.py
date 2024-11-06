import streamlit as st
from datetime import datetime

# Defina a data da viagem
data_viagem = datetime(2024, 12, 16, 18, 0)

# Função para calcular o tempo restante
def cronometro_viagem():
    agora = datetime.now()
    tempo_restante = data_viagem - agora
    
    if tempo_restante.total_seconds() > 0:
        dias = tempo_restante.days
        horas, resto = divmod(tempo_restante.seconds, 3600)
        minutos, segundos = divmod(resto, 60)
        return dias, horas, minutos, segundos
    else:
        return 0, 0, 0, 0

# Aplicando o estilo CSS para o fundo verde e centralização
st.markdown(
    """
    <style>
    .stApp {
        background-color: #002b00; /* verde escuro */
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
    }
    .cronometro-box {
        background-color: #003300;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: #ccffcc;
        font-size: 24px;
        font-weight: bold;
        width: 300px; /* aumenta a largura para caber o texto em linha */
        margin: 20px auto;
    }
    .imagem-box {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .texto-emoji {
        text-align: center;
        color: #ccffcc;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Mostra o tempo restante com texto e cronômetro na mesma linha
dias, horas, minutos, segundos = cronometro_viagem()
st.markdown(
    f"""
    <div class='imagem-box'>
        <div class='cronometro-box'>
            Tempo para ver meu amor:<br>
            <span style="font-size: 28px;">{dias}d {horas}h {minutos}m {segundos}s</span>
        </div>
        <img src='https://i.imgur.com/xG9tzBD.png' width='80'>
    </div>
    """,
    unsafe_allow_html=True
)

# Mensagem de amor com o mesmo estilo
st.markdown("<div class='texto-emoji'>Lembre-se sempre: Eu te amo demais!</div>", unsafe_allow_html=True)
