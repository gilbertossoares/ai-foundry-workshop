# Lab 4: Frameworks de LLM - Desenvolvendo com Semantic Kernel, AutoGen e LangChain

> **⚠️ Nota**: Este laboratório está em desenvolvimento. O notebook `lab4.ipynb` será disponibilizado em breve com exercícios práticos.

Este laboratório apresenta uma visão geral dos principais frameworks para desenvolvimento de aplicações com Modelos de Linguagem de Grande Escala (LLMs), como o Semantic Kernel, AutoGen e LangChain. Estes frameworks fornecem ferramentas e abstrações para facilitar a integração e orquestração de LLMs em aplicações.

## Objetivos de Aprendizado

- Compreender o propósito e os casos de uso de cada framework
- Explorar exemplos básicos de implementação com cada tecnologia
- Comparar as abordagens dos diferentes frameworks
- Desenvolver um mini-projeto usando um dos frameworks

## Pré-requisitos

- Conhecimento básico de Python
- Familiaridade com conceitos de LLMs
- Ambiente de desenvolvimento Python configurado
- Chaves de API para Azure OpenAI Service

## Frameworks de LLM

### Semantic Kernel

O Semantic Kernel é um framework de código aberto desenvolvido pela Microsoft que permite integrar LLMs em aplicações de forma modular e estruturada.

#### Exemplo Básico com Semantic Kernel

```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion

# Inicializar o kernel
kernel = sk.Kernel()

# Configurar serviço AI
deployment_name = "text-davinci-003"
endpoint = "https://your-endpoint.openai.azure.com/"
api_key = "sua-chave-api"

# Adicionar o serviço de IA ao kernel
kernel.add_text_completion_service("demoservice", 
                                  AzureTextCompletion(deployment_name, endpoint, api_key))

# Criar uma função semântica
prompt_config = sk.PromptTemplateConfig.from_completion_parameters(
    max_tokens=2000,
    temperature=0.7,
    top_p=0.8
)

prompt_template = """
Resuma o seguinte texto em 3 pontos principais:
{{$input}}
"""

summary_function = kernel.create_semantic_function(
    prompt_template, 
    prompt_config, 
    "summarize", 
    "summary"
)

# Executar a função
text = "..."  # Texto longo aqui
summary = summary_function(text)
print(summary)
```

### AutoGen

AutoGen é um framework que permite criar, usar e otimizar agentes de IA que podem conversar entre si para resolver tarefas. Desenvolvido pela Microsoft, ele facilita a criação de fluxos multiagente.

#### Exemplo Básico com AutoGen

```python
import autogen

# Configurar os modelos
config_list = [
    {
        "model": "gpt-4",
        "api_key": "sua-chave-api",
    }
]

# Criar agentes
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
)

# Iniciar conversa entre agentes
user_proxy.initiate_chat(
    assistant,
    message="Crie uma função Python que calcule números Fibonacci até n."
)
```

### LangChain

LangChain é um framework popular para desenvolvimento de aplicações baseadas em LLMs, oferecendo componentes para lidar com documentos, memória, agentes e cadeias de processamento.

#### Exemplo Básico com LangChain

```python
from langchain.llms import AzureOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Configurar o LLM
llm = AzureOpenAI(
    deployment_name="text-davinci-003",
    model_name="text-davinci-003",
    openai_api_key="sua-chave-api",
    openai_api_base="https://your-endpoint.openai.azure.com/",
    openai_api_version="2022-12-01"
)

# Criar um template de prompt
prompt_template = PromptTemplate(
    input_variables=["produto"],
    template="Escreva uma descrição atrativa para o produto: {produto}"
)

# Criar uma chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Executar a chain
resultado = chain.run("Cafeteira programável")
print(resultado)
```

## Comparação dos Frameworks

| Framework | Pontos Fortes | Casos de Uso Ideais |
|-----------|---------------|---------------------|
| Semantic Kernel | Integração com ecossistema .NET, arquitetura de plugins, memória semântica | Aplicações empresariais, soluções Microsoft, integrações complexas |
| AutoGen | Agentes conversacionais, fluxos multiagente, flexibilidade | Automação de tarefas, sistemas colaborativos, desenvolvimento de protótipos rápidos |
| LangChain | Grande comunidade, diversos componentes prontos, documentação robusta | Recuperação de dados (RAG), chatbots, agentes de tarefas específicas |

## Exercício Prático

Escolha um dos frameworks apresentados e implemente uma aplicação simples que:

1. Carregue um documento de texto
2. Extraia informações relevantes
3. Gere um resumo baseado nas informações extraídas
4. Responda perguntas sobre o conteúdo

## Próximos Passos

- Explore projetos de código aberto que utilizam esses frameworks
- Experimente combinar diferentes frameworks em um único projeto
- Implemente um agente especializado para seu domínio de negócio
- Explore opções de deployment em produção com Azure

## Recursos Adicionais

- [Documentação do Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- [Documentação do AutoGen](https://github.com/microsoft/autogen)
- [Documentação do LangChain](https://langchain.readthedocs.io/)
- [Azure AI Studio](https://azure.microsoft.com/services/ai-studio/)
- [Curso de Construção de RAG Avançado](https://learn.microsoft.com/training/)