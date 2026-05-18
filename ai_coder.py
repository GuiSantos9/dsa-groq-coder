import os
import streamlit as st
from groq import Groq
from groq.types.chat import chat_completion
from rich import markdown

# configura o header da aplicação
st.set_page_config(
    page_title="AI CODER",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# prompt com as regras e instruções
CUSTOM_PROMPT =  """  
Você é o "AI Coder", um assistente de IA especialista em programação, com foco principal em Python. 
Sua missão é ajudar desenvolvedores iniciantes com dúvidas de programação de forma clara, precisa e útil.  
  
REGRAS DE OPERAÇÃO:  
1.  **Foco em Programação**: Responda apenas a perguntas relacionadas a programação, algoritmos,
 estruturas de dados, bibliotecas e frameworks. Se o usuário perguntar sobre outro assunto, 
 responda educadamente que seu foco é exclusivamente em auxiliar com código.  
2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:  
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado.
     Seja direto e didático.   
    * **Exemplo de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta.
     O código deve ser bem comentado para explicar as partes importantes.    
     * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do 
     código faz, explicando a lógica e as funções utilizadas.    
     * **Documentação de Referência**: Ao final, inclua uma seção chamada "📚 Documentação de Referência" 
     com um link direto e relevante para a documentação oficial da Linguagem Python (docs.python.org) ou da biblioteca em questão.3.  
     **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.  
"""

# sidebar
with st.sidebar:
    # título
    st.title("AI Coder")

    # adiciona texto
    st.markdown("Um assitente de IA focado em programação Python para ajudar iniciantes")

    # campo para inserir a chave da API da Groq
    groq_api_key = st.text_input(
        "Insira sua chave API da Groq",
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    # divisórias e outras explicações
    st.markdown("===")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com Python. A IA pode cometer erros")

    st.markdown("===")
    st.markdown("Conheça os cursos individuais")

    # botão de link para enviar email para o suporte
    st.link_button("Email para o Suporte no Caso de Dúvidas", "guilhermeaugusto923@gmail.com")


# título principal da aplicação
st.title("GS AI Coder")

# subtítulo
st.title("Assitente Pessoal de Programação Python")

# texto auxiliar abaixo do título
st.caption("Faça perguntas sobre a linguagem python e obtenha o código, explicações e referências.")

# historico
# Inicializa o historico de mensagens da sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state.messages = []

# exibe as mensagens anteriores que foram armazenadas na sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

client = None

# verifica se o usuário forneceu a chave API da groq
if groq_api_key:
    try:

        # cria um cliente groq com a chave API fornecida
        client = Groq(api_key=groq_api_key)

    except Exception as e:

        # Exibe um erro caso haja problema na inicialização
        st.sidebar.error(f"Erro ao inicializar o cliente groq: {e}")
        st.stop()

# caso não tenha chave, mas já existam mensagens, mostra aviso
elif st.session_state.messages:
    st.warning("Por favor insira sua chave API da Groq na lateral para continuar!")

# captura a entrada do usuário do chat
if prompt := st.chat_input("Qual a sua dúvida sobre Python?"):

    if not client:
        st.warning("Por favor insira sua chave API da Groq na lateral para continuar!")
        st.stop()

    # armazena a mensagem do usuário no estado da sessão
    st.session_state.messages.append({"role": "user", "content": prompt})

    # exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # prepara a mensagem que será enviada na API incluindo o prompt
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        messages_for_api.append(msg)

    with st.chat_message("assistente"):

        with st.spinner("Analisando sua pergunta..."):

            try:
                # resultado da chamada de API
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model="meta-llama/llama-4-scout-17b-16e-instruct",
                    temperature = 0.7,
                    max_tokens = 8192,
                )

                # extrai a resposta gerada pela API
                resposta_da_ia = chat_completion.choices[0].message.content

                # exibe a resposta no Streamlit
                st.markdown(resposta_da_ia)

                st.session_state.messages.append({"role": "assistant","content": resposta_da_ia})

            except Exception as e:
                st.error(f"Erro ao inicializar o cliente groq: {e}")

st.markdown(
    """
    <div style="text-align: center; color black;">
        <hr>
        <p>AI Coder - Projeto pessoal de Guilherme Augusto dos Santos do curso Data Science Academy </p>
    </div>
    """,

    unsafe_allow_html=True,
)