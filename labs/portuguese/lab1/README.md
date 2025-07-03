# Lab 1: Conexão e Primeiros Passos com Azure OpenAI

## Visão Geral

Neste laboratório você irá realizar os primeiros passos com o Azure OpenAI Service, aprendendo desde a configuração inicial até a execução de tarefas práticas avançadas. O lab abrange chamadas à API, análise detalhada de respostas, geração de embeddings, processamento de imagens com modelos multimodais e exploração de outros modelos LLM disponíveis no Azure AI Foundry.

## Objetivos

- ✅ Configurar e conectar com o Azure OpenAI Service
- ✅ Realizar chamadas básicas e avançadas à API de chat completions
- ✅ Analisar detalhadamente as respostas da API e metadados
- ✅ Gerar e trabalhar com embeddings de texto para análise semântica
- ✅ Processar imagens usando modelos multimodais (visão computacional)
- ✅ Explorar outros modelos LLM disponíveis no Azure AI Foundry
- ✅ Realizar atividades práticas para consolidar o aprendizado

## Pré-requisitos

- Conta Azure com acesso ao Azure OpenAI Service
- Variáveis de ambiente configuradas no arquivo `.env` na raiz do projeto
- Conhecimentos básicos de Python
- Acesso ao Azure AI Foundry

## Conteúdo do Laboratório

### Exercício 1 - Chamada à API

Configure o cliente Azure OpenAI e realize sua primeira chamada à API:
- Importação das bibliotecas necessárias (openai, dotenv)
- Carregamento das credenciais do arquivo `.env`
- Inicialização do cliente Azure OpenAI
- Estruturação de mensagens com diferentes roles (system, user, assistant)
- Execução de chamadas de chat completion com contexto

### Exercício 2 - Analisando a Resposta

Explore em detalhes a estrutura completa da resposta da API:
- Análise de metadados (ID, modelo, timestamp)
- Informações detalhadas sobre uso de tokens
- Filtragem de conteúdo e avaliações de segurança
- Contadores de tokens de prompt e completion
- Detalhes sobre tokens de raciocínio para modelos avançados
- Formatação estruturada da resposta em JSON

Experimente com parâmetros importantes:
- **max_completion_tokens**: Controle do tamanho da resposta
- **temperature**: Ajuste da criatividade (0.0 = determinístico, 1.0 = criativo)
- **top_p**: Controle de diversidade via nucleus sampling
- **frequency_penalty**: Penalização por repetição baseada em frequência
- **presence_penalty**: Penalização por repetição independente da frequência

### Exercício 3 - Embeddings

Aprenda a trabalhar com embeddings para análise semântica:
- Geração de embeddings a partir de texto usando Azure OpenAI
- Compreensão das representações vetoriais do significado semântico
- Casos de uso para busca semântica, classificação e análise de similaridade
- Comparação de similaridade entre palavras relacionadas

Explore as opções de armazenamento de embeddings no Azure:
- Azure AI Search (busca vetorial)
- Azure Cosmos DB (MongoDB vCore, NoSQL, PostgreSQL)
- Azure SQL Database (vector search)
- Azure Cache for Redis (vector similarity)
- Azure Database for PostgreSQL (pgvector)
- Microsoft Fabric Eventhouse (vector database)

### Exercício 4 - Processamento de Imagens

Aprenda a trabalhar com modelos multimodais para visão computacional:
- Envio de imagens via URL pública
- Codificação de imagens locais em base64
- Combinação de texto e imagens em prompts multimodais
- Descrição automática e análise detalhada de imagens
- Processamento de diferentes tipos de conteúdo visual

### Exercício 5 - Outros Modelos no Azure AI Foundry

Explore a diversidade de modelos disponíveis através do Model Catalog:
- **Modelos Microsoft**: OpenAI, Meta, Mistral AI, Deepseek, xAI, Black Forest Labs
- **Modelos de Parceiros**: Nixtla, AI21, NTT Data, Core42, NVIDIA NIM, Stability AI
- Configuração de diferentes bibliotecas de cliente (azure-ai-inference)
- Exemplo prático com modelo Phi-4
- Diferentes modos de disponibilização e implantação

### 🎯 Atividades Práticas Incluídas

O laboratório inclui 5 atividades práticas para consolidar o aprendizado:

1. **Teste de Temperatura**: Experimente como diferentes valores de temperature afetam a criatividade
2. **Comparação de Embeddings**: Analise similaridade entre palavras relacionadas
3. **Análise de Imagem com Diferentes Prompts**: Teste vários tipos de perguntas para a mesma imagem
4. **Contador de Tokens**: Entenda como o tamanho do prompt afeta o consumo
5. **Teste de Personas**: Explore como system messages diferentes criam personalidades distintas

### Funcionalidades Avançadas Apresentadas

O laboratório apresenta outras funcionalidades avançadas do Azure OpenAI:
- **Responses API**: Múltiplas alternativas de resposta
- **Reasoning Models**: Modelos com capacidade de raciocínio (o1)
- **Computer Use**: Interação com interfaces de usuário
- **Model Router**: Roteamento inteligente entre modelos
- **Function Calling**: Chamada de funções externas
- **Predicted Outputs**: Otimização de completions
- **Prompt Caching**: Cache de prompts para eficiência
- **Structured Outputs**: Saídas em formato estruturado
- **Vision-enabled Chats**: Conversas com suporte a imagens
- **JSON Mode**: Respostas estruturadas em JSON
- **Reproducible Output**: Resultados consistentes

## Instruções de Execução

1. **Configuração Inicial**:
   - Configure as variáveis de ambiente no arquivo `.env` na raiz do repositório
   - Certifique-se de ter acesso ao Azure OpenAI Service

2. **Execução**:
   - Abra o notebook `lab1.ipynb` no Azure AI Foundry ou VS Code
   - Execute as células sequencialmente, observando os exemplos e resultados
   - Experimente modificar parâmetros para entender seu impacto

3. **Experimentação**:
   - Teste com seus próprios prompts personalizados
   - Experimente com diferentes imagens (URLs ou locais)
   - Modifique os parâmetros das atividades práticas

## Resultados Esperados

Ao completar este laboratório, você será capaz de:
- Conectar e usar o Azure OpenAI Service efetivamente
- Analisar e interpretar respostas detalhadas da API
- Gerar e comparar embeddings para análise semântica
- Processar imagens com modelos multimodais
- Escolher e configurar diferentes modelos do Azure AI Foundry
- Aplicar técnicas de prompt engineering básicas

## Recursos Adicionais

- [Documentação do Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/)
- [Como trabalhar com embeddings](https://learn.microsoft.com/azure/ai-services/openai/how-to/embeddings)
- [Azure AI Foundry Model Catalog](https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview)
- [Chat Completions API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt)
- [Function Calling](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling)
- [Structured Outputs](https://learn.microsoft.com/azure/ai-services/openai/how-to/structured-outputs)
- [Vision-enabled Chats](https://learn.microsoft.com/azure/ai-services/openai/how-to/gpt-with-vision)

## Próximos Passos

Após concluir este laboratório, você estará preparado para avançar para o Lab 2, onde explorará conceitos mais avançados de implementação e casos de uso específicos com Azure OpenAI.