# Azure AI Foundry Workshop

Welcome to the Azure AI Foundry Workshop! This comprehensive hands-on workshop will guide you through the latest capabilities of Azure AI Foundry, Microsoft's unified platform for building, deploying, and managing AI applications.

## 🎯 Workshop Overview

Azure AI Foundry provides a collaborative environment for AI development, offering tools for data preparation, model training, fine-tuning, evaluation, and deployment. This workshop covers everything from getting started to advanced scenarios with practical implementations.

## 📚 Available Languages

This workshop is available in multiple languages:

- **English**: `/labs/english/` - Complete workshop materials in English
- **Português (Brasil)**: `/labs/portuguese/` - Materiais completos do workshop em português brasileiro

## 🚀 What You'll Learn

This workshop provides a complete journey through Azure AI capabilities, structured in five progressive laboratories:

### 🔧 [Lab 1: Connection and First Steps with Azure OpenAI](labs/english/lab1/) | [Lab 1: Conexão e Primeiros Passos](labs/portuguese/lab1/)
**Fundamentals and Initial Configuration**
- Configure and connect with Azure OpenAI Service
- Master API calls and detailed response analysis
- Generate embeddings for semantic analysis
- Process images with multimodal models
- Explore advanced features like Function Calling and Reasoning Models

### 🧠 [Lab 2: Exploring Azure AI Services Ecosystem](labs/english/lab2/) | [Lab 2: Serviços de IA do Azure](labs/portuguese/lab2/)
**Complete Suite of AI Services**
- **Azure AI Speech**: Recognition, synthesis, and audio translation
- **Azure AI Language + Translator**: NER, sentiment analysis, text processing
- **Azure AI Vision + Document**: OCR, image analysis, document processing
- **Azure AI Content Safety**: Content moderation and safety filtering

### 📝 [Lab 3: Advanced Prompt Engineering](labs/english/lab3/) | [Lab 3: Engenharia de Prompts](labs/portuguese/lab3/)
**Mastering AI Communication**
- Zero-Shot and Few-Shot prompting techniques
- Chain-of-Thought and Tree of Thoughts methodologies
- Meta Prompting and Prompt Chaining strategies
- RAG and Active-Prompt implementations
- Best practices for prompt optimization

### 🔨 [Lab 4: LLM Frameworks - Semantic Kernel, AutoGen, and LangChain](labs/english/lab4/) | [Lab 4: Frameworks de LLM](labs/portuguese/lab4/)
**Professional Development Frameworks**
- **Semantic Kernel**: Microsoft's modular LLM integration framework
- **AutoGen**: Multi-agent conversational systems
- **LangChain**: Comprehensive LLM application components
- Framework comparison and selection guidance

### 🔍 [Lab 5: RAG Implementation with Azure AI Search](labs/english/lab5/) | [Lab 5: Implementação de RAG](labs/portuguese/lab5/)
**Advanced Retrieval and Generation Patterns**
- Complete RAG architecture implementation
- Azure OpenAI and Azure AI Search integration
- Knowledge base creation and optimization
- Advanced techniques: chunking, embedding, reranking

## 🔧 Prerequisites

### Required
- **Azure Subscription**: Active Azure subscription with appropriate permissions
- **Azure AI Foundry Access**: Access to Azure AI Foundry platform
- **Programming Knowledge**: Familiarity with Python (recommended)
- **Development Environment**: VS Code or similar IDE

### Recommended
- **Azure CLI**: For command-line interactions with Azure
- **Git**: For version control and repository management
- **Basic ML Knowledge**: Understanding of machine learning concepts
- **REST API Experience**: Familiarity with API consumption

## 🛠️ Setup Instructions

### 1. Azure Environment Setup
```bash
# Login to Azure
az login

# Set your subscription
az account set --subscription "your-subscription-id"

# Create a resource group for the workshop
az group create --name "ai-foundry-workshop-rg" --location "eastus"
```

### 2. Clone Workshop Materials
```bash
git clone https://github.com/gilbertossoares/ai-foundry-workshop.git
cd ai-foundry-workshop
```

### 3. Environment Configuration
Create a `.env` file in the root directory with the following variables:

```bash
# Azure OpenAI
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_API_VERSION=2024-02-01

# Azure AI Services
SPEECH_ENDPOINT=https://your-region.api.cognitive.microsoft.com/
SPEECH_KEY=your-speech-key
SPEECH_REGION=your-region

LANGUAGE_ENDPOINT=https://your-language-resource.cognitiveservices.azure.com/
LANGUAGE_KEY=your-language-key

VISION_ENDPOINT=https://your-vision-resource.cognitiveservices.azure.com/
VISION_KEY=your-vision-key

CONTENT_SAFETY_ENDPOINT=https://your-content-safety-resource.cognitiveservices.azure.com/
CONTENT_SAFETY_KEY=your-content-safety-key

# Azure AI Search (for Lab 5)
SEARCH_ENDPOINT=https://your-search-service.search.windows.net
SEARCH_KEY=your-search-admin-key
```

## 📖 Detailed Laboratory Content

### 🔧 [Laboratory 1: Azure OpenAI Fundamentals](labs/english/lab1/) | [Laboratório 1: Fundamentos Azure OpenAI](labs/portuguese/lab1/)
**Complete Foundation for AI Development**

**Objectives:**
- Master Azure OpenAI Service configuration and connection
- Understand API structures and response analysis
- Implement embeddings for semantic search and analysis
- Work with multimodal models for image processing
- Explore advanced model capabilities and features

**Key Exercises:**
1. **API Configuration**: Set up Azure OpenAI client and perform first API calls
2. **Response Analysis**: Deep dive into API responses, token usage, and filtering
3. **Embeddings**: Generate text embeddings and understand their applications
4. **Image Processing**: Use multimodal models for image analysis and description
5. **Model Exploration**: Test various LLM models available in Azure AI Foundry

**Advanced Features Covered:**
- Function Calling and tool integration
- Reasoning Models and chain-of-thought
- Structured Outputs and JSON Mode
- Temperature and sampling parameters
- Token optimization strategies

### 🧠 [Laboratory 2: Azure AI Services Ecosystem](labs/english/lab2/) | [Laboratório 2: Ecossistema de Serviços Azure AI](labs/portuguese/lab2/)
**Comprehensive AI Service Integration**

**Objectives:**
- Integrate multiple Azure AI services in unified workflows
- Implement speech recognition and synthesis solutions
- Deploy natural language processing and translation
- Create computer vision and document processing pipelines
- Establish content safety and moderation systems

**Service Categories:**
1. **Speech Services**: Audio transcription, voice synthesis, real-time translation
2. **Language Services**: NER, sentiment analysis, key phrase extraction, translation
3. **Vision Services**: OCR, image analysis, face detection, document processing
4. **Content Safety**: Harmful content detection, prompt injection protection

**Real-World Applications:**
- Automated transcription and subtitle generation
- Multi-language document processing
- Content moderation for user-generated content
- Accessibility solutions with speech and vision

### 📝 [Laboratory 3: Advanced Prompt Engineering](labs/english/lab3/) | [Laboratório 3: Engenharia de Prompts Avançada](labs/portuguese/lab3/)
**Mastering AI Communication and Optimization**

**Objectives:**
- Master fundamental and advanced prompting techniques
- Implement systematic approaches to prompt optimization
- Develop strategies for complex reasoning tasks
- Create adaptive and context-aware prompting systems

**Techniques Covered:**
1. **Zero-Shot Prompting**: Effective instructions without examples
2. **Few-Shot Prompting**: Learning from targeted examples
3. **Chain-of-Thought**: Step-by-step reasoning encouragement
4. **Meta Prompting**: Instructions about instruction following
5. **Prompt Chaining**: Breaking complex tasks into sequences
6. **Tree of Thoughts**: Multiple reasoning path exploration
7. **RAG Integration**: External knowledge incorporation
8. **Active Prompting**: Dynamic adaptation based on context

**Best Practices Framework:**
- Specificity and clarity in instruction design
- Strategic use of examples and analogies
- Importance of prompt structure and ordering
- Fallback strategies and error handling

### 🔨 [Laboratory 4: Professional LLM Frameworks](labs/english/lab4/) | [Laboratório 4: Frameworks Profissionais de LLM](labs/portuguese/lab4/)
**Enterprise-Grade Development Patterns**

**Objectives:**
- Compare and select appropriate LLM frameworks
- Implement modular and scalable AI solutions
- Create multi-agent systems and workflows
- Integrate LLMs with existing enterprise systems

**Framework Deep Dive:**
1. **Semantic Kernel**:
   - Microsoft's enterprise framework for LLM integration
   - Plugin architecture and function composition
   - Memory management and semantic operations
   - .NET and Python ecosystem integration

2. **AutoGen**:
   - Multi-agent conversational systems
   - Role-based agent design and interaction
   - Automated workflow orchestration
   - Human-in-the-loop integration patterns

3. **LangChain**:
   - Comprehensive component library
   - Chain composition and workflow management
   - External tool and API integration
   - Document processing and retrieval systems

**Architecture Considerations:**
- Framework selection criteria
- Performance and scalability factors
- Integration complexity assessment
- Maintenance and support considerations

### 🔍 [Laboratory 5: Production RAG Implementation](labs/english/lab5/) | [Laboratório 5: Implementação RAG em Produção](labs/portuguese/lab5/)
**Advanced Information Retrieval and Generation**

**Objectives:**
- Implement production-ready RAG architectures
- Optimize retrieval accuracy and generation quality
- Design scalable knowledge management systems
- Deploy and monitor RAG solutions in Azure

**Complete Implementation:**
1. **Knowledge Base Creation**: Document ingestion, chunking, and indexing
2. **Search Integration**: Azure AI Search configuration and optimization
3. **Retrieval Pipeline**: Query processing and document ranking
4. **Generation Pipeline**: Context integration and response synthesis
5. **Evaluation Framework**: Quality metrics and continuous improvement

**Advanced Techniques:**
- Semantic chunking strategies
- Embedding model selection and fine-tuning
- Query expansion and rewriting
- Result reranking and filtering
- Cache strategies for performance optimization

**Production Considerations:**
- Scalability and performance monitoring
- Cost optimization strategies
- Security and access control
- Update and maintenance workflows

## 🎯 Learning Progression and Outcomes

### Recommended Learning Path

**🟢 Beginner Track (Labs 1-2)**
- Perfect for those new to AI and Azure services
- Covers fundamental concepts and basic implementations
- Provides hands-on experience with core Azure AI services
- Estimated completion time: 8-12 hours

**🟡 Intermediate Track (Labs 1-3)**
- Builds on fundamentals with advanced prompt engineering
- Introduces optimization techniques and best practices
- Covers systematic approaches to AI solution design
- Estimated completion time: 12-16 hours

**🔴 Advanced Track (Labs 1-5)**
- Complete workshop covering enterprise patterns
- Includes framework evaluation and production deployment
- Focuses on scalable and maintainable AI solutions
- Estimated completion time: 20-25 hours

**🎖️ Specialist Focus**
- Choose specific labs based on immediate needs
- Can be completed independently with prerequisite knowledge
- Ideal for targeting specific skills or technologies

### Learning Outcomes by Laboratory

**After Lab 1, you will:**
✅ Configure and use Azure OpenAI Service effectively
✅ Understand API structures and response optimization
✅ Generate and apply embeddings for semantic tasks
✅ Process images with multimodal AI models
✅ Navigate Azure AI Foundry platform confidently

**After Lab 2, you will:**
✅ Integrate multiple Azure AI services in workflows
✅ Implement speech and language processing solutions
✅ Deploy computer vision and document analysis
✅ Establish content safety and moderation systems
✅ Design comprehensive AI service architectures

**After Lab 3, you will:**
✅ Master advanced prompt engineering techniques
✅ Optimize AI model interactions systematically
✅ Implement complex reasoning and chaining patterns
✅ Design adaptive and context-aware AI systems
✅ Apply prompt engineering best practices consistently

**After Lab 4, you will:**
✅ Select and implement appropriate LLM frameworks
✅ Build modular and scalable AI applications
✅ Create multi-agent systems and workflows
✅ Integrate AI solutions with enterprise systems
✅ Compare framework capabilities and trade-offs

**After Lab 5, you will:**
✅ Implement production-ready RAG architectures
✅ Optimize information retrieval and generation quality
✅ Design scalable knowledge management systems
✅ Deploy and monitor AI solutions in production
✅ Apply advanced techniques for performance optimization

## 🔒 Security & Best Practices

This workshop follows Azure security and AI best practices:

### Security Framework
- **Managed Identity**: All examples use managed identity for authentication
- **Key Vault Integration**: Secure storage of secrets and connection strings
- **RBAC**: Proper role-based access control configuration
- **Network Security**: Virtual network integration where applicable
- **Data Privacy**: Compliance with data protection regulations

### Responsible AI Implementation
- **Fairness**: Bias detection and mitigation strategies
- **Reliability & Safety**: Error handling and graceful degradation
- **Transparency**: Explainable AI and decision traceability
- **Accountability**: Audit trails and governance frameworks
- **Privacy**: Data minimization and protection techniques
- **Inclusiveness**: Accessibility and diverse user consideration

### Operational Excellence
- **Monitoring**: Comprehensive logging and alerting
- **Performance**: Optimization for cost and speed
- **Scalability**: Design for growth and demand fluctuation
- **Maintainability**: Code quality and documentation standards
- **Compliance**: Regulatory and organizational requirement adherence

## 🆘 Troubleshooting & Support

### Common Issues and Solutions

**🔴 Access and Permission Issues**
- **Azure Subscription Access**: Ensure your account has Contributor or Owner role
- **AI Service Quotas**: Check service quotas in your Azure region
- **API Key Configuration**: Verify endpoint URLs and API keys in `.env` file
- **Resource Availability**: Confirm services are available in your selected region

**🟡 Technical Configuration Issues**
- **Python Environment**: Use Python 3.8+ with virtual environment
- **Package Dependencies**: Install requirements.txt files for each lab
- **Network Connectivity**: Check firewall and proxy settings
- **Jupyter Notebooks**: Ensure proper kernel selection in notebook environment

**🟢 Performance and Optimization**
- **API Rate Limits**: Implement retry logic and respect rate limiting
- **Token Optimization**: Monitor token usage and implement efficient prompting
- **Cost Management**: Set up billing alerts and optimize service tiers
- **Response Times**: Consider caching strategies and service regions

### Getting Help and Support

**📖 Documentation Resources**
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure OpenAI Service Guide](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure AI Services Documentation](https://learn.microsoft.com/azure/ai-services/)
- [Troubleshooting Guide](https://learn.microsoft.com/azure/ai-services/openai/troubleshooting)

**🤝 Community Support**
- [Microsoft Tech Community - Azure AI](https://techcommunity.microsoft.com/category/azure-ai)
- [Stack Overflow - Azure AI Tags](https://stackoverflow.com/questions/tagged/azure-ai)
- [GitHub Issues for Workshop-Specific Problems](https://github.com/gilbertossoares/ai-foundry-workshop/issues)
- [Azure Support Plans](https://azure.microsoft.com/support/plans/) for enterprise customers

**🔧 Self-Help Tools**
- Azure Portal Resource Health checker
- Azure Service Health status page
- Azure CLI diagnostic commands
- Log Analytics for service monitoring

## 📋 Prerequisites Checklist

Before starting the workshop, ensure you have completed:

### Azure Environment
- [ ] Active Azure subscription with sufficient credits/budget
- [ ] Access to Azure AI Foundry platform
- [ ] Resource group created for workshop resources
- [ ] Required service quotas available in target region
- [ ] Billing alerts configured (recommended)

### Development Environment
- [ ] Python 3.8+ installed with pip and virtual environment support
- [ ] Visual Studio Code or preferred IDE configured
- [ ] Git installed for repository management
- [ ] Azure CLI installed and configured
- [ ] Workshop repository cloned locally

### Service Configuration
- [ ] Azure OpenAI Service provisioned with required models
- [ ] Azure AI Speech Service created
- [ ] Azure AI Language Service configured
- [ ] Azure AI Vision Service available
- [ ] Azure AI Content Safety Service set up
- [ ] Azure AI Search Service created (for Lab 5)

### Environment Variables
- [ ] `.env` file created with all required credentials
- [ ] All endpoint URLs and API keys configured
- [ ] Environment variables tested and validated
- [ ] Backup of credentials stored securely

## 🌟 Advanced Learning Path

### After Completing This Workshop

**🚀 Immediate Next Steps**
- Implement a custom AI solution using learned techniques
- Explore Azure AI Foundry's latest features and updates
- Join the Azure AI developer community
- Begin working on Azure AI certification paths

**📚 Continuous Learning Resources**
- [Microsoft Learn - AI Learning Paths](https://learn.microsoft.com/training/browse/?products=azure-cognitive-services)
- [Azure AI Foundry Release Notes](https://learn.microsoft.com/azure/ai-foundry/whats-new)
- [AI/ML Research Papers and Updates](https://arxiv.org/list/cs.AI/recent)
- [Microsoft AI Blog](https://blogs.microsoft.com/ai/)

**🎯 Certification Preparation**
- [AI-102: Designing and Implementing an Azure AI Solution](https://learn.microsoft.com/certifications/azure-ai-engineer/)
- [AI-900: Microsoft Azure AI Fundamentals](https://learn.microsoft.com/certifications/azure-ai-fundamentals/)
- [DP-100: Designing and Implementing a Data Science Solution on Azure](https://learn.microsoft.com/certifications/azure-data-scientist/)

**🛠️ Practical Projects Ideas**
- Build an intelligent document processing system
- Create a multilingual customer service chatbot
- Implement a content recommendation engine
- Develop a real-time sentiment analysis dashboard
- Design an automated content moderation system

## 🤝 Contributing to This Workshop

We welcome contributions to improve this workshop experience!

### How to Contribute
1. **Fork the Repository**: Create your own copy of the workshop
2. **Create Feature Branch**: Develop improvements in isolated branches
3. **Follow Standards**: Maintain code quality and documentation standards
4. **Test Thoroughly**: Ensure all examples work as expected
5. **Submit Pull Request**: Provide clear description of improvements

### Areas for Contribution
- **New Exercises**: Additional hands-on scenarios and use cases
- **Language Support**: Translations and localization improvements
- **Bug Fixes**: Error corrections and clarifications
- **Documentation**: Enhanced explanations and tutorials
- **Performance Optimization**: Improved efficiency and best practices

### Community Guidelines
- Be respectful and constructive in feedback
- Follow Microsoft's Code of Conduct
- Maintain focus on educational value
- Ensure accessibility in all contributions
- Test contributions across different environments

## 🌟 Workshop Success Outcomes

By the end of this comprehensive workshop, you will have achieved:

### 🎯 Technical Mastery
✅ **Azure AI Platform Expertise**: Navigate and utilize Azure AI Foundry effectively for enterprise AI development
✅ **API Integration Skills**: Master Azure OpenAI and other AI service APIs for production applications
✅ **Prompt Engineering Proficiency**: Design and optimize prompts for maximum effectiveness and reliability
✅ **Framework Implementation**: Select and implement appropriate LLM frameworks for different use cases
✅ **RAG Architecture Deployment**: Build and deploy production-ready retrieval-augmented generation systems
✅ **Multi-Service Integration**: Combine multiple Azure AI services in cohesive, scalable solutions

### 🛠️ Practical Capabilities
✅ **End-to-End AI Solutions**: Design, implement, and deploy complete AI applications
✅ **Performance Optimization**: Optimize AI systems for cost, speed, and accuracy
✅ **Security Implementation**: Apply security best practices and responsible AI principles
✅ **Production Deployment**: Deploy AI solutions with monitoring and maintenance strategies
✅ **Troubleshooting Skills**: Diagnose and resolve common AI implementation challenges
✅ **Documentation and Testing**: Create maintainable, well-documented AI solutions

### 🎓 Strategic Understanding
✅ **Technology Selection**: Make informed decisions about AI technologies and architectures
✅ **Business Application**: Identify and implement AI solutions for real business problems
✅ **Cost Management**: Understand and optimize costs for AI service consumption
✅ **Compliance and Governance**: Implement AI solutions that meet regulatory requirements
✅ **Future-Proofing**: Design solutions that can evolve with advancing AI technologies

## 📚 Comprehensive Resource Library

### Official Microsoft Documentation
- [Azure AI Foundry Platform Guide](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure AI Services Overview](https://learn.microsoft.com/azure/ai-services/)
- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
- [Responsible AI Framework](https://www.microsoft.com/ai/responsible-ai)

### Advanced Learning Resources
- [Azure Architecture Center - AI Solutions](https://learn.microsoft.com/azure/architecture/browse/?terms=ai)
- [AI Builder and Power Platform Integration](https://learn.microsoft.com/ai-builder/)
- [Azure Machine Learning Documentation](https://learn.microsoft.com/azure/machine-learning/)
- [Cognitive Services REST API Reference](https://learn.microsoft.com/rest/api/cognitiveservices/)

### Community and Support
- [Microsoft Tech Community - Azure AI](https://techcommunity.microsoft.com/category/azure-ai)
- [Azure AI Developer Blog](https://techcommunity.microsoft.com/category/azure-ai/blog)
- [GitHub - Azure AI Samples](https://github.com/Azure-Samples/cognitive-services-quickstart-code)
- [Stack Overflow - Azure AI Community](https://stackoverflow.com/questions/tagged/azure-ai)

### Training and Certification
- [Microsoft Learn - AI Learning Paths](https://learn.microsoft.com/training/browse/?products=azure-cognitive-services)
- [Azure AI Fundamentals (AI-900)](https://learn.microsoft.com/certifications/azure-ai-fundamentals/)
- [Azure AI Engineer Associate (AI-102)](https://learn.microsoft.com/certifications/azure-ai-engineer/)
- [Azure Data Scientist Associate (DP-100)](https://learn.microsoft.com/certifications/azure-data-scientist/)

## 📄 License and Usage

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for complete details.

### Usage Rights
- ✅ Commercial use permitted
- ✅ Modification and distribution allowed
- ✅ Private use encouraged
- ✅ Educational and training use supported

### Attribution Requirements
- Include original license and copyright notice
- Acknowledge Microsoft and workshop contributors
- Maintain links to original repository

## 👥 Authors and Acknowledgments

### Workshop Development Team
This workshop was created by the Azure AI team and community contributors, with special recognition to:

- **Microsoft Azure AI Engineering Team**: Core content development and technical validation
- **Community Contributors**: Feedback, testing, and continuous improvement
- **Documentation Team**: Comprehensive guides and troubleshooting resources
- **Translation Team**: Multi-language support and localization

### Special Thanks
We extend our gratitude to all who have contributed to making this educational resource available, including:
- Beta testers who provided valuable feedback
- Community members who reported issues and suggested improvements
- Microsoft Learn team for documentation and learning path support
- Open source community for framework examples and best practices

---

## 🚀 Ready to Begin Your AI Journey?

**Choose your preferred language and start exploring the cutting-edge world of Azure AI:**

### 🇺🇸 English Workshop Materials
**[Begin English Workshop →](./labs/english/)**
- Complete step-by-step laboratories
- Comprehensive documentation and examples
- Advanced implementation guides
- Community support and resources

### 🇧🇷 Materiais em Português Brasileiro
**[Iniciar Workshop em Português →](./labs/portuguese/)**
- Laboratórios passo a passo completos
- Documentação abrangente e exemplos práticos
- Guias de implementação avançada
- Suporte da comunidade e recursos

---

**🌟 Transform your understanding of AI and unlock the full potential of Azure AI Foundry. Start your journey today!**