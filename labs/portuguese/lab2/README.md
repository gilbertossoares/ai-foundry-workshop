# Lab 2: Explorando Serviços de IA do Azure Foundry

## Visão Geral

Neste laboratório você irá explorar os principais serviços de IA disponíveis no Azure Foundry, aprendendo a integrar recursos avançados de inteligência artificial em suas aplicações. O laboratório oferece uma visão abrangente de quatro categorias essenciais: **Speech**, **Language + Translator**, **Vision + Document** e **Content Safety**, com exemplos práticos e casos de uso reais.

## Objetivos

- ✅ Compreender e utilizar os serviços de IA multimodais do Azure Foundry
- ✅ Implementar reconhecimento de fala e síntese de voz com Azure Speech
- ✅ Explorar análise de texto avançada com Azure Language Service
- ✅ Trabalhar com visão computacional e processamento de documentos
- ✅ Aplicar técnicas de moderação de conteúdo para detectar material prejudicial
- ✅ Integrar múltiplos serviços de IA em aplicações práticas

## Pré-requisitos

- Conta Azure com acesso aos serviços de IA (Speech, Language, Vision, Content Safety)
- Variáveis de ambiente configuradas no arquivo `.env` na raiz do projeto
- Conhecimentos básicos de Python e APIs REST
- Conclusão do Lab 1 (recomendado para familiaridade com Azure AI)

## Conteúdo do Laboratório

### Exercício 1 - Speech Service

Explore o **Azure AI Speech Service** com recursos completos de processamento de áudio:

#### Funcionalidades Principais:
- **Transcrição de áudio**: Conversão de fala para texto com alta precisão
- **Síntese de voz**: Geração de vozes naturais a partir de texto
- **Tradução de áudio**: Tradução de fala em tempo real
- **Reconhecimento de locutor**: Identificação de diferentes falantes
- **Personalização**: Vozes customizadas e vocabulários específicos

#### Casos de Uso Demonstrados:
- **Geração de legenda**: Sincronização automática de legendas com áudio
- **Criação de conteúdo de áudio**: Audiolivros e assistentes de voz
- **Central de atendimento**: Transcrição e análise de chamadas telefônicas
- **Aprendizado de idiomas**: Avaliação de pronúncia e feedback
- **Assistentes de voz**: Interfaces conversacionais naturais

#### Exemplo Prático:
- Reconhecimento contínuo de fala em português brasileiro
- Processamento de arquivo de áudio com silêncio inicial
- Configuração de idioma e região

#### Variáveis Necessárias:
- `SPEECH_ENDPOINT` - Endpoint do serviço Speech
- `SPEECH_KEY` - Chave de acesso ao Speech Service
- `SPEECH_REGION` - Região Azure do serviço

### Exercício 2 - Language + Translator Service

Descubra o **Azure AI Language Service**, que unifica Text Analytics, QnA Maker e LUIS:

#### Recursos de Análise de Texto:
- **Reconhecimento de Entidade Nomeada (NER)**: Identifica pessoas, locais, organizações
- **Detecção de PII/PHI**: Identifica informações pessoais e de saúde sensíveis
- **Detecção de idioma**: Reconhece automaticamente idiomas e dialetos
- **Análise de sentimento**: Determina polaridade emocional do texto
- **Mineração de opinião**: Vincula sentimentos a aspectos específicos
- **Sumarização**: Condensa textos longos e conversas
- **Extração de frases-chave**: Identifica conceitos principais automaticamente
- **Vinculação de entidades**: Conecta entidades identificadas à Wikipedia

#### Recursos Personalizados:
- **Classificação de texto personalizada**: Modelos customizados por domínio
- **NER personalizado**: Categorias de entidades específicas do negócio
- **Compreensão de linguagem conversacional (CLU)**: Intenções personalizadas
- **Orquestração de workflow**: Integração entre diferentes serviços
- **Sistema de Q&A**: Respostas baseadas em conhecimento customizado

#### Exemplo Prático:
- Análise de sentimento em português com scores de confiança
- Extração de frases-chave de textos em português
- Processamento de múltiplos documentos simultaneamente

### Exercício 3 - Vision + Document Intelligence

Explore o **Azure AI Vision Service** para processamento visual avançado:

#### Recursos de Visão Computacional:
- **OCR Avançado**: Extração de texto de imagens e documentos digitalizados
- **Análise de Imagem**: Detecção de objetos, pessoas, atividades e conceitos
- **Descrição automática**: Geração de legendas descritivas para imagens
- **Detecção de rostos**: Identificação e análise de características faciais
- **Análise de cenas**: Compreensão do contexto e ambiente da imagem

#### Azure Document Intelligence:
- **Análise de layout**: Extração de estrutura de documentos (tabelas, parágrafos)
- **Modelos pré-construídos**: Processamento de faturas, recibos, cartões de visita
- **Extração de dados estruturados**: Pares chave-valor e informações tabulares
- **OCR para documentos**: Reconhecimento de texto em documentos complexos

#### Exemplos Práticos:
- Análise completa de imagens com múltiplas funcionalidades
- Comparação de análises entre diferentes tipos de imagens
- Processamento de documentos com extração de layout
- Exercício interativo para testar suas próprias imagens

#### Funcionalidades Demonstradas:
- **CAPTION**: Legendas descritivas automáticas
- **READ**: Extração de texto (OCR)
- **TAGS**: Identificação de objetos e conceitos
- **OBJECTS**: Detecção e localização de objetos
- **PEOPLE**: Identificação de pessoas nas imagens
- **SMART_CROPS**: Sugestões de recortes inteligentes

### Exercício 4 - Content Safety

Implemente o **Azure AI Content Safety** para moderação de conteúdo:

#### Recursos de Moderação:
- **Escudos de Prompt**: Proteção contra ataques de prompt injection
- **Detecção de fundamentação**: Verificação de base factual em respostas de LLMs
- **Material protegido**: Identificação de conteúdo protegido por direitos autorais
- **Categorias personalizadas**: Filtros customizados para conteúdo específico
- **Análise multimodal**: Moderação tanto de texto quanto de imagens

#### Categorias de Análise:
- **Ódio (Hate)**: Conteúdo discriminatório ou ofensivo
- **Autolesão (Self-harm)**: Conteúdo relacionado a danos próprios
- **Sexual**: Conteúdo de natureza sexual explícita
- **Violência (Violence)**: Conteúdo violento ou agressivo

#### Características da Implementação:
- Múltiplos níveis de severidade (0-6)
- Análise tanto de texto quanto de imagens
- Interpretação automática de níveis de risco
- Tratamento de erros e casos especiais

#### Exemplos Práticos:
- Análise de textos com diferentes níveis de risco
- Moderação de imagens com categorização automática
- Sistema de scoring para avaliação de segurança
- Comparação entre diferentes tipos de conteúdo

## Instruções de Execução

1. **Configuração Inicial**:
   - Configure todas as variáveis de ambiente necessárias no arquivo `.env`
   - Verifique o acesso aos serviços Azure Speech, Language, Vision e Content Safety

2. **Execução**:
   - Abra o notebook `lab2.ipynb` no Azure AI Foundry ou VS Code
   - Execute as células sequencialmente, observando os resultados de cada serviço
   - Teste com diferentes tipos de conteúdo (áudio, texto, imagens)

3. **Experimentação**:
   - Modifique os exemplos com seus próprios dados
   - Teste diferentes configurações e parâmetros
   - Explore combinações entre diferentes serviços

## Variáveis de Ambiente Necessárias

Configure as seguintes variáveis no arquivo `.env`:

```bash
# Azure Speech Service
SPEECH_ENDPOINT=https://your-speech-service.cognitiveservices.azure.com/
SPEECH_KEY=your-speech-key
SPEECH_REGION=your-region

# Azure Language Service  
AZURE_LANGUAGE_ENDPOINT=https://your-language-service.cognitiveservices.azure.com/
AZURE_LANGUAGE_KEY=your-language-key

# Azure Vision Service
AZURE_VISION_ENDPOINT=https://your-vision-service.cognitiveservices.azure.com/
AZURE_VISION_KEY=your-vision-key

# Azure Document Intelligence
DOC_INTELLIGENCE_ENDPOINT=https://your-doc-intelligence.cognitiveservices.azure.com/
DOC_INTELLIGENCE_KEY=your-doc-intelligence-key

# Azure Content Safety
CONTENT_SAFETY_ENDPOINT=https://your-content-safety.cognitiveservices.azure.com/
CONTENT_SAFETY_KEY=your-content-safety-key
```

## Resultados Esperados

Ao completar este laboratório, você será capaz de:
- Implementar reconhecimento de fala e síntese de voz em aplicações
- Analisar sentimentos e extrair insights de textos em português
- Processar imagens para extração de informações e moderação
- Analisar documentos complexos com extração de dados estruturados
- Implementar sistemas de moderação de conteúdo robustos
- Integrar múltiplos serviços de IA para criar soluções completas

## Recursos Adicionais

### Documentação Oficial:
- [Azure AI Speech Service](https://learn.microsoft.com/azure/ai-services/speech-service/)
- [Azure AI Language Service](https://learn.microsoft.com/azure/ai-services/language-service/)
- [Azure AI Vision Service](https://learn.microsoft.com/azure/ai-services/computer-vision/)
- [Azure AI Document Intelligence](https://learn.microsoft.com/azure/ai-services/document-intelligence/)
- [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)

### Ferramentas Visuais:
- [Azure AI Vision Studio](https://portal.vision.cognitive.azure.com/)
- [Azure AI Language Studio](https://language.cognitive.azure.com/)
- [Azure AI Speech Studio](https://speech.microsoft.com/)
- [Azure AI Content Safety Studio](https://contentsafety.cognitive.azure.com/)

### Casos de Uso Avançados:
- [Análise de Sentimento em Tempo Real](https://learn.microsoft.com/azure/ai-services/language-service/sentiment-opinion-mining/overview)
- [OCR para Documentos Complexos](https://learn.microsoft.com/azure/ai-services/computer-vision/how-to/call-read-api)
- [Moderação de Conteúdo em Escala](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/harm-categories)
- [Sistemas de Transcrição Multilíngue](https://learn.microsoft.com/azure/ai-services/speech-service/language-support)

## Próximos Passos

Após concluir este laboratório, você estará preparado para avançar para o **Lab 3**, onde explorará técnicas avançadas de **Prompt Engineering** para otimizar suas interações com modelos de IA generativa.