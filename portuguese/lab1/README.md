# Lab 1: Conexão e Primeiros Passos com Azure OpenAI

## Visão Geral

Neste laboratório você irá realizar os primeiros passos com o Azure OpenAI Service, desde a configuração inicial até a execução de tarefas práticas incluindo chamadas à API, análise de respostas, geração de embeddings, processamento de imagens e exploração de outros modelos disponíveis no Azure AI Foundry.

## Objetivos

- Configurar e conectar com o Azure OpenAI Service
- Realizar chamadas básicas e avançadas à API de chat completions
- Analisar detalhadamente as respostas da API
- Gerar e trabalhar com embeddings de texto
- Processar imagens usando modelos multimodais
- Explorar outros modelos LLM disponíveis no Azure AI Foundry

## Pré-requisitos

- Conta Azure com acesso ao Azure OpenAI Service
- Variáveis de ambiente configuradas no arquivo `.env`
- Conhecimentos básicos de Python
- Acesso ao Azure AI Foundry

## Conteúdo do Laboratório

### Exercício 1 - Chamada à API

Aprenda a configurar o cliente Azure OpenAI e realizar sua primeira chamada à API, incluindo:
- Configuração de credenciais e endpoints
- Estruturação de mensagens com diferentes roles (system, user, assistant)
- Execução de chamadas de chat completion

### Exercício 2 - Analisando a Resposta

Explore em detalhes a estrutura completa da resposta da API, incluindo:
- Análise de metadados da resposta
- Informações sobre uso de tokens
- Detalhes sobre filtragem de conteúdo
- Contadores de tokens de prompt e completion
- Detalhes sobre tokens de raciocínio para modelos avançados

Experimente com parâmetros importantes como:
- **max_completion_tokens**: Controle do tamanho da resposta
- **temperature**: Ajuste da criatividade (0.0 = determinístico, 1.0 = criativo)
- **top_p**: Controle de diversidade via nucleus sampling
- **frequency_penalty**: Penalização por repetição baseada em frequência
- **presence_penalty**: Penalização por repetição independente da frequência

### Exercício 3 - Embeddings

Descubra como trabalhar com embeddings para análise semântica:
- Geração de embeddings a partir de texto
- Compreensão das representações numéricas do significado
- Casos de uso para busca semântica, classificação e análise de similaridade

Explore as opções de armazenamento de embeddings no Azure:
- Azure AI Search
- Azure Cosmos DB (MongoDB vCore, NoSQL, PostgreSQL)
- Azure SQL Database
- Azure Cache for Redis
- Azure Database for PostgreSQL
- Microsoft Fabric Eventhouse

### Exercício 4 - Processamento de Imagens

Aprenda a trabalhar com modelos multimodais:
- Envio de imagens via URL
- Codificação de imagens locais em base64
- Combinação de texto e imagens em prompts
- Descrição e análise de imagens usando IA

### Exercício 5 - Outros Modelos no Azure AI Foundry

Explore a diversidade de modelos disponíveis através do Model Catalog:
- Modelos da Microsoft (OpenAI, Meta, Mistral AI, Deepseek, xAI, Black Forest Labs)
- Modelos de parceiros (Nixtla, AI21, NTT Data, Core42, NVIDIA NIM, Stability AI)
- Configuração e uso de diferentes bibliotecas de cliente
- Exemplo prático com modelo Phi-4

### Funcionalidades Avançadas Disponíveis

O laboratório também apresenta outras funcionalidades do Azure OpenAI:
- Responses API
- Reasoning Models
- Computer Use
- Model Router
- Function Calling
- Predicted Outputs
- Prompt Caching
- Structured Outputs
- JSON Mode
- Reproducible Output

## Instruções

1. Configure as variáveis de ambiente no arquivo `.env` na raiz do repositório
2. Abra o notebook `lab1.ipynb` no Azure AI Foundry
3. Execute as células sequencialmente, observando os exemplos e resultados
4. Experimente modificar parâmetros para entender seu impacto
5. Teste com seus próprios prompts e imagens

## Recursos Adicionais

- [Documentação do Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/)
- [Como trabalhar com embeddings](https://learn.microsoft.com/azure/ai-services/openai/how-to/embeddings)
- [Azure AI Foundry Model Catalog](https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview)
- [Chat Completions API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt)
- [Function Calling](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling)
- [Structured Outputs](https://learn.microsoft.com/azure/ai-services/openai/how-to/structured-outputs)

## Próximos Passos

Após concluir este laboratório, você estará preparado para avançar para o Lab 2, onde explorará conceitos mais avançados de implementação e casos de uso específicos com Azure OpenAI.