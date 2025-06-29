# Lab 1: Connection and First Steps with Azure OpenAI

## Overview

In this laboratory, you will take the first steps with Azure OpenAI Service, from initial configuration to executing practical tasks including API calls, response analysis, embedding generation, image processing, and exploring other models available in Azure AI Foundry.

## Objectives

- Configure and connect with Azure OpenAI Service
- Perform basic and advanced calls to the chat completions API
- Analyze API responses in detail
- Generate and work with text embeddings
- Process images using multimodal models
- Explore other LLM models available in Azure AI Foundry

## Prerequisites

- Azure account with access to Azure OpenAI Service
- Environment variables configured in the `.env` file
- Basic Python knowledge
- Access to Azure AI Foundry

## Laboratory Content

### Exercise 1 - API Call

Learn to configure the Azure OpenAI client and make your first API call, including:
- Credential and endpoint configuration
- Message structuring with different roles (system, user, assistant)
- Executing chat completion calls

### Exercise 2 - Analyzing the Response

Explore in detail the complete structure of the API response, including:
- Response metadata analysis
- Token usage information
- Content filtering details
- Prompt and completion token counters
- Reasoning token details for advanced models

Experiment with important parameters such as:
- **max_completion_tokens**: Control response size
- **temperature**: Adjust creativity (0.0 = deterministic, 1.0 = creative)
- **top_p**: Control diversity via nucleus sampling
- **frequency_penalty**: Penalization for frequency-based repetition
- **presence_penalty**: Penalization for repetition independent of frequency

### Exercise 3 - Embeddings

Discover how to work with embeddings for semantic analysis:
- Generate embeddings from text
- Understanding numerical representations of meaning
- Use cases for semantic search, classification, and similarity analysis

Explore embedding storage options in Azure:
- Azure AI Search
- Azure Cosmos DB (MongoDB vCore, NoSQL, PostgreSQL)
- Azure SQL Database
- Azure Cache for Redis
- Azure Database for PostgreSQL
- Microsoft Fabric Eventhouse

### Exercise 4 - Image Processing

Learn to work with multimodal models:
- Sending images via URL
- Encoding local images to base64
- Combining text and images in prompts
- Image description and analysis using AI

### Exercise 5 - Other Models in Azure AI Foundry

Explore the diversity of models available through the Model Catalog:
- Microsoft models (OpenAI, Meta, Mistral AI, Deepseek, xAI, Black Forest Labs)
- Partner models (Nixtla, AI21, NTT Data, Core42, NVIDIA NIM, Stability AI)
- Configuration and use of different client libraries
- Practical example with Phi-4 model

### Available Advanced Features

The laboratory also presents other Azure OpenAI functionalities:
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

## Instructions

1. Configure environment variables in the `.env` file at the repository root
2. Open the `lab1.ipynb` notebook in Azure AI Foundry
3. Execute cells sequentially, observing examples and results
4. Experiment with modifying parameters to understand their impact
5. Test with your own prompts and images

## Additional Resources

- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [How to work with embeddings](https://learn.microsoft.com/azure/ai-services/openai/how-to/embeddings)
- [Azure AI Foundry Model Catalog](https://learn.microsoft.com/azure/ai-foundry/concepts/foundry-models-overview)
- [Chat Completions API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt)
- [Function Calling](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling)
- [Structured Outputs](https://learn.microsoft.com/azure/ai-services/openai/how-to/structured-outputs)

## Next Steps

After completing this laboratory, you will be prepared to advance to Lab 2, where you will explore more advanced concepts of implementation and specific use cases with Azure OpenAI.
