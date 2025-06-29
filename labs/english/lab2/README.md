# Lab 2: Exploring Azure Foundry AI Services

## Overview

In this laboratory, you will explore the main AI services available in Azure Foundry, learning to integrate advanced artificial intelligence capabilities into your applications. The laboratory will cover four essential categories of services: Speech, Language + Translator, Vision + Document, and Content Safety.

## Objectives

- Understand and utilize AI services available in Azure Foundry
- Implement speech recognition and audio-to-text conversion
- Explore natural language processing and translation resources
- Work with image analysis and document processing
- Apply content safety techniques to detect harmful material

## Prerequisites

- Azure account with access to AI services
- Environment variables configured in the `.env` file
- Basic Python knowledge
- Completion of Lab 1 (recommended)

## Laboratory Content

### Exercise 1 - Speech

Explore the Azure AI Speech Service, which offers comprehensive speech-to-text and text-to-speech capabilities. This service enables:

- **Audio transcription**: Convert speech to text with high accuracy
- **Voice synthesis**: Produce natural voices from text
- **Audio translation**: Translate spoken audio in real-time
- **Speaker recognition**: Identify different speakers in conversations
- **Customization**: Create custom voices and specific vocabularies

#### Common Use Cases:
- **Caption generation**: Subtitle synchronization with audio
- **Audio content creation**: Audiobooks, voice assistants
- **Call center**: Call transcription and analysis
- **Language learning**: Pronunciation assessment and feedback
- **Voice assistants**: Natural conversational interfaces

#### Required Variables:
- `SPEECH_ENDPOINT`
- `SPEECH_KEY`
- `SPEECH_REGION`

### Exercise 2 - Language + Translator

Discover the Azure AI Language Service, which unifies functionalities previously available in Text Analytics, QnA Maker, and LUIS. This service offers:

#### Text Analysis Resources:
- **Named Entity Recognition (NER)**: Identifies and categorizes entities in text
- **Personal and health information detection**: Identifies sensitive data (PII/PHI)
- **Language detection**: Recognizes diverse languages and dialects
- **Sentiment analysis**: Determines positive/negative sentiments in text
- **Opinion mining**: Links sentiments to specific elements
- **Summarization**: Condenses information from text and conversations
- **Key phrase extraction**: Identifies main concepts
- **Entity linking**: Connects entities to Wikipedia
- **Text analytics for health**: Extracts relevant medical information

#### Custom Resources:
- **Custom text classification**: Customized classification models
- **Custom NER**: Personalized entity categories
- **Conversational Language Understanding (CLU)**: Custom intent models
- **Orchestration workflow**: Connects different language applications
- **Question answering**: Personalized Q&A system

### Exercise 3 - Vision + Document

Explore the Azure AI Vision Service, which offers advanced algorithms for image and document processing:

#### Main Resources:
- **OCR (Optical Character Recognition)**: Extracts text from images and documents
- **Image Analysis**: Detects objects, faces, content, and generates automatic descriptions
- **Face API**: Detects, recognizes, and analyzes human faces
- **Video Retrieval**: Creates searchable indexes of video content

#### Practical Applications:
- Processing commercial documents, invoices, and receipts
- Visual content analysis for classification and moderation
- Identification and access control systems
- Multimedia content indexing and search

### Exercise 4 - Content Safety

Implement Azure AI Content Safety to detect and filter harmful content:

#### Safety Resources:
- **Prompt Shields**: Protects against prompt injection attacks
- **Grounding detection**: Verifies if LLM responses are based on provided sources
- **Protected material detection**: Identifies copyright-protected content
- **Custom categories**: Creates custom filters for specific content
- **Text and image analysis**: Detects sexual, violent, hate, and self-harm content

#### Analysis Levels:
- Multiple severity levels for each category
- APIs for both standard and rapid analysis
- Support for text and images

## Instructions

1. Configure the necessary environment variables in the `.env` file
2. Open the `lab2.ipynb` notebook in Azure AI Foundry
3. Execute cells sequentially for each exercise
4. Test the services with your own data when appropriate
5. Explore different configurations and available parameters

## Additional Resources
- [Azure AI Speech Service](https://learn.microsoft.com/azure/ai-services/speech-service/)
- [Azure AI Language Service](https://learn.microsoft.com/azure/ai-services/language-service/)
- [Azure AI Vision Service](https://learn.microsoft.com/azure/ai-services/computer-vision/)
- [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/)

## Next Steps

After completing this laboratory, you will be prepared to advance to Lab 3, where you will explore advanced prompt engineering techniques to optimize your interactions with AI models.

- [Azure AI Services Documentation](https://docs.microsoft.com/en-us/azure/ai-services/)
- [Code samples on GitHub](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai-services)
- [Azure AI Quick Start Guides](https://docs.microsoft.com/en-us/azure/ai-services/quickstarts/)

## Next Steps

Continue to Lab 3, where we will explore advanced AI integration in applications.
