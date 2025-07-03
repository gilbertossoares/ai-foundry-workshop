# Lab 4: Frameworks Avançados - Semantic Kernel e AutoGen

## Visão Geral

Neste laboratório você explorará dois frameworks poderosos para construção de aplicações inteligentes: **Semantic Kernel** e **AutoGen** com Azure OpenAI. Aprenderá como criar agentes conversacionais, orchestrar múltiplos agentes, implementar plugins personalizados e desenvolver workflows complexos de automação.

O **Semantic Kernel** é um SDK open-source da Microsoft que permite integrar modelos de IA com linguagens de programação convencionais, oferecendo funcionalidades como plugins, planejamento e memória. O **AutoGen** é um framework da Microsoft para criar aplicações multi-agente onde diferentes agentes podem colaborar para resolver problemas complexos através de conversação estruturada.

## Objetivos

- ✅ Configurar e usar o Semantic Kernel com Azure OpenAI
- ✅ Criar e implementar plugins personalizados
- ✅ Trabalhar com templates de prompts e argumentos dinâmicos
- ✅ Configurar agentes AutoGen especializados
- ✅ Implementar sistemas multi-agente colaborativos
- ✅ Comparar abordagens entre Semantic Kernel e AutoGen
- ✅ Desenvolver sistema de análise de produtos combinando ambos

## Pré-requisitos

- Conhecimento básico de Python e programação assíncrona
- Familiaridade com conceitos de LLMs e IA generativa
- Conclusão dos Labs 1-3 (recomendado)
- Variáveis de ambiente configuradas no arquivo `.env`
- Acesso ao Azure OpenAI Service

## Conteúdo do Laboratório

### Exercício 1 - Configuração e Semantic Kernel

**Configuração Inicial**:
- Instalação das dependências necessárias
- Importação das bibliotecas (semantic-kernel, autogen)
- Carregamento das credenciais do Azure OpenAI
- Inicialização do kernel do Semantic Kernel

**Recursos Cobertos**:
- Configuração do AzureChatCompletion
- Adição de serviços ao kernel
- Estruturação básica para desenvolvimento

### Exercício 2 - Plugins e Funcionalidades Avançadas

**Plugins Built-in**:
- Exploração do TextPlugin integrado
- Operações de manipulação de texto
- Uso de plugins pré-construídos

**Plugin Personalizado - MathPlugin**:
- Criação de plugin para operações matemáticas
- Implementação de funções com decorators
- Anotações de tipo para parâmetros
- Tratamento de erros e validação

**Funcionalidades Demonstradas**:
```python
@kernel_function(description="Calcula a média de uma lista de números")
def calculate_average(self, numbers: str) -> str:
    # Implementação de cálculo de média
    
@kernel_function(description="Encontra o maior número em uma lista")  
def find_maximum(self, numbers: str) -> str:
    # Implementação de busca do máximo
```

**Templates de Prompt**:
- Criação de funções semânticas
- Uso de argumentos dinâmicos com KernelArguments
- Templates personalizados para diferentes cenários

### Exercício 3 - Introdução ao AutoGen

**Conceitos Fundamentais**:
- **Agentes**: Entidades que enviam e recebem mensagens
- **Conversação**: Fluxo estruturado de mensagens entre agentes
- **Roles**: Papéis específicos (Assistant, User Proxy, etc.)
- **Especialização**: Agentes com expertise em domínios específicos

**Nova API AutoGen 0.6+**:
- Uso do `model_client` ao invés de `llm_config`
- Método `run()` assíncrono para execução
- `AzureOpenAIChatCompletionClient` para integração Azure
- Estrutura simplificada e mais limpa

**Exemplo de Configuração**:
```python
# Cliente Azure OpenAI
azure_model_client = AzureOpenAIChatCompletionClient(
    azure_deployment=deployment_name,
    model=deployment_name,
    api_version=api_version,
    azure_endpoint=azure_endpoint,
    api_key=api_key
)

# Agente assistente especializado
assistente_criativo = AssistantAgent(
    name="assistente_criativo",
    model_client=azure_model_client,
    system_message="Você é um assistente criativo especializado..."
)
```

### Quando Usar Cada Framework

**Semantic Kernel é ideal para**:
- Orchestração de AI com código tradicional
- Criação de plugins e funções reutilizáveis
- Aplicações que precisam de planejamento automático
- Integração com sistemas existentes
- Aplicações single-agent com funcionalidades complexas

**AutoGen é ideal para**:
- Sistemas multi-agente complexos
- Simulações de discussões e brainstorming
- Workflows que envolvem múltiplas perspectivas
- Automação de processos colaborativos
- Sistemas de tomada de decisão distribuída

### Sistema Prático - Análise de Produtos

**Combinação de Frameworks**:
O laboratório culmina com um sistema prático que combina ambos os frameworks:

1. **Semantic Kernel** para:
   - Plugin de análise de sentimentos
   - Processamento estruturado de feedbacks
   - Funções reutilizáveis de análise

2. **AutoGen** para:
   - Agente especialista em qualidade
   - Agente especialista em experiência do usuário
   - Análise colaborativa de múltiplas perspectivas

**Fluxo do Sistema**:
```
Feedbacks → Semantic Kernel (Análise Sentimento) → AutoGen (Especialistas) → Relatório Final
```

## Instruções de Execução

1. **Instalação de Dependências**:
   ```bash
   pip install semantic-kernel autogen-agentchat autogen-ext[openai,azure] python-dotenv
   ```

2. **Configuração**:
   - Configure as variáveis do Azure OpenAI no arquivo `.env`
   - Certifique-se de ter acesso ao Azure OpenAI Service

3. **Execução**:
   - Abra o notebook `lab4.ipynb` no Azure AI Foundry ou VS Code
   - Execute as células sequencialmente
   - Observe as diferenças entre as abordagens

4. **Experimentação**:
   - Modifique os agentes especializados
   - Crie novos plugins para o Semantic Kernel
   - Teste diferentes cenários de análise

## Estrutura do Laboratório

- **Configuração inicial** e imports
- **Semantic Kernel básico** com templates
- **Plugins personalizados** com funções matemáticas  
- **AutoGen configuração** com nova API
- **Agentes especializados** por domínio
- **Sistema integrado** combinando ambos frameworks
- **Comparações práticas** entre abordagens

## Resultados Esperados

Ao completar este laboratório, você será capaz de:
- Configurar e usar o Semantic Kernel efetivamente
- Criar plugins personalizados para funcionalidades específicas
- Implementar agentes AutoGen especializados
- Escolher o framework adequado para cada cenário
- Combinar frameworks para soluções híbridas
- Desenvolver sistemas de análise multi-perspectiva

## Recursos Adicionais

### Semantic Kernel:
- [Documentação Oficial](https://learn.microsoft.com/semantic-kernel/)
- [Repositório GitHub](https://github.com/microsoft/semantic-kernel)
- [Exemplos e Tutoriais](https://learn.microsoft.com/semantic-kernel/get-started/)
- [Plugins da Comunidade](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic_kernel/core_plugins)

### AutoGen:
- [Documentação Oficial](https://microsoft.github.io/autogen/)
- [Repositório GitHub](https://github.com/microsoft/autogen)
- [Galeria de Exemplos](https://microsoft.github.io/autogen/docs/Examples)
- [Notebooks de Tutorial](https://github.com/microsoft/autogen/tree/main/notebook)

### Azure AI Foundry:
- [Portal do Azure AI Foundry](https://ai.azure.com/)
- [Documentação do Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Modelos Disponíveis](https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview)
- [Melhores Práticas](https://learn.microsoft.com/azure/ai-services/openai/concepts/best-practices)

## Desafios para Prática

1. **Expansão do Sistema**: Adicione plugins para análise de imagens de produtos
2. **Agentes Especializados**: Crie agentes para diferentes setores (finanças, educação)
3. **Workflow Complexo**: Implemente sistema de aprovação multi-etapas
4. **Interface de Usuário**: Crie interface web para interagir com os agentes
5. **Integração de Dados**: Conecte com APIs externas para enriquecimento de dados
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