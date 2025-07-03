# Workshop Azure AI Foundry - Português

Este workshop oferece uma jornada completa através das capacidades mais recentes do **Azure AI Foundry**, desde conceitos fundamentais até implementações avançadas de IA generativa. Cada laboratório foi cuidadosamente projetado para construir conhecimento progressivamente, permitindo que você domine as ferramentas e técnicas essenciais para desenvolvimento de aplicações inteligentes.

## 🎯 Objetivos do Workshop

- **Dominar o Azure AI Foundry**: Configuração, uso e melhores práticas
- **Aplicar Prompt Engineering**: Técnicas avançadas para otimizar interações com LLMs
- **Implementar RAG**: Sistemas de recuperação e geração aumentada
- **Usar Frameworks Avançados**: Semantic Kernel e AutoGen para aplicações complexas
- **Integrar Serviços de IA**: Speech, Vision, Language e Content Safety
- **Desenvolver Soluções Práticas**: Projetos reais com casos de uso empresariais

## 📚 Estrutura dos Laboratórios

### [🚀 Lab 1: Conexão e Primeiros Passos com Azure OpenAI](lab1/)
**Fundamentos e Configuração Inicial**

Estabeleça a base sólida para trabalhar com Azure OpenAI, desde configuração até uso avançado de modelos multimodais.

**O que você aprenderá:**
- ✅ Configuração completa do Azure OpenAI Service
- ✅ Chamadas à API com análise detalhada de respostas
- ✅ Geração e análise de embeddings para busca semântica
- ✅ Processamento de imagens com modelos multimodais (GPT-4V)
- ✅ Exploração do Model Catalog com 200+ modelos
- ✅ 5 atividades práticas interativas para consolidar aprendizado

**Funcionalidades Avançadas Incluídas:**
- Responses API, Reasoning Models, Function Calling
- Structured Outputs, JSON Mode, Prompt Caching
- Computer Use, Model Router, Predicted Outputs

### [🧠 Lab 2: Explorando Serviços de IA do Azure Foundry](lab2/)
**Ecossistema Completo de Serviços Multimodais**

Domine os quatro pilares dos serviços de IA do Azure para criar aplicações completas e robustas.

**Serviços Cobertos:**

**🎤 Azure AI Speech**
- Reconhecimento de fala contínuo em português
- Síntese de voz natural e personalizada
- Tradução de áudio em tempo real
- Casos de uso: call centers, acessibilidade, assistentes

**💬 Azure AI Language + Translator**
- Análise de sentimentos com scores de confiança
- Extração de entidades e frases-chave
- Detecção de PII/PHI para conformidade
- Sumarização automática e tradução

**👁️ Azure AI Vision + Document Intelligence**
- OCR avançado para 300+ formatos de arquivo
- Análise de imagens com detecção de objetos
- Processamento de documentos comerciais
- Extração de dados estruturados

**🛡️ Azure AI Content Safety**
- Moderação de conteúdo em texto e imagem
- Detecção de ódio, violência, conteúdo sexual
- Escudos contra prompt injection
- Conformidade e governança

### [🎨 Lab 3: Prompt Engineering - Técnicas Avançadas](lab3/)
**Masterclass em Otimização de Prompts**

Domine 8 técnicas avançadas de prompt engineering para maximizar a eficácia dos modelos de linguagem.

**Técnicas Implementadas:**

| Técnica | Quando Usar | Benefícios |
|---------|-------------|------------|
| **Zero-Shot** | Tarefas simples, testes iniciais | Simplicidade, rapidez |
| **Few-Shot** | Tarefas estruturadas | Consistência, formato específico |
| **Chain-of-Thought** | Problemas complexos | Raciocínio verificável |
| **Meta Prompting** | Otimização de prompts | Melhoria automática |
| **Prompt Chaining** | Workflows complexos | Controle granular |
| **Tree of Thoughts** | Múltiplas soluções | Exploração de alternativas |
| **RAG** | Conhecimento específico | Informações atualizadas |
| **Active-Prompt** | Sistemas adaptativos | Otimização dinâmica |

**Resultados Esperados:**
- 📈 Melhoria de 40-60% na precisão das respostas
- 🎯 Redução significativa de alucinações
- 💰 Otimização de custos através de prompts eficientes
- 🔧 Toolkit completo para diferentes cenários

### [🤖 Lab 4: Frameworks Avançados - Semantic Kernel e AutoGen](lab4/)
**Desenvolvimento com Frameworks Especializados**

Explore frameworks poderosos para criar aplicações inteligentes escaláveis e robustas.

**🧮 Semantic Kernel**
- SDK open-source da Microsoft para integração modular
- Plugins personalizados e reutilizáveis
- Templates de prompts dinâmicos
- Integração com sistemas existentes

**🎭 AutoGen (v0.6+)**
- Framework multi-agente para colaboração
- Agentes especializados por domínio
- Conversação estruturada entre agentes
- Nova API simplificada com `model_client`

**Projeto Prático - Sistema de Análise de Produtos:**
```
Feedbacks → Semantic Kernel (Análise) → AutoGen (Especialistas) → Relatório
```

**Quando Usar Cada Framework:**
- **Semantic Kernel**: Single-agent, plugins, integração sistemas
- **AutoGen**: Multi-agente, brainstorming, decisões colaborativas

### [🔍 Lab 5: RAG (Retrieval-Augmented Generation) Completo](lab5/)
**Sistema de Recuperação e Geração Aumentada**

Implemente um sistema RAG completo que combina busca semântica com geração de texto para respostas precisas e atualizadas.

**Pipeline RAG Completo:**
1. **Preparação**: Documentos → Embeddings → Índice vetorial
2. **Retrieval**: Pergunta → Busca semântica → Documentos relevantes
3. **Augmentation**: Contexto + Pergunta → Prompt enriquecido
4. **Generation**: LLM → Resposta fundamentada → Fontes citadas

**Comparação Demonstrada:**
- ❌ **Sem RAG**: Respostas genéricas, possíveis alucinações
- ✅ **Com RAG**: Respostas específicas, fontes verificáveis, precisão alta

**Implementação Incluída:**
- Busca semântica com similaridade coseno
- Integração com Azure AI Search (código real)
- Sistema de avaliação de qualidade
- Testes interativos personalizáveis

**Para Produção:**
- Estratégias de chunking (512-1024 tokens)
- Busca híbrida (keyword + semântica)
- Re-ranking e cache de resultados
- Métricas de monitoramento e governança

## 🛠️ Configuração e Pré-requisitos

### **Obrigatórios:**
- Assinatura do Azure com acesso aos serviços de IA
- Python 3.8 ou superior
- Conhecimentos básicos de programação e APIs REST
- Acesso ao Azure AI Foundry ([ai.azure.com](https://ai.azure.com/))

### **Recomendados:**
- Visual Studio Code com extensões do Azure e Python
- Azure CLI para interações via linha de comando
- Git para controle de versão
- Conhecimentos básicos de machine learning

## ⚙️ Configuração Inicial

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
2. Configure seu arquivo `.env` na raiz com as credenciais do Azure
3. Instale as dependências necessárias para cada laboratório
4. Verifique o acesso ao Azure AI Foundry

### 3. Variáveis de Ambiente Necessárias
Crie um arquivo `.env` na raiz do projeto com:

```bash
# Azure OpenAI (Obrigatório para todos os labs)
AZURE_OPENAI_ENDPOINT=https://your-openai.openai.azure.com/
AZURE_OPENAI_API_KEY=your-key
API_VERSION=2024-10-21
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_OPENAI_EMBEDDING_MODEL=text-embedding-ada-002

# Azure AI Speech (Lab 2)
SPEECH_ENDPOINT=https://your-speech.cognitiveservices.azure.com/
SPEECH_KEY=your-speech-key
SPEECH_REGION=eastus

# Azure AI Language (Lab 2)  
AZURE_LANGUAGE_ENDPOINT=https://your-language.cognitiveservices.azure.com/
AZURE_LANGUAGE_KEY=your-language-key

# Azure AI Vision (Lab 2)
AZURE_VISION_ENDPOINT=https://your-vision.cognitiveservices.azure.com/
AZURE_VISION_KEY=your-vision-key

# Azure AI Content Safety (Lab 2)
CONTENT_SAFETY_ENDPOINT=https://your-safety.cognitiveservices.azure.com/
CONTENT_SAFETY_KEY=your-safety-key

# Azure AI Search (Lab 5 - Opcional)
AZURE_SEARCH_ENDPOINT=https://your-search.search.windows.net
AZURE_SEARCH_KEY=your-search-key
AZURE_SEARCH_INDEX=rag-index

# Modelos Adicionais (Labs 1 e 4)
AZURE_PHI4_ENDPOINT=https://your-phi4.inference.ai.azure.com
AZURE_PHI4_API_KEY=your-phi4-key
AZURE_PHI4_DEPLOYMENT=phi-4
AZURE_PHI4_API_VERSION=2024-04-01-preview
```

## 🎓 Progressão Recomendada

### **Para Iniciantes:**
1. **Lab 1** → Fundamentos do Azure OpenAI
2. **Lab 2** → Serviços de IA multimodais
3. **Lab 3** → Prompt Engineering básico

### **Para Desenvolvedores Intermediários:**
1. **Labs 1-3** → Base sólida em IA generativa
2. **Lab 4** → Frameworks avançados
3. **Lab 5** → Implementação RAG

### **Para Especialistas:**
- Escolha laboratórios específicos baseados em necessidades
- Combine conceitos de múltiplos labs para projetos complexos
- Use como referência para implementações em produção

## 🎯 Resultados de Aprendizado

Ao concluir este workshop, você será capaz de:

| Competência | Nível | Laboratórios |
|-------------|-------|--------------|
| **Azure AI Foundry** | 🟢 Avançado | Todos |
| **Prompt Engineering** | 🟢 Avançado | Lab 3 |
| **RAG Implementation** | 🟢 Avançado | Lab 5 |
| **Multi-Agent Systems** | 🟡 Intermediário | Lab 4 |
| **Multimodal AI** | 🟡 Intermediário | Labs 1-2 |
| **AI Safety & Governance** | 🟡 Intermediário | Lab 2 |

### **Habilidades Técnicas Desenvolvidas:**
✅ Configurar e usar Azure OpenAI Service efetivamente  
✅ Implementar sistemas RAG de qualidade produtiva  
✅ Aplicar técnicas de prompt engineering para cenários específicos  
✅ Desenvolver agentes especializados com Semantic Kernel e AutoGen  
✅ Integrar múltiplos serviços de IA do Azure  
✅ Seguir melhores práticas de segurança e governança  
✅ Otimizar custos e performance de soluções de IA  

### **Competências de Negócio:**
📈 Identificar casos de uso de IA em organizações  
🛠️ Escolher a tecnologia adequada para cada cenário  
📊 Avaliar ROI e impacto de soluções de IA  
⚖️ Implementar IA responsável e ética  

## 📚 Recursos Adicionais

### **Documentação Oficial:**
- [Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure AI Services](https://learn.microsoft.com/azure/ai-services/)
- [Prompt Engineering Guide](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)

### **Ferramentas e Plataformas:**
- [Azure AI Foundry Portal](https://ai.azure.com/)
- [Azure OpenAI Studio](https://oai.azure.com/)
- [Azure AI Studio](https://ai.azure.com/explore/aiservices)
- [GitHub Copilot](https://github.com/features/copilot) para desenvolvimento

### **Comunidade e Suporte:**
- [Microsoft AI Community](https://learn.microsoft.com/community/)
- [Azure AI Foundry Samples](https://github.com/Azure/AI-Foundry-Samples)
- [Azure OpenAI Examples](https://github.com/Azure/azure-openai-samples)
- [Microsoft Learn](https://learn.microsoft.com/training/browse/?products=azure-openai%2Cazure-ai-services)

### **Certificações Relacionadas:**
- [AI-102: Azure AI Engineer Associate](https://learn.microsoft.com/certifications/azure-ai-engineer/)
- [AI-900: Azure AI Fundamentals](https://learn.microsoft.com/certifications/azure-ai-fundamentals/)
- [Azure Solutions Architect Expert](https://learn.microsoft.com/certifications/azure-solutions-architect/)

## 🚀 Próximos Passos

Após completar o workshop:

1. **🔬 Experimente**: Aplique os conceitos em projetos pessoais
2. **🏢 Implemente**: Use em cenários reais da sua organização  
3. **📢 Compartilhe**: Contribua com a comunidade Azure AI
4. **📖 Continue Aprendendo**: Explore funcionalidades avançadas e novos serviços
5. **🎯 Especialize-se**: Foque em áreas específicas como RAG, Multi-Agent ou Computer Vision

## 💬 Suporte e Contribuições

- **Issues**: Use as [Issues do GitHub](../../issues) para reportar problemas
- **Discussões**: Participe das [Discussions](../../discussions) para trocar ideias
- **Contribuições**: PRs são bem-vindos para melhorias e correções
- **Feedback**: Seus comentários ajudam a melhorar o workshop

---

**Desenvolvido com ❤️ pela comunidade Azure AI**

*Este workshop é mantido pela comunidade e não representa posições oficiais da Microsoft*

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
