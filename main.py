import streamlit as st
from openai import OpenAI


cliente = OpenAI(api_key="")

st.title("💰 Assistente Financeiro com IA")


if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = [
        {"role": "system", "content": "Você é um assistente financeiro claro, didático e responsável."}
    ]


for mensagem in st.session_state["lista_mensagens"]:
    if mensagem["role"] != "system":
        st.chat_message(mensagem["role"]).write(mensagem["content"])


texto_usuario = st.chat_input("Digite sua mensagem...")

def simular_investimento(texto):
    try:
        palavras = texto.split()
        numeros = [float(p) for p in palavras if p.replace('.', '', 1).isdigit()]

        if len(numeros) >= 2:
            valor = numeros[0]
            meses = int(numeros[1])
            total = valor * meses
            return f"💰 Se você investir {valor} por {meses} meses, terá aproximadamente R$ {total:.2f} (sem juros)."
    except:
        pass
    return None

if texto_usuario:
    
    st.chat_message("user").write(texto_usuario)

    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    
    resposta_simulacao = simular_investimento(texto_usuario)

    if resposta_simulacao:
        texto_resposta_ia = resposta_simulacao
    else:
        resposta_ia = cliente.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state["lista_mensagens"]
        )
        texto_resposta_ia = resposta_ia.choices[0].message.content

    
    st.chat_message("assistant").write(texto_resposta_ia)

    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
