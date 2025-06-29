# Workshop Azure AI Foundry

Este repositório contém uma série de laboratórios práticos projetados para explorar e aprender sobre os serviços de IA do Azure, com foco no Azure AI Foundry e tecnologias relacionadas.

## Visão Geral do Workshop

Este workshop abrangente oferece uma jornada completa através das capacidades mais recentes do Azure AI Foundry, desde conceitos fundamentais até implementações avançadas de IA. Cada laboratório foi cuidadosamente projetado para construir conhecimento progressivamente, permitindo que você domine as ferramentas e técnicas essenciais para desenvolvimento de IA.

## Estrutura dos Laboratórios

### [Lab 1: Conexão e Primeiros Passos com Azure OpenAI](lab1/)
**Fundamentos e Configuração Inicial**

- Configuração e conexão com Azure OpenAI Service
- Primeiras chamadas à API e análise detalhada de respostas
- Geração e utilização de embeddings para análise semântica
- Processamento de imagens com modelos multimodais
- Exploração de outros modelos LLM disponíveis no Azure AI Foundry
- Funcionalidades avançadas: Responses API, Reasoning Models, Function Calling

**Principais Recursos Abordados:**
- Configuração de credenciais e endpoints
- Parâmetros importantes (temperature, top_p, frequency_penalty)
- Análise de metadados e uso de tokens
- Embeddings e suas aplicações práticas
- Modelos multimodais para processamento de imagem

### [Lab 2: Explorando Serviços de IA do Azure Foundry](lab2/)
**Ecossistema Completo de Serviços de IA**

- **Azure AI Speech**: Reconhecimento de fala, síntese de voz e tradução de áudio
- **Azure AI Language + Translator**: Análise de texto, NER, análise de sentimento, tradução
- **Azure AI Vision + Document**: OCR, análise de imagem, processamento de documentos
- **Azure AI Content Safety**: Detecção e filtragem de conteúdo prejudicial

**Casos de Uso Implementados:**
- Transcrição de áudio e geração de legendas
- Análise semântica de textos e documentos
- Processamento de documentos comerciais e faturas
- Sistemas de moderação de conteúdo

### [Lab 3: Prompt Engineering](lab3/)
**Técnicas Avançadas de Engenharia de Prompts**

- **Zero-Shot Prompting**: Criação de prompts eficazes sem exemplos
- **Few-Shot Prompting**: Melhoria da qualidade com exemplos direcionados
- **Chain-of-Thought Prompting**: Incentivando raciocínio passo a passo
- **Meta Prompting**: Instruções sobre como abordar diferentes tarefas
- **Prompt Chaining**: Divisão de tarefas complexas em sequências focadas
- **Tree of Thoughts (ToT)**: Consideração de múltiplas linhas de raciocínio
- **Retrieval Augmented Generation (RAG)**: Combinação de informações externas
- **Active-Prompt**: Prompts que se adaptam dinamicamente

**Melhores Práticas:**
- Especificidade e clareza nas instruções
- Uso efetivo de analogias e exemplos
- Importância da ordem e estrutura
- Estratégias de fallback e alternativas

### [Lab 4: Frameworks de LLM - Semantic Kernel, AutoGen e LangChain](lab4/)
**Desenvolvimento com Frameworks Especializados**

- **Semantic Kernel**: Framework da Microsoft para integração modular de LLMs
- **AutoGen**: Criação de agentes conversacionais e fluxos multiagente
- **LangChain**: Componentes para aplicações baseadas em LLMs

**Comparação de Frameworks:**
- Pontos fortes e casos de uso ideais para cada framework
- Exemplos práticos de implementação
- Integração com ecossistemas existentes
- Considerações de arquitetura e deployment

**Exercícios Práticos:**
- Implementação de agentes especializados
- Criação de fluxos de processamento complexos
- Integração com APIs e serviços externos

### [Lab 5: Implementação de RAG com Azure OpenAI e Azure AI Search](lab5/)
**Padrões Avançados de Recuperação e Geração**

- Conceitos fundamentais de RAG (Retrieval Augmented Generation)
- Configuração de Azure OpenAI e Azure AI Search
- Criação e indexação de bases de conhecimento
- Implementação de fluxos completos de RAG
- Estratégias de otimização e refinamento

**Arquitetura Implementada:**
- Base de conhecimento indexada no Azure AI Search
- Serviços de recuperação para documentos relevantes
- Modelos de linguagem para geração informada
- Avaliação e métricas de qualidade

**Técnicas Avançadas:**
- Chunking e embedding de documentos
- Filtragem semântica
- Reranking de resultados
- Estratégias de cache e performance

## Pré-requisitos

### Obrigatórios
- Assinatura do Azure com acesso aos serviços de IA
- Python 3.8 ou superior
- Conhecimentos básicos de programação e APIs
- Acesso ao Azure AI Foundry

### Recomendados
- Visual Studio Code com extensões do Azure e Python
- Azure CLI para interações via linha de comando
- Git para controle de versão
- Conhecimentos básicos de machine learning

## Configuração Inicial

### 1. Preparação do Ambiente Azure
```bash
# Login no Azure
az login

# Definir sua assinatura
az account set --subscription "seu-id-de-assinatura"

# Criar grupo de recursos para o workshop
az group create --name "ai-foundry-workshop-rg" --location "eastus"
```

### 2. Configuração Local
1. Clone este repositório
2. Configure seu arquivo `.env` com as credenciais do Azure
3. Instale as dependências necessárias para cada laboratório
4. Verifique o acesso ao Azure AI Foundry

### 3. Variáveis de Ambiente Necessárias
```
# Azure OpenAI
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_API_VERSION=

# Azure AI Services
SPEECH_ENDPOINT=
SPEECH_KEY=
SPEECH_REGION=

LANGUAGE_ENDPOINT=
LANGUAGE_KEY=

VISION_ENDPOINT=
VISION_KEY=

CONTENT_SAFETY_ENDPOINT=
CONTENT_SAFETY_KEY=

# Azure AI Search (Lab 5)
SEARCH_ENDPOINT=
SEARCH_KEY=
```

## Progressão Recomendada

1. **Iniciantes**: Comece pelo Lab 1 para entender os fundamentos
2. **Intermediário**: Labs 1-3 fornecem uma base sólida em IA generativa
3. **Avançado**: Labs 4-5 abordam arquiteturas e padrões complexos
4. **Especialização**: Escolha laboratórios específicos baseados em suas necessidades

## Resultados de Aprendizado

Ao concluir este workshop, você será capaz de:

✅ **Dominar Azure AI Foundry**: Navegar e utilizar a plataforma efetivamente
✅ **Desenvolver Soluções de IA**: Construir aplicações completas end-to-end
✅ **Aplicar Prompt Engineering**: Otimizar interações com modelos de linguagem
✅ **Implementar Padrões RAG**: Combinar recuperação e geração para respostas precisas
✅ **Usar Frameworks Especializados**: Escolher e implementar as ferramentas certas
✅ **Integrar Múltiplos Serviços**: Combinar diferentes serviços de IA do Azure
✅ **Seguir Melhores Práticas**: Implementar segurança e governança adequadas

## Recursos Adicionais

### Documentação Oficial
- [Azure AI Foundry](https://learn.microsoft.com/pt-br/azure/ai-foundry/)
- [Azure OpenAI Service](https://learn.microsoft.com/pt-br/azure/ai-services/openai/)
- [Azure AI Services](https://learn.microsoft.com/pt-br/azure/ai-services/)
- [Azure AI Search](https://learn.microsoft.com/pt-br/azure/search/)

### Tutoriais e Guias
- [Engenharia de Prompts](https://learn.microsoft.com/pt-br/azure/ai-services/openai/concepts/prompt-engineering)
- [Padrões de RAG](https://learn.microsoft.com/pt-br/azure/architecture/pattern/ai/retrieval-augmented-generation-pattern)
- [IA Responsável](https://www.microsoft.com/pt-br/ai/responsible-ai)

### Comunidade e Suporte
- [Microsoft Learn - Cursos de IA](https://learn.microsoft.com/pt-br/training/browse/?products=azure-cognitive-services)
- [Azure AI Community](https://techcommunity.microsoft.com/category/azure-ai)
- [Stack Overflow - Azure AI](https://stackoverflow.com/questions/tagged/azure-ai)

## Solução de Problemas

### Problemas Comuns
- **Erros de acesso negado**: Verifique permissões da assinatura Azure e acesso ao AI Foundry
- **Limites de cota**: Verifique cotas do Azure para serviços de IA em sua região
- **Conectividade de rede**: Assegure configuração adequada de firewall e rede

### Obtendo Ajuda
- Consulte o guia de solução de problemas em cada laboratório
- Revise a documentação do Azure AI Foundry
- Abra uma issue neste repositório para problemas específicos do workshop

## Próximos Passos

Após concluir este workshop, considere:

- **Certificações Azure AI**: Explore as certificações AI-102 e AI-900
- **Projetos Práticos**: Implemente soluções de IA em cenários reais
- **Comunidade**: Junte-se às comunidades de desenvolvedores de IA
- **Aprendizado Contínuo**: Mantenha-se atualizado com as novidades do Azure AI

---

*Este workshop foi projetado para fornecer experiência prática com as mais recentes tecnologias de IA do Azure. Cada laboratório constrói sobre o anterior, criando uma jornada de aprendizado abrangente e estruturada.*

**Pronto para começar?** Inicie pelo [Lab 1](lab1/) e comece sua jornada no Azure AI Foundry!
