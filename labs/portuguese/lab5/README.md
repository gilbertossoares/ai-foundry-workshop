# Lab 5: RAG (Retrieval-Augmented Generation) Completo

## Visão Geral

Neste laboratório você implementará um sistema **RAG (Retrieval-Augmented Generation)** completo usando Azure AI Search e Azure OpenAI. O RAG é uma técnica poderosa que combina recuperação de informações com geração de texto, permitindo que modelos de linguagem acessem conhecimentos específicos externos ao seu treinamento, resultando em respostas mais precisas, atualizadas e com menor taxa de alucinações.

## Objetivos

- ✅ Entender o conceito e benefícios do RAG
- ✅ Implementar busca semântica com embeddings
- ✅ Configurar integração com Azure AI Search (simulada)
- ✅ Comparar respostas com e sem RAG
- ✅ Analisar a qualidade e precisão das respostas aumentadas
- ✅ Testar sistema RAG com diferentes tipos de consultas
- ✅ Compreender implementação real em produção

## Pré-requisitos

- Conhecimentos básicos de Python e conceitos de IA
- Conclusão dos Labs 1-4 (recomendado)
- Acesso ao Azure OpenAI Service (embeddings + chat completions)
- Opcionalmente: Azure AI Search configurado
- Variáveis de ambiente configuradas no arquivo `.env`

## Conteúdo do Laboratório

### Exercício 1 - Configuração e Importação

**Bibliotecas Principais**:
- `openai` - Azure OpenAI para chat completions e embeddings
- `azure.search.documents` - Azure AI Search client
- `numpy` - Cálculos de similaridade vetorial
- `dotenv` - Carregamento de variáveis de ambiente

**Configuração de Credenciais**:
```python
# Azure OpenAI
AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, API_VERSION
AZURE_OPENAI_DEPLOYMENT, AZURE_OPENAI_EMBEDDING_MODEL

# Azure AI Search  
AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_KEY, AZURE_SEARCH_INDEX
```

### Exercício 2 - Consulta Sem RAG (Baseline)

**Objetivo**: Estabelecer uma linha de base para comparação.

**Pergunta de Teste**: "Quais são as principais funcionalidades do Azure AI Foundry lançadas em 2024?"

**Limitações Observadas**:
- Conhecimento limitado sobre recursos específicos
- Informações potencialmente desatualizadas
- Respostas genéricas sem detalhes específicos
- Possíveis alucinações sobre funcionalidades

### Exercício 3 - Preparação de Dados

**Base de Conhecimento Simulada**:
Documentos de exemplo sobre Azure AI Foundry 2024:

1. **Visão Geral**: Plataforma unificada, ferramentas integradas, lançamento 2024
2. **Funcionalidades Principais**: Model Catalog (200+ modelos), Prompt Flow, RAG integrado
3. **Suporte RAG**: Integração nativa, Azure AI Search, ferramentas visuais  
4. **Azure AI Search**: Busca híbrida, múltiplos algoritmos, 300+ formatos

**Estrutura dos Documentos**:
```python
{
    "id": "1",
    "title": "Azure AI Foundry - Visão Geral", 
    "content": "Conteúdo detalhado..."
}
```

### Exercício 4 - Geração de Embeddings

**Processo de Embeddings**:
- Geração usando Azure OpenAI Embeddings API
- Combinação de título + conteúdo para contexto completo
- Armazenamento de vetores para busca semântica
- Dimensionalidade: 1536 (modelo text-embedding-ada-002)

**Exemplo de Implementação**:
```python
def get_embedding(text):
    response = openai_client.embeddings.create(
        input=text,
        model=embedding_model
    )
    return response.data[0].embedding
```

### Exercício 5 - Busca Semântica (Simulada)

**Implementação de Similaridade**:
- Cálculo de similaridade coseno entre vetores
- Ranking dos documentos mais relevantes
- Seleção dos top-k resultados mais similares

**Algoritmo de Busca**:
```python
def semantic_search(query, documents, top_k=2):
    query_embedding = get_embedding(query)
    similarities = []
    for doc in documents:
        similarity = cosine_similarity(query_embedding, doc['embedding'])
        similarities.append({'document': doc, 'similarity': similarity})
    return sorted(similarities, key=lambda x: x['similarity'], reverse=True)[:top_k]
```

### Exercício 6 - Implementação RAG Completa

**Pipeline RAG**:
1. **Retrieval**: Busca documentos relevantes usando embeddings
2. **Context Building**: Construção do contexto com documentos recuperados
3. **Prompt Engineering**: Criação de prompt com contexto + pergunta
4. **Augmented Generation**: Geração de resposta informada pelo contexto

**Sistema de Prompt**:
```python
system_message = """Você é um assistente especializado em Azure. 
Use APENAS as informações fornecidas no contexto para responder. 
Se a informação não estiver no contexto, indique claramente."""
```

**Controle de Qualidade**:
- Temperature baixa (0.2-0.3) para maior precisão
- Instrução para citar fontes quando possível
- Tratamento de casos onde informação não está disponível

### Exercício 7 - Comparação de Resultados

**Métricas de Comparação**:
- **Precisão**: Informações corretas e específicas
- **Completude**: Cobertura dos aspectos da pergunta
- **Atualidade**: Informações recentes e relevantes
- **Rastreabilidade**: Capacidade de identificar fontes
- **Redução de Alucinações**: Respostas baseadas em fatos

**Benefícios Demonstrados**:
- ✅ Informações mais específicas e atualizadas
- ✅ Respostas baseadas em fontes confiáveis  
- ✅ Maior precisão em detalhes técnicos
- ✅ Rastreabilidade das informações (sources)
- ✅ Redução significativa de alucinações

### Exercício 8 - RAG com Azure AI Search (Implementação Real)

**Código para Produção**:
```python
def query_with_azure_ai_search(question, search_client, openai_client):
    # Busca vetorizada no Azure AI Search
    vector_query = VectorizedQuery(
        vector=get_embedding(question),
        k_nearest_neighbors=3,
        fields="content_vector"
    )
    
    # Busca híbrida (texto + vetorial)
    search_results = search_client.search(
        search_text=question,
        vector_queries=[vector_query],
        top=3
    )
    
    # Geração com contexto
    return generate_response_with_context(question, search_results)
```

**Requisitos para Produção**:
- Índice configurado no Azure AI Search
- Campos de embedding configurados
- Documentos indexados com vetores
- Configuração de busca híbrida

### Exercício 9 - Teste Interativo

**Perguntas de Teste Incluídas**:
- "Como o Azure AI Foundry suporta RAG?"
- "Quantos modelos estão disponíveis no Model Catalog?"
- "Quais são os tipos de busca suportados pelo Azure AI Search?"
- "O que é o Prompt Flow no Azure AI Foundry?"

**Funcionalidades de Teste**:
- Comparação lado a lado (com vs sem RAG)
- Exibição de fontes utilizadas
- Análise de qualidade das respostas
- Interface para testes personalizados

## Instruções de Execução

1. **Configuração de Ambiente**:
   ```bash
   # Variáveis necessárias no .env
   AZURE_OPENAI_ENDPOINT=https://your-openai.openai.azure.com/
   AZURE_OPENAI_API_KEY=your-key
   AZURE_OPENAI_DEPLOYMENT=your-chat-model
   AZURE_OPENAI_EMBEDDING_MODEL=text-embedding-ada-002
   
   # Opcionais para Azure AI Search real
   AZURE_SEARCH_ENDPOINT=https://your-search.search.windows.net
   AZURE_SEARCH_KEY=your-search-key
   AZURE_SEARCH_INDEX=your-index-name
   ```

2. **Execução**:
   - Abra o notebook `lab5.ipynb` no Azure AI Foundry ou VS Code
   - Execute as células sequencialmente
   - Observe as diferenças entre respostas com e sem RAG

3. **Experimentação**:
   - Teste com suas próprias perguntas
   - Modifique os documentos da base de conhecimento
   - Experimente diferentes parâmetros de busca

## Resultados Esperados

Ao completar este laboratório, você compreenderá:
- Como implementar RAG do zero com Azure OpenAI
- A diferença fundamental entre respostas com e sem RAG
- Como funciona a busca semântica com embeddings
- Configuração necessária para Azure AI Search em produção
- Melhores práticas para sistemas RAG robustos

## Para Implementação em Produção

### Considerações Técnicas:
1. **Chunking**: Dividir documentos grandes (512-1024 tokens)
2. **Busca Híbrida**: Combinar keyword + semântica
3. **Re-ranking**: Melhorar relevância dos resultados
4. **Cache**: Implementar cache para consultas frequentes
5. **Monitoramento**: Métricas de performance e qualidade
6. **Governança**: Validação e auditoria de fontes

### Arquitetura Recomendada:
```
Usuário → API Gateway → RAG Service → Azure AI Search + Azure OpenAI → Resposta Aumentada
```

## Recursos Adicionais

### Documentação Oficial:
- [Azure AI Search Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview)
- [Azure OpenAI RAG Patterns](https://learn.microsoft.com/azure/ai-services/openai/concepts/use-your-data)
- [Azure AI Foundry RAG](https://learn.microsoft.com/azure/ai-foundry/)

### Melhores Práticas:
- [RAG Best Practices](https://learn.microsoft.com/azure/ai-services/openai/concepts/advanced-usage)
- [Chunking Strategies](https://learn.microsoft.com/azure/search/vector-search-how-to-chunk-documents)
- [Hybrid Search](https://learn.microsoft.com/azure/search/hybrid-search-overview)

### Próximos Passos:
- Implementar RAG em aplicação real
- Explorar técnicas avançadas de chunking
- Integrar com Azure AI Foundry Prompt Flow
- Desenvolver métricas de avaliação personalizadas