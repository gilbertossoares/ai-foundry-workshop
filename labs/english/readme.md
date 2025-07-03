# Azure AI Foundry Workshop

This repository contains a comprehensive series of hands-on laboratories designed to explore and master Azure AI services, with a special focus on Azure AI Foundry and its ecosystem. The workshop provides a complete learning journey from basic concepts to advanced AI implementations.

## Workshop Overview

This comprehensive workshop offers a complete journey through the latest capabilities of Azure AI Foundry, from fundamental concepts to advanced AI implementations. Each laboratory is carefully designed to build knowledge progressively, enabling you to master essential tools and techniques for modern AI development.

The workshop covers 5 progressive laboratories that explore everything from basic Azure OpenAI connections to complex multi-agent systems and RAG implementations. Each lab includes practical exercises, real examples, and hands-on activities to consolidate learning.

## Laboratory Structure

### [Lab 1: Connection and First Steps with Azure OpenAI](lab1/)
**Fundamentals and API Mastery**

Learn the fundamentals of Azure OpenAI through hands-on practice:
- Azure OpenAI Service configuration and connection
- Basic and advanced API calls with chat completions
- Detailed analysis of API responses and metadata
- Generation and comparison of text embeddings for semantic analysis
- Image processing with multimodal models (computer vision)
- Exploration of other LLM models available in Azure AI Foundry Model Catalog
- 5 practical activities to consolidate learning

**Key Topics Covered:**
- Client configuration and authentication
- Important parameters (temperature, top_p, frequency_penalty, presence_penalty)
- Token usage analysis and cost optimization  
- Embeddings and their practical applications
- Multimodal prompts with images
- Other models via azure-ai-inference library

**Advanced Features Presented:**
- Responses API, Reasoning Models, Computer Use, Model Router
- Function Calling, Predicted Outputs, Prompt Caching
- Structured Outputs, Vision-enabled Chats, JSON Mode

### [Lab 2: Azure AI Services Ecosystem](lab2/)
**Complete Suite of AI Services**

Deep exploration of Azure AI services beyond OpenAI:
- **Azure AI Speech**: Speech-to-text, text-to-speech, audio translation
- **Azure AI Language + Translator**: Sentiment analysis, NER, key phrase extraction, translation
- **Azure AI Vision + Document**: OCR, image analysis, object detection, document processing
- **Azure AI Content Safety**: Text and image content moderation

**Practical Examples:**
- Continuous speech recognition from audio files
- Sentiment analysis with confidence scores
- Complete image analysis with multiple features
- Document intelligence for structured data extraction
- Content safety for text and image moderation

**Real Use Cases:**
- Call center transcription and analysis
- Multi-language content processing
- Document automation for business processes
- Content moderation systems

### [Lab 3: Prompt Engineering Mastery](lab3/)
**Advanced Prompt Engineering Techniques**

Master the art and science of prompt engineering:
- **Zero-Shot Prompting**: Creating effective prompts without examples
- **Few-Shot Prompting**: Quality improvement with targeted examples  
- **Chain-of-Thought Prompting**: Encouraging step-by-step reasoning
- **Meta Prompting**: Instructions on how to approach different tasks
- **Prompt Chaining**: Breaking complex tasks into focused sequences
- **Tree of Thoughts (ToT)**: Exploring multiple reasoning paths
- **Retrieval Augmented Generation (RAG)**: Combining external information
- **Active-Prompt**: Dynamically adapting prompts based on context

**Structure and Content:**
- Complete theoretical explanation of each technique
- Practical examples with Azure OpenAI
- Comparison of results between different approaches
- Hands-on exercises and experiments
- Best practices and common pitfalls

**Best Practices Covered:**
- Specificity and clarity in instructions
- Effective use of examples and analogies  
- Importance of order and structure
- Fallback strategies and error handling

### [Lab 4: AI Frameworks - Semantic Kernel and AutoGen](lab4/)
**Building with Specialized Frameworks**

Explore powerful frameworks for advanced AI applications:
- **Semantic Kernel**: Microsoft's SDK for LLM integration with conventional code
- **AutoGen**: Framework for multi-agent conversational AI systems

**Semantic Kernel Concepts:**
- Kernel configuration and AI service integration
- Creating and using plugins (built-in and custom)
- Function orchestration and planning
- Prompt templates and argument handling

**AutoGen Features:**
- Creating specialized conversational agents
- Multi-agent collaboration and group chats
- Agent roles and conversation flows
- Practical examples with Azure OpenAI

**Practical System:**
- Complete product analysis system implementation
- Integration between Semantic Kernel and AutoGen
- When to use each framework
- Architecture and deployment considerations

**Real Examples:**
- Custom math plugin creation
- Sentiment analysis plugin
- Creative assistant agents
- Multi-agent product review system

### [Lab 5: RAG Implementation with Azure AI Search](lab5/)
**Retrieval-Augmented Generation Patterns**

Complete implementation of RAG systems:
- Fundamental RAG concepts and architecture
- Azure OpenAI and Azure AI Search configuration
- Knowledge base creation and indexing
- Complete RAG pipeline implementation
- Quality comparison: with vs. without RAG

**Implementation Components:**
- Document preparation and embedding generation
- Semantic search simulation (cosine similarity)
- Context integration with generation
- Real implementation with Azure AI Search
- Performance optimization and best practices

**Advanced Techniques:**
- Document chunking strategies
- Embedding storage options in Azure
- Semantic filtering and reranking
- Cache and performance optimization
- Quality evaluation metrics

**Expected Results:**
- Understand when and how to use RAG
- Implement production-ready RAG systems
- Integrate multiple Azure services effectively
- Apply best practices for accuracy and performance

## Prerequisites

### Required
- Azure subscription with access to Azure OpenAI Service
- Python 3.8 or higher
- Basic knowledge of programming and APIs
- Access to Azure AI Foundry

### Recommended
- Visual Studio Code with Azure and Python extensions
- Azure CLI for command-line interactions
- Git for version control
- Basic understanding of machine learning concepts

## Initial Setup

### 1. Environment Preparation
```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
# Edit .env with your Azure credentials

# Verify setup
python check_environment.py
```

### 2. Azure Services Required
- Azure OpenAI Service (required for all labs)
- Azure AI Speech (Lab 2)
- Azure AI Language (Lab 2)  
- Azure AI Vision (Lab 2)
- Azure AI Content Safety (Lab 2)
- Azure AI Search (Lab 5)

### 3. Environment Variables Configuration
Complete template available in `.env.example`. Key variables:

```env
# Azure OpenAI (required)
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
API_VERSION=2024-02-01

# Additional services as needed per lab
AZURE_LANGUAGE_ENDPOINT=...
AZURE_VISION_ENDPOINT=...
AZURE_SEARCH_ENDPOINT=...
```

## Recommended Progression

1. **Beginners**: Start with Lab 1 to understand fundamentals, then proceed sequentially
2. **Intermediate**: Labs 1-3 provide a solid foundation in generative AI and prompt engineering
3. **Advanced**: Labs 4-5 address complex architectures, frameworks, and RAG patterns
4. **Specialization**: Focus on specific laboratories based on your project needs

**Estimated Time:**
- Lab 1: 2-3 hours (foundations)
- Lab 2: 2-3 hours (AI services)
- Lab 3: 1-2 hours (prompt engineering)
- Lab 4: 2-3 hours (frameworks)
- Lab 5: 2-3 hours (RAG implementation)

## Learning Outcomes

Upon completing this workshop, you will be able to:

✅ **Master Azure AI Foundry**: Navigate the platform and use all major features effectively
✅ **Develop Complete AI Solutions**: Build end-to-end AI applications with Azure services  
✅ **Apply Advanced Prompt Engineering**: Optimize interactions with language models using proven techniques
✅ **Implement RAG Patterns**: Combine retrieval and generation for precise, knowledge-grounded responses
✅ **Use Specialized Frameworks**: Choose and implement Semantic Kernel, AutoGen based on requirements
✅ **Integrate Multiple AI Services**: Combine speech, vision, language, and content safety services
✅ **Follow Best Practices**: Implement proper security, governance, and optimization patterns
✅ **Handle Real-World Scenarios**: Process multimodal content, build conversational agents, moderate content

## Additional Resources

### Official Documentation
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure AI Services](https://learn.microsoft.com/azure/ai-services/)
- [Azure AI Search](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)
- [AutoGen Framework](https://github.com/microsoft/autogen)

### Tutorials and Guides
- [Prompt Engineering Guide](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)
- [RAG Patterns and Best Practices](https://learn.microsoft.com/azure/architecture/pattern/ai/retrieval-augmented-generation-pattern)
- [Responsible AI Guidelines](https://www.microsoft.com/ai/responsible-ai)
- [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)

### Community and Support
- [Microsoft Learn - AI Learning Paths](https://learn.microsoft.com/training/browse/?products=azure-cognitive-services)
- [Azure AI Tech Community](https://techcommunity.microsoft.com/category/azure-ai)
- [GitHub - Azure AI Samples](https://github.com/Azure-Samples/azure-ai-samples)

## Troubleshooting

### Common Issues
- **Access denied errors**: Verify Azure subscription permissions and Azure AI Foundry access
- **Quota limits**: Check Azure quotas for AI services in your region  
- **Network connectivity**: Ensure proper firewall and network configuration
- **Environment variables**: Use `python check_environment.py` to verify setup

### Getting Help
- Check the troubleshooting section in each laboratory README
- Review Azure AI Foundry documentation for service-specific issues
- Use the `check_environment.py` script to diagnose setup problems
- Check `SETUP.md` for detailed configuration instructions

## File Structure

```
├── requirements.txt          # All dependencies for the workshop
├── .env.example             # Environment variables template  
├── SETUP.md                 # Detailed setup instructions
├── check_environment.py     # Environment verification script
├── samples/                 # Sample files for exercises
└── labs/
    ├── english/
    │   ├── readme.md        # This file
    │   ├── lab1/            # Azure OpenAI fundamentals
    │   ├── lab2/            # Azure AI Services
    │   ├── lab3/            # Prompt Engineering
    │   ├── lab4/            # Semantic Kernel & AutoGen
    │   └── lab5/            # RAG Implementation
    └── portuguese/          # Portuguese version
```

## Next Steps

After completing this workshop, consider:

- **Azure AI Certifications**: Explore AI-102 (Azure AI Engineer) and AI-900 (Azure AI Fundamentals)
- **Production Deployment**: Implement your solutions in real-world scenarios using Azure Container Apps or App Service
- **Advanced Topics**: Explore Azure Machine Learning, MLOps, and custom model training
- **Community Engagement**: Join AI developer communities and contribute to open-source projects
- **Continuous Learning**: Stay updated with the latest Azure AI innovations and features

---

*This workshop provides hands-on experience with the latest Azure AI technologies through a structured, progressive learning approach. Each laboratory builds upon previous knowledge while introducing new concepts and practical applications.*

**Ready to begin your Azure AI journey?** Start with [Lab 1](lab1/) and explore the foundations of Azure OpenAI!
