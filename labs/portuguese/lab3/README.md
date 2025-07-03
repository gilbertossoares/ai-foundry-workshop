# Lab 3: Prompt Engineering - Técnicas Avançadas de Engenharia de Prompts

## Visão Geral

Neste laboratório, você irá dominar as principais técnicas de **Prompt Engineering** para otimizar a interação com modelos de linguagem de grande escala (LLMs) e obter resultados mais precisos, relevantes e consistentes. A engenharia de prompts é uma habilidade fundamental para maximizar o desempenho de modelos de IA generativa em aplicações reais.

## Objetivos

- ✅ Compreender os fundamentos da engenharia de prompts
- ✅ Dominar 8 técnicas avançadas de prompting com exemplos práticos
- ✅ Aplicar estratégias para melhorar precisão e consistência das respostas
- ✅ Implementar melhores práticas no design de prompts eficazes
- ✅ Comparar diferentes abordagens para cenários específicos
- ✅ Desenvolver habilidades para prompt optimization

## Pré-requisitos

- Conhecimentos básicos de IA e modelos de linguagem
- Conclusão dos Lab 1 e Lab 2 (recomendado para familiaridade com Azure OpenAI)
- Acesso ao Azure OpenAI Service através do Azure AI Foundry
- Variáveis de ambiente configuradas no arquivo `.env`

## Conteúdo do Laboratório

### 1. Zero-Shot Prompting

**Conceito**: Instruções diretas sem exemplos prévios, dependendo do conhecimento pré-treinado do modelo.

**Características**:
- Não requer exemplos de entrada/saída
- Simples de implementar e testar
- Eficaz para tarefas bem definidas
- Depende da qualidade da instrução

**Exemplos Práticos**:
- Tradução de textos
- Classificação de sentimentos
- Tarefas de conhecimento geral

**Quando Usar**: Tarefas simples, testes iniciais, quando não há exemplos disponíveis.

### 2. Few-Shot Prompting

**Conceito**: Fornece 2-5 exemplos demonstrativos antes da tarefa real para estabelecer padrões.

**Características**:
- Melhora precisão comparado ao zero-shot
- Estabelece formato e estilo de resposta
- Eficaz para tarefas que seguem padrões
- Requer curadoria de exemplos de qualidade

**Exemplos Práticos**:
- Classificação com exemplos de cada categoria
- Formatação de dados estruturados
- Tarefas de transformação com padrões específicos

**Quando Usar**: Tarefas estruturadas, quando zero-shot não é suficiente, formatação específica necessária.

### 3. Chain-of-Thought (CoT) Prompting

**Conceito**: Encoraja o modelo a mostrar raciocínio passo a passo antes da resposta final.

**Características**:
- Melhora significativamente problemas complexos
- Permite verificação do processo de raciocínio
- Reduz erros lógicos
- Especialmente eficaz para matemática e lógica

**Exemplos Práticos**:
- Problemas matemáticos com múltiplas etapas
- Análise lógica de situações complexas
- Resolução de problemas que requerem sequência de passos

**Quando Usar**: Problemas matemáticos, lógica complexa, verificação de raciocínio necessária.

### 4. Meta Prompting

**Conceito**: Usa o modelo para gerar ou melhorar prompts para ele mesmo ou outras tarefas.

**Características**:
- Otimização automática de prompts
- Melhoria iterativa da qualidade
- Criação de prompts especializados
- Requer conhecimento sobre técnicas de prompting

**Exemplos Práticos**:
- Geração de prompts para ensino
- Otimização de instruções para domínios específicos
- Criação de variações de prompts para teste

**Quando Usar**: Otimização de prompts existentes, criação de prompts especializados, múltiplas variações.

### 5. Prompt Chaining

**Conceito**: Divide tarefas complexas em múltiplos prompts sequenciais onde a saída de um alimenta o próximo.

**Características**:
- Controle granular sobre cada etapa
- Reduz chance de erros em tarefas complexas
- Permite validação intermediária
- Flexibilidade para modificar etapas individuais

**Exemplos Práticos**:
- Análise de documento → Resumo → Apresentação
- Identificação de problemas → Análise → Soluções → Implementação
- Processamento de dados multi-etapas

**Quando Usar**: Tarefas multi-etapas, transformações complexas, necessidade de controle granular.

### 6. Tree of Thoughts (ToT)

**Conceito**: Explora múltiplos caminhos de raciocínio simultaneamente, como uma árvore de decisão.

**Características**:
- Avalia múltiplas abordagens simultaneamente
- Permite backtracking quando necessário
- Mais robusto que raciocínio linear
- Ideal para problemas com múltiplas soluções

**Exemplos Práticos**:
- Resolução de conflitos organizacionais
- Planejamento estratégico
- Tomada de decisão com múltiplas variáveis
- Análise de cenários complexos

**Quando Usar**: Problemas complexos, múltiplas soluções possíveis, planejamento estratégico.

### 7. Retrieval Augmented Generation (RAG)

**Conceito**: Combina busca de informações externas com geração de texto para respostas mais precisas.

**Características**:
- Acesso a conhecimento externo e atualizado
- Reduz alucinações do modelo
- Permite citação de fontes específicas
- Flexibilidade para atualizar base de conhecimento

**Componentes**:
- Base de conhecimento externa
- Sistema de recuperação (busca)
- Integração contexto + geração
- Controle de qualidade das fontes

**Exemplos Práticos**:
- Sistema de Q&A corporativo
- Assistente com conhecimento específico
- Análise baseada em documentos atuais

**Quando Usar**: Conhecimento específico necessário, informações atualizadas, redução de alucinações.

### 8. Active-Prompt

**Conceito**: Seleção automática dos exemplos mais úteis para few-shot prompting baseado na incerteza do modelo.

**Características**:
- Seleção inteligente de exemplos
- Baseado na incerteza do modelo
- Melhora eficiência do few-shot learning
- Adapta-se automaticamente ao conteúdo

**Exemplos Práticos**:
- Classificação com exemplos adaptativos
- Análise de sentimento contextual
- Sistemas que melhoram com uso

**Quando Usar**: Large pool de exemplos disponível, otimização automática necessária, sistemas adaptativos.

### 9. Melhores Práticas Fundamentais

**Princípios Essenciais**:

- **Seja Específico**: Minimize ambiguidade, restrinja o espaço operacional
- **Seja Descritivo**: Use analogias e metáforas para clarificar instruções
- **Reforce Instruções**: Repita pontos importantes antes e depois do conteúdo
- **A Ordem Importa**: Considere viés de recência na ordem das informações
- **Ofereça Alternativas**: Forneça caminhos alternativos quando a tarefa não puder ser completada

## Instruções de Execução

1. **Configuração Inicial**:
   - Certifique-se de que as variáveis do Azure OpenAI estão configuradas no `.env`
   - Abra o notebook `lab3.ipynb` no Azure AI Foundry ou VS Code

2. **Execução Sequencial**:
   - Execute cada seção de técnica de prompting individualmente
   - Compare os resultados entre diferentes abordagens
   - Experimente modificar os prompts para entender o impacto

3. **Experimentação Prática**:
   - Use a área de experimentação no final do notebook
   - Teste suas próprias técnicas e combinações
   - Documente quais abordagens funcionam melhor para seus casos de uso

## Estrutura do Laboratório

O notebook está organizado com:
- **Configuração inicial** do Azure OpenAI
- **8 seções de técnicas** com exemplos práticos
- **Comparações diretas** entre abordagens
- **Área de experimentação** para testes personalizados
- **Melhores práticas** consolidadas

## Resultados Esperados

Ao completar este laboratório, você será capaz de:
- Escolher a técnica de prompting adequada para cada cenário
- Criar prompts mais eficazes e consistentes
- Reduzir alucinações e melhorar precisão das respostas
- Implementar sistemas de prompting adaptativos
- Otimizar custos através de prompts mais eficientes
- Combinar múltiplas técnicas para casos complexos

## Casos de Uso por Técnica

| Técnica | Melhor Para | Exemplo de Uso |
|---------|-------------|----------------|
| Zero-Shot | Tarefas simples, teste inicial | Tradução, classificação básica |
| Few-Shot | Tarefas estruturadas | Formatação de dados, classificação específica |
| Chain-of-Thought | Problemas complexos | Matemática, análise lógica |
| Meta Prompting | Otimização de prompts | Criação de prompts especializados |
| Prompt Chaining | Workflows complexos | Análise → Resumo → Ação |
| Tree of Thoughts | Múltiplas soluções | Planejamento estratégico |
| RAG | Conhecimento específico | Q&A corporativo, documentos |
| Active-Prompt | Sistemas adaptativos | Classificação contextual |

## Recursos Adicionais

### Documentação e Pesquisa:
- [Azure OpenAI Prompt Engineering](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Chain-of-Thought Papers](https://arxiv.org/abs/2201.11903)
- [Tree of Thoughts Research](https://arxiv.org/abs/2305.10601)

### Ferramentas Complementares:
- [Azure AI Foundry Prompt Flow](https://learn.microsoft.com/azure/ai-foundry/how-to/prompt-flow)
- [Azure OpenAI Studio](https://oai.azure.com/)
- [Prompt Engineering Tools](https://learn.microsoft.com/azure/ai-services/openai/concepts/advanced-usage)

### Próximos Passos:
- **Lab 4**: Frameworks avançados (Semantic Kernel, AutoGen)
- **Lab 5**: Implementação de RAG completo
- **Projetos Práticos**: Aplicação em cenários reais

## Dicas de Otimização

1. **Performance**: Comece com zero-shot, evolua para few-shot se necessário
2. **Custo**: Use chain-of-thought apenas quando raciocínio for crítico
3. **Precisão**: Combine RAG com few-shot para máxima precisão
4. **Flexibilidade**: Use prompt chaining para workflows adaptativos
5. **Debugging**: Chain-of-thought ajuda a identificar onde o raciocínio falha