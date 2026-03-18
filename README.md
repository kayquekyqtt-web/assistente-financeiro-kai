Assistente Financeiro com IA

Aplicação interativa desenvolvida em Python que simula um **assistente financeiro de um banco digital**, utilizando **inteligência artificial, análise de dados e linguagem natural**.

O sistema permite registrar gastos, visualizar análises financeiras e receber orientações personalizadas com base no contexto do usuário.

---

Funcionalidades

* Chat interativo com IA (Streamlit)
* Registro de gastos via linguagem natural
  Ex: `gasto 50`
* Resumo financeiro automático:

  * Total gasto
  * Média
  * Maior gasto
* Simulações financeiras simples
  Ex: `simular 100 12`
* Respostas inteligentes com IA contextualizada
* FAQ financeiro dinâmico (educação financeira)
* Persistência de contexto durante a sessão

---

Tecnologias utilizadas

* Python
* Streamlit
* Pandas
* OpenAI API (IA generativa)

---

Arquitetura da Solução

A aplicação é estruturada em três camadas principais:

* **Interface (Streamlit)**
  Responsável pela interação com o usuário via chat

* **Processamento (Python)**
  Interpretação de comandos e controle de fluxo

* **Inteligência (OpenAI API)**
  Geração de respostas contextualizadas utilizando IA generativa

Os dados financeiros são armazenados em memória utilizando listas e dicionários, e analisados com `pandas`.

---

Fluxo da aplicação

1. Usuário envia uma mensagem no chat
2. O sistema identifica a intenção:

   * registro de gasto
   * consulta de resumo
   * simulação
   * pergunta geral
3. Atualiza os dados financeiros (se necessário)
4. Gera resposta:

   * via lógica local (resumo/simulação)
   * ou via IA (OpenAI)
5. Exibe a resposta no chat

---

Uso de IA

O sistema utiliza um **prompt estruturado** para:

* interpretar linguagem natural
* considerar o contexto financeiro do usuário
* fornecer respostas claras e práticas
* sugerir melhorias financeiras

Isso permite uma experiência mais próxima de assistentes reais de bancos digitais.

---

Como executar o projeto

1. Clone o repositório

```bash
git clone https://github.com/kayquekyqtt-web/assistente-financeiro-kai.git
```

2. Acesse a pasta

```bash
cd assistente-financeiro-kai
```

3. Instale as dependências

```bash
pip install streamlit pandas openai
```

Configure sua API Key

No arquivo `main.py`:

```python
cliente = OpenAI(api_key="SUA_API_KEY_AQUI")
```

Execute a aplicação

```bash
streamlit run main.py
```

---

Exemplos de uso

Registro de gastos

* `gasto 50`
* `gasto 120`

Análise financeira

* `resumo`
* `como posso melhorar meus gastos?`

Simulações

* `simular 100 12`

Perguntas financeiras

* `como criar uma reserva de emergência?`
* `vale a pena investir todo mês?`
* `como evitar dívidas no cartão?`

---

Objetivo do Projeto

Este projeto foi desenvolvido para:

* Aplicar conceitos de **Python e análise de dados**
* Integrar **IA generativa em aplicações reais**
* Simular soluções utilizadas em **bancos digitais**
* Criar uma experiência baseada em **linguagem natural e contexto**

---

Diferenciais

* Integração entre **dados + IA + interface**
* Uso de **contexto dinâmico** para respostas personalizadas
* Interpretação de comandos em linguagem natural
* Estrutura modular e escalável
* Foco em experiência do usuário (UX)

---

Limitações

* Os dados não são persistidos após encerrar a aplicação
* As categorias de gastos ainda são genéricas
* As simulações não consideram juros compostos

---

Melhorias futuras

* Persistência de dados (CSV ou banco)
* Gráficos interativos
* Classificação automática de gastos com IA
* Sistema de login
* Versão mobile

---

Demonstração

O projeto pode ser demonstrado com:

* Registro de gastos
* Exibição de resumo
* Simulação financeira
* Perguntas respondidas pela IA
