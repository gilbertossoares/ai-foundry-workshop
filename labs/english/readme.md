# Azure AI Foundry Workshop

This repository contains a series of hands-on laboratories designed to explore and learn about Azure AI services, with a focus on Azure AI Foundry and related technologies.

## Workshop Overview

This comprehensive workshop offers a complete journey through the latest capabilities of Azure AI Foundry, from fundamental concepts to advanced AI implementations. Each laboratory is carefully designed to build knowledge progressively, enabling you to master essential tools and techniques for AI development.

## Laboratory Structure

### [Lab 1: Connection and First Steps with Azure OpenAI](lab1/)
**Fundamentals and Initial Configuration**

- Configuration and connection with Azure OpenAI Service
- First API calls and detailed response analysis
- Generation and use of embeddings for semantic analysis
- Image processing with multimodal models
- Exploration of other LLM models available in Azure AI Foundry
- Advanced features: Responses API, Reasoning Models, Function Calling

**Key Resources Covered:**
- Credential and endpoint configuration
- Important parameters (temperature, top_p, frequency_penalty)
- Metadata analysis and token usage
- Embeddings and their practical applications
- Multimodal models for image processing

### [Lab 2: Exploring Azure Foundry AI Services](lab2/)
**Complete Ecosystem of AI Services**

- **Azure AI Speech**: Speech recognition, voice synthesis, and audio translation
- **Azure AI Language + Translator**: Text analysis, NER, sentiment analysis, translation
- **Azure AI Vision + Document**: OCR, image analysis, document processing
- **Azure AI Content Safety**: Detection and filtering of harmful content

**Implemented Use Cases:**
- Audio transcription and subtitle generation
- Semantic analysis of texts and documents
- Processing of commercial documents and invoices
- Content moderation systems

### [Lab 3: Prompt Engineering](lab3/)
**Advanced Prompt Engineering Techniques**

- **Zero-Shot Prompting**: Creating effective prompts without examples
- **Few-Shot Prompting**: Quality improvement with targeted examples
- **Chain-of-Thought Prompting**: Encouraging step-by-step reasoning
- **Meta Prompting**: Instructions on how to approach different tasks
- **Prompt Chaining**: Breaking complex tasks into focused sequences
- **Tree of Thoughts (ToT)**: Considering multiple reasoning lines
- **Retrieval Augmented Generation (RAG)**: Combining external information
- **Active-Prompt**: Dynamically adapting prompts

**Best Practices:**
- Specificity and clarity in instructions
- Effective use of analogies and examples
- Importance of order and structure
- Fallback strategies and alternatives

### [Lab 4: LLM Frameworks - Semantic Kernel, AutoGen and LangChain](lab4/)
**Development with Specialized Frameworks**

- **Semantic Kernel**: Microsoft framework for modular LLM integration
- **AutoGen**: Creating conversational agents and multi-agent flows
- **LangChain**: Components for LLM-based applications

**Framework Comparison:**
- Strengths and ideal use cases for each framework
- Practical implementation examples
- Integration with existing ecosystems
- Architecture and deployment considerations

**Practical Exercises:**
- Implementation of specialized agents
- Creation of complex processing flows
- Integration with external APIs and services

### [Lab 5: RAG Implementation with Azure OpenAI and Azure AI Search](lab5/)
**Advanced Retrieval and Generation Patterns**

- Fundamental concepts of RAG (Retrieval Augmented Generation)
- Configuration of Azure OpenAI and Azure AI Search
- Creation and indexing of knowledge bases
- Implementation of complete RAG flows
- Optimization and refinement strategies

**Implemented Architecture:**
- Knowledge base indexed in Azure AI Search
- Retrieval services for relevant documents
- Language models for informed generation
- Quality evaluation and metrics

**Advanced Techniques:**
- Document chunking and embedding
- Semantic filtering
- Result reranking
- Cache and performance strategies

## Prerequisites

### Required
- Azure subscription with access to AI services
- Python 3.8 or higher
- Basic knowledge of programming and APIs
- Access to Azure AI Foundry

### Recommended
- Visual Studio Code with Azure and Python extensions
- Azure CLI for command-line interactions
- Git for version control
- Basic machine learning knowledge

## Initial Setup

### 1. Azure Environment Preparation
```bash
# Login to Azure
az login

# Set your subscription
az account set --subscription "your-subscription-id"

# Create resource group for the workshop
az group create --name "ai-foundry-workshop-rg" --location "eastus"
```

### 2. Local Configuration
1. Clone this repository
2. Configure your `.env` file with Azure credentials
3. Install required dependencies for each laboratory
4. Verify access to Azure AI Foundry

### 3. Required Environment Variables
```
# Azure OpenAI
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_API_VERSION=

# Azure AI Services
SPEECH_ENDPOINT=
SPEECH_KEY=
SPEECH_REGION=

LANGUAGE_ENDPOINT=
LANGUAGE_KEY=

VISION_ENDPOINT=
VISION_KEY=

CONTENT_SAFETY_ENDPOINT=
CONTENT_SAFETY_KEY=

# Azure AI Search (Lab 5)
SEARCH_ENDPOINT=
SEARCH_KEY=
```

## Recommended Progression

1. **Beginners**: Start with Lab 1 to understand fundamentals
2. **Intermediate**: Labs 1-3 provide a solid foundation in generative AI
3. **Advanced**: Labs 4-5 address complex architectures and patterns
4. **Specialization**: Choose specific laboratories based on your needs

## Learning Outcomes

Upon completing this workshop, you will be able to:

✅ **Master Azure AI Foundry**: Navigate and use the platform effectively
✅ **Develop AI Solutions**: Build complete end-to-end applications
✅ **Apply Prompt Engineering**: Optimize interactions with language models
✅ **Implement RAG Patterns**: Combine retrieval and generation for precise responses
✅ **Use Specialized Frameworks**: Choose and implement the right tools
✅ **Integrate Multiple Services**: Combine different Azure AI services
✅ **Follow Best Practices**: Implement adequate security and governance

## Additional Resources

### Official Documentation
- [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)
- [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Azure AI Services](https://learn.microsoft.com/en-us/azure/ai-services/)
- [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/)

### Tutorials and Guides
- [Prompt Engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)
- [RAG Patterns](https://learn.microsoft.com/en-us/azure/architecture/pattern/ai/retrieval-augmented-generation-pattern)
- [Responsible AI](https://www.microsoft.com/ai/responsible-ai)

### Community and Support
- [Microsoft Learn - AI Courses](https://learn.microsoft.com/en-us/training/browse/?products=azure-cognitive-services)
- [Azure AI Community](https://techcommunity.microsoft.com/category/azure-ai)
- [Stack Overflow - Azure AI](https://stackoverflow.com/questions/tagged/azure-ai)

## Troubleshooting

### Common Issues
- **Access denied errors**: Verify Azure subscription permissions and AI Foundry access
- **Quota limits**: Check Azure quotas for AI services in your region
- **Network connectivity**: Ensure proper firewall and network configuration

### Getting Help
- Check the troubleshooting guide in each laboratory
- Review Azure AI Foundry documentation
- Open an issue in this repository for workshop-specific problems

## Next Steps

After completing this workshop, consider:

- **Azure AI Certifications**: Explore AI-102 and AI-900 certifications
- **Practical Projects**: Implement AI solutions in real-world scenarios
- **Community**: Join AI developer communities
- **Continuous Learning**: Stay updated with Azure AI innovations

---

*This workshop is designed to provide hands-on experience with the latest Azure AI technologies. Each laboratory builds upon the previous one, creating a comprehensive and structured learning journey.*

**Ready to start?** Begin with [Lab 1](lab1/) and start your Azure AI Foundry journey!
