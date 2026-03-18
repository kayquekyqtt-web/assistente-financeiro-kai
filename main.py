import openai

openai.api_key = ""

historico = []

def responder(pergunta):
    historico.append({"role": "user", "content": pergunta})

    resposta = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Você é um assistente financeiro claro, didático e responsável."}] + historico
    )

    texto = resposta.choices[0].message.content
    historico.append({"role": "assistant", "content": texto})

    return texto


def simular_investimento():
    try:
        valor = float(input("Quanto deseja investir por mês? "))
        meses = int(input("Por quantos meses? "))

        total = valor * meses

        print(f"\n💰 Resultado:")
        print(f"Investindo {valor} por {meses} meses, você acumulará R$ {total:.2f} (sem juros).")

    except:
        print("⚠️ Erro ao calcular. Tente novamente.")


while True:
    print("\n1 - Fazer pergunta")
    print("2 - Simular investimento")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        pergunta = input("Digite sua dúvida: ")
        resposta = responder(pergunta)
        print("\n🤖", resposta)

    elif opcao == "2":
        simular_investimento()

    elif opcao == "3":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
