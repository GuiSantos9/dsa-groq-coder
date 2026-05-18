# 🤖 GS AI Coder — Assistente Pessoal de Programação Python

> Estudo de Caso 1 — Curso **Fundamentos da Linguagem Python: Do Básico até a IA**

O **GS AI Coder** é um assistente de IA conversacional focado em Python, desenvolvido para acompanhar programadores iniciantes em sua jornada com a linguagem. A interação funciona como uma sala de aula virtual: você faz perguntas no chat e recebe respostas estruturadas com explicações, exemplos de código e referências à documentação oficial — tudo isso em tempo real, alimentado por um modelo de linguagem de última geração.

---

## ✨ Funcionalidades

- 💬 **Chat interativo** com histórico de conversa na sessão
- 🐍 **Foco exclusivo em Python** — o assistente redireciona perguntas fora do escopo
- 📋 **Respostas estruturadas** com explicação conceitual, código comentado, detalhes de implementação e links para a documentação oficial
- 🔑 **Chave de API configurável** diretamente pela interface (sidebar)
- ⚡ **Inferência ultrarrápida** via hardware LPU da Groq

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|---|---|---|
| Python | 3.12 | Linguagem principal |
| Streamlit | latest | Interface web interativa |
| Groq SDK | latest | Cliente para chamadas à API |
| LLM | `meta-llama/llama-4-scout-17b-16e-instruct` | Geração de respostas |

---

## 📁 Estrutura do Projeto

```
gs-ai-coder/
│
├── ai_coder.py        # Aplicação principal
└── requirements.txt   # dependências para instalação
```

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/gs-ai-coder.git
cd gs-ai-coder
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Obtenha sua chave de API da Groq

Acesse [console.groq.com/keys](https://console.groq.com/keys), crie uma conta gratuita e gere sua chave de API.

### 4. Execute a aplicação

```bash
streamlit run ai_coder.py
```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`.

### 5. Insira sua chave de API

Na barra lateral (sidebar), cole sua chave de API da Groq no campo indicado e comece a fazer suas perguntas.

---

## 💡 Como Usar

1. Com a aplicação aberta no navegador, insira sua **Groq API Key** na sidebar
2. Digite sua dúvida sobre Python no campo de chat
3. O assistente responderá com:
   - 📖 Explicação clara do conceito
   - 💻 Exemplo de código em Python comentado
   - 🔍 Detalhes sobre a lógica utilizada
   - 📚 Link para a documentação oficial

---

## ⚙️ Limites do Modelo Gratuito (Free Tier)

O modelo `meta-llama/llama-4-scout-17b-16e-instruct` na Groq oferece:

| Limite | Valor |
|---|---|
| Requisições por minuto (RPM) | 30 |
| Requisições por dia (RPD) | 1.000 |
| Tokens por minuto (TPM) | 30.000 |
| Tokens por dia (TPD) | 500.000 |

---

## 📚 Referências

- [Documentação do Streamlit](https://docs.streamlit.io)
- [Documentação da Groq](https://console.groq.com/docs)
- [Documentação oficial do Python](https://docs.python.org/3/)

---

## 👨‍💻 Autor

Desenvolvido como parte do curso **Fundamentos da Linguagem Python - Do Básico até a IA**.
