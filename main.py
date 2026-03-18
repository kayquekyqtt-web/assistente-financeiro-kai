import streamlit as st
import pandas as pd
from openai import OpenAI


cliente = OpenAI(api_key="")

st.set_page_config(page_title="Assistente Financeiro Kai", layout="centered")
st.title("💰 Assistente Financeiro com IA")

if "mensagens" not in st.session_state:
    st.session_state["mensagens"] = [
        {"role": "system", "content": "Você é um assistente financeiro claro, didático, responsável e prático."}
    ]

if "gastos" not in st.session_state:
    st.session_state["gastos"] = []

def gerar_resumo():
    if not st.session_state["gastos"]:
        return None

    df = pd.DataFrame(st.session_state["gastos"])

    return {
        "df": df,
        "total": df["valor"].sum(),
        "media": df["valor"].mean(),
        "maior": df["valor"].max()
    }

def simular_investimento(texto):
    try:
        palavras = texto.split()
        numeros = [float(p) for p in palavras if p.replace('.', '', 1).isdigit()]

        if len(numeros) >= 2:
            valor = numeros[0]
            meses = int(numeros[1])
            total = valor * meses
            return f"Investindo R$ {valor:.2f} por {meses} meses → R$ {total:.2f} (sem juros)."
    except:
        pass
    return None

for msg in st.session_state["mensagens"]:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

entrada = st.chat_input("Digite algo como: gasto 50 | resumo | simular 100 12 | dicas")

if entrada:
    st.chat_message("user").write(entrada)
    st.session_state["mensagens"].append({"role": "user", "content": entrada})

    texto = entrada.lower()
    resposta = ""

    if "gasto" in texto:
        try:
            valor = float(next(p for p in texto.split() if p.replace('.', '', 1).isdigit()))

            st.session_state["gastos"].append({
                "categoria": "geral",
                "valor": valor
            })

            resposta = f"✅ Gasto de R$ {valor:.2f} registrado."

        except:
            resposta = "⚠️ Use: gasto 50"

    elif "resumo" in texto:
        resumo = gerar_resumo()

        if not resumo:
            resposta = "📭 Nenhum gasto registrado."
        else:
            resposta = (
                f"📊 Resumo:\n"
                f"- Total: R$ {resumo['total']:.2f}\n"
                f"- Média: R$ {resumo['media']:.2f}\n"
                f"- Maior gasto: R$ {resumo['maior']:.2f}"
            )

            st.dataframe(resumo["df"])

    elif "simular" in texto:
        resposta = simular_investimento(texto)
        if not resposta:
            resposta = "⚠️ Ex: simular 100 12"

    else:
        resumo = gerar_resumo()

        contexto = "Sem dados financeiros." if not resumo else resumo["df"].to_string(index=False)

        prompt = f"""
Você é um assistente financeiro de um banco digital.

Regras:
- Seja claro, direto e útil
- Dê exemplos simples
- Sugira melhorias práticas
- Evite termos complexos

Dados do cliente:
{contexto}

Pergunta:
{entrada}
"""

        try:
            resposta_ia = cliente.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            resposta = resposta_ia.choices[0].message.content

        except Exception as e:
            resposta = f"Erro: {e}"

    st.chat_message("assistant").write(resposta)
    st.session_state["mensagens"].append({"role": "assistant", "content": resposta})
