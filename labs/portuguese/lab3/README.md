# Lab 3: Prompt Engineering

## Visão Geral

Neste laboratório, você irá explorar as principais técnicas de engenharia de prompts (Prompt Engineering) para otimizar a interação com modelos de linguagem e obter resultados mais precisos e relevantes. A engenharia de prompts é uma habilidade fundamental para maximizar o desempenho de modelos de IA generativa.

## Objetivos

- Compreender os fundamentos da engenharia de prompts
- Dominar diferentes técnicas de prompting
- Aplicar estratégias avançadas para melhorar a qualidade das respostas
- Implementar melhores práticas no design de prompts

## Pré-requisitos

- Conhecimentos básicos de IA e modelos de linguagem
- Conclusão dos Lab 1 e Lab 2 (recomendado)
- Acesso ao Azure AI Foundry

## Conteúdo do Laboratório

### 1. Zero-Shot Prompting
Aprenda a criar prompts eficazes sem fornecer exemplos, utilizando apenas instruções claras e específicas para orientar o modelo.

### 2. Few-Shot Prompting
Explore como fornecer alguns exemplos no prompt pode melhorar significativamente a qualidade e consistência das respostas do modelo.

### 3. Chain-of-Thought Prompting
Descubra como incentivar o modelo a mostrar seu raciocínio passo a passo, resultando em respostas mais lógicas e bem fundamentadas.

### 4. Meta Prompting
Entenda como criar prompts que instruem o modelo sobre como abordar diferentes tipos de tarefas de forma mais eficiente.

### 5. Prompt Chaining
Aprenda a dividir tarefas complexas em uma sequência de prompts mais simples e focados.

### 6. Tree of Thoughts (ToT)
Explore uma técnica avançada que permite ao modelo considerar múltiplas linhas de raciocínio simultaneamente.

### 7. Retrieval Augmented Generation (RAG)
Compreenda como combinar informações externas com prompts para gerar respostas mais precisas e atualizadas.

### 8. Active-Prompt
Descubra técnicas para criar prompts que se adaptam dinamicamente com base no contexto e feedback.

### 9. Melhores Práticas

Aplique os princípios fundamentais para criar prompts mais eficazes:

- **Seja Específico**: Deixe o mínimo possível para interpretação. Restrinja o espaço operacional.
- **Seja Descritivo**: Use analogias para tornar as instruções mais claras.
- **Reforce as Instruções**: Às vezes pode ser necessário se repetir para o modelo. Forneça instruções antes e depois do seu conteúdo principal.
- **A Ordem Importa**: A ordem em que você apresenta informações ao modelo pode impactar o resultado. O viés de recência pode afetar como o modelo processa as informações.
- **Ofereça uma Alternativa**: Dê ao modelo um caminho alternativo se ele não conseguir completar a tarefa. Por exemplo: "responda com 'não encontrado' se a resposta não estiver presente."

## Instruções

1. Abra o notebook `lab3.ipynb` no Azure AI Foundry
2. Execute as células sequencialmente, observando os exemplos de cada técnica
3. Experimente modificar os prompts para ver como as mudanças afetam os resultados
4. Compare a eficácia das diferentes abordagens para tarefas similares

## Recursos Adicionais

- [Documentação do Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/)
- [Guia de Engenharia de Prompts](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)
- [Técnicas Avançadas de Prompting](https://learn.microsoft.com/azure/ai-services/openai/concepts/advanced-prompt-engineering)

## Próximos Passos

Após concluir este laboratório, você estará preparado para aplicar técnicas avançadas de engenharia de prompts em seus projetos, criando interações mais eficazes com modelos de IA e obtendo resultados mais precisos e consistentes.