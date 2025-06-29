# Laboratório 5: Implementação de RAG (Retrieval Augmented Generation) com Azure OpenAI e Azure AI Search

Neste laboratório, você aprenderá como implementar um sistema de RAG (Retrieval Augmented Generation) utilizando o Azure OpenAI e o Azure AI Search. Este padrão arquitetural é fundamental para melhorar as respostas de modelos de linguagem com informações específicas de uma base de conhecimento própria.

## Objetivos

- Entender o conceito de RAG e suas aplicações
- Configurar um serviço Azure OpenAI
- Configurar um serviço Azure AI Search
- Criar e carregar documentos para um índice de pesquisa
- Implementar um fluxo de RAG completo em um notebook Python
- Testar consultas que combinam a geração do modelo com a recuperação de documentos relevantes

## Pré-requisitos

- Uma assinatura do Azure com acesso aos serviços Azure OpenAI e Azure AI Search
- Python 3.8 ou superior
- Visual Studio Code ou outro ambiente de desenvolvimento
- Conhecimentos básicos de Python e APIs REST

## Arquitetura de Referência

RAG é um padrão que combina a recuperação de informações de uma base de conhecimento com a geração de texto por um modelo de linguagem. A arquitetura básica inclui:

1. **Base de Conhecimento**: Documentos indexados no Azure AI Search
2. **Serviço de Recuperação**: Azure AI Search para encontrar documentos relevantes
3. **Modelo de Linguagem**: Azure OpenAI para gerar respostas informadas pelos documentos recuperados

## Guia do Laboratório

### 1. Configuração dos Serviços Azure

#### Azure OpenAI
- Provisione um serviço Azure OpenAI
- Implemente o modelo GPT-4 ou GPT-3.5 Turbo
- Obtenha as credenciais de acesso (endpoint e chave)

#### Azure AI Search
- Crie um serviço Azure AI Search
- Configure um índice de pesquisa
- Obtenha as credenciais de acesso (endpoint e chave)

### 2. Preparação dos Dados

- Prepare os documentos que servirão como base de conhecimento
- Processe e indexe os documentos no Azure AI Search
- Verifique se a indexação foi concluída com sucesso

### 3. Implementação do RAG

Abra o notebook `rag_example.ipynb` para seguir um exemplo prático de:

- Conexão com os serviços Azure OpenAI e Azure AI Search
- Formulação de consultas de pesquisa
- Recuperação de documentos relevantes
- Construção de prompts enriquecidos com o contexto recuperado
- Geração de respostas usando o Azure OpenAI
- Avaliação e refinamento dos resultados

### 4. Experimentação e Testes

- Experimente com diferentes consultas
- Ajuste os parâmetros de pesquisa e geração
- Compare respostas com e sem o componente de recuperação

## Recursos Adicionais

- [Documentação do Azure OpenAI](https://learn.microsoft.com/azure/cognitive-services/openai/)
- [Documentação do Azure AI Search](https://learn.microsoft.com/azure/search/)
- [Padrões de RAG](https://learn.microsoft.com/azure/architecture/pattern/ai/retrieval-augmented-generation-pattern)
- [Melhores práticas para implementações de RAG](https://learn.microsoft.com/azure/ai-services/openai/concepts/retrieval-augmented-generation)

## Próximos Passos

Após completar este laboratório, considere:
- Adicionar técnicas de filtragem semântica
- Implementar reranking de resultados
- Desenvolver um aplicativo web que utilize este padrão RAG
- Explorar técnicas avançadas como chunking e embedding de documentos

---

*Este laboratório faz parte da série de workshops de IA da Microsoft.*