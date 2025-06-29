# Lab 2: Explorando Serviços de IA do Azure Foundry

## Visão Geral

Neste laboratório você irá explorar os principais serviços de IA disponíveis no Azure Foundry, aprendendo a integrar recursos avançados de inteligência artificial em suas aplicações. O laboratório cobrirá quatro categorias essenciais de serviços: Speech, Language + Translator, Vision + Document e Content Safety.

## Objetivos

- Compreender e utilizar os serviços de IA disponíveis no Azure Foundry
- Implementar reconhecimento de fala e conversão de áudio para texto
- Explorar recursos de processamento de linguagem natural e tradução
- Trabalhar com análise de imagens e processamento de documentos
- Aplicar técnicas de segurança de conteúdo para detectar material prejudicial

## Pré-requisitos

- Conta Azure com acesso aos serviços de IA
- Variáveis de ambiente configuradas no arquivo `.env`
- Conhecimentos básicos de Python
- Conclusão do Lab 1 (recomendado)

## Conteúdo do Laboratório

### Exercício 1 - Speech

Explore o Azure AI Speech Service, que oferece recursos completos de conversão de fala para texto e texto para fala. Este serviço permite:

- **Transcrição de áudio**: Converta fala para texto com alta precisão
- **Síntese de voz**: Produza vozes naturais a partir de texto
- **Tradução de áudio**: Traduza áudio falado em tempo real
- **Reconhecimento de locutor**: Identifique diferentes falantes em conversas
- **Personalização**: Crie vozes customizadas e vocabulários específicos

#### Casos de Uso Comuns:
- **Geração de legenda**: Sincronização de legendas com áudio
- **Criação de conteúdo de áudio**: Audiolivros, assistentes de voz
- **Central de atendimento**: Transcrição e análise de chamadas
- **Aprendizado de idiomas**: Avaliação de pronúncia e feedback
- **Assistentes de voz**: Interfaces conversacionais naturais

#### Variáveis Necessárias:
- `SPEECH_ENDPOINT`
- `SPEECH_KEY`
- `SPEECH_REGION`

### Exercício 2 - Language + Translator

Descubra o Azure AI Language Service, que unifica funcionalidades anteriormente disponíveis em Text Analytics, QnA Maker e LUIS. Este serviço oferece:

#### Recursos de Análise de Texto:
- **Reconhecimento de Entidade Nomeada (NER)**: Identifica e categoriza entidades no texto
- **Detecção de informações pessoais e de saúde**: Identifica dados sensíveis (PII/PHI)
- **Detecção de idioma**: Reconhece idiomas e dialetos diversos
- **Análise de sentimento**: Determina sentimentos positivos/negativos no texto
- **Mineração de opinião**: Vincula sentimentos a elementos específicos
- **Sumarização**: Condensa informações de texto e conversas
- **Extração de frases-chave**: Identifica conceitos principais
- **Vinculação de entidades**: Conecta entidades à Wikipedia
- **Análise de texto para saúde**: Extrai informações médicas relevantes

#### Recursos Personalizados:
- **Classificação de texto personalizada**: Modelos customizados de classificação
- **NER personalizado**: Categorias de entidades personalizadas
- **Compreensão de linguagem conversacional (CLU)**: Modelos de intenção personalizados
- **Fluxo de trabalho de orquestração**: Conecta diferentes aplicações de linguagem
- **Resposta a perguntas**: Sistema de Q&A personalizado

### Exercício 3 - Vision + Document

Explore o Azure AI Vision Service, que oferece algoritmos avançados para processamento de imagens e documentos:

#### Recursos Principais:
- **OCR (Reconhecimento Óptico de Caracteres)**: Extrai texto de imagens e documentos
- **Análise de Imagem**: Detecta objetos, rostos, conteúdo e gera descrições automáticas
- **Face API**: Detecta, reconhece e analisa rostos humanos
- **Recuperação de Vídeo**: Cria índices pesquisáveis de conteúdo de vídeo

#### Aplicações Práticas:
- Processamento de documentos comerciais, faturas e recibos
- Análise de conteúdo visual para classificação e moderação
- Sistemas de identificação e controle de acesso
- Indexação e busca de conteúdo multimídia

### Exercício 4 - Content Safety

Implemente o Azure AI Content Safety para detectar e filtrar conteúdo prejudicial:

#### Recursos de Segurança:
- **Escudos de Prompt**: Protege contra ataques de prompt injection
- **Detecção de fundamentação**: Verifica se respostas de LLMs estão baseadas em fontes fornecidas
- **Detecção de material protegido**: Identifica conteúdo protegido por direitos autorais
- **Categorias personalizadas**: Cria filtros customizados para conteúdo específico
- **Análise de texto e imagem**: Detecta conteúdo sexual, violento, de ódio e autolesão

#### Níveis de Análise:
- Múltiplos níveis de severidade para cada categoria
- APIs tanto para análise padrão quanto rápida
- Suporte para texto e imagens

## Instruções

1. Configure as variáveis de ambiente necessárias no arquivo `.env`
2. Abra o notebook `lab2.ipynb` no Azure AI Foundry
3. Execute as células sequencialmente para cada exercício
4. Teste os serviços com seus próprios dados quando apropriado
5. Explore as diferentes configurações e parâmetros disponíveis

## Recursos Adicionais

- [Azure AI Speech Service](https://learn.microsoft.com/azure/ai-services/speech-service/)
- [Azure AI Language Service](https://learn.microsoft.com/azure/ai-services/language-service/)
- [Azure AI Vision Service](https://learn.microsoft.com/azure/ai-services/computer-vision/)
- [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)

## Próximos Passos

Após concluir este laboratório, você estará preparado para avançar para o Lab 3, onde explorará técnicas avançadas de engenharia de prompts (Prompt Engineering) para otimizar suas interações com modelos de IA.