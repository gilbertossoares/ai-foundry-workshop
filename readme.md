# Azure AI Foundry Workshop

Welcome to the Azure AI Foundry Workshop! This comprehensive hands-on workshop will guide you through the latest capabilities of Azure AI Foundry, Microsoft's unified platform for building, deploying, and managing AI applications.

## 🎯 Workshop Overview

Azure AI Foundry provides a collaborative environment for AI development, offering tools for data preparation, model training, fine-tuning, evaluation, and deployment. This workshop covers everything from getting started to advanced scenarios.

## 📚 Available Languages

This workshop is available in multiple languages:

- **English**: `/english/` - Complete workshop materials in English
- **Português (Brasil)**: `/portuguese/` - Materiais completos do workshop em português brasileiro

## 🚀 What You'll Learn

- **Azure AI Foundry Fundamentals**: Understanding the platform architecture and core concepts
- **Project Setup**: Creating and configuring AI projects in Azure AI Foundry
- **Data Management**: Working with datasets, data flows, and data preparation
- **Model Development**: Building, training, and fine-tuning AI models
- **Model Evaluation**: Testing and validating model performance
- **Deployment Strategies**: Deploying models to various endpoints and environments
- **Monitoring & MLOps**: Implementing continuous integration and monitoring for AI applications
- **Security & Governance**: Best practices for secure AI development
- **Integration Patterns**: Connecting AI models with applications and services

## 🔧 Prerequisites

Before starting this workshop, ensure you have:

### Required
- **Azure Subscription**: Active Azure subscription with appropriate permissions
- **Azure AI Foundry Access**: Access to Azure AI Foundry (preview)
- **Basic Programming Knowledge**: Familiarity with Python or .NET
- **Git**: For cloning and managing workshop materials

### Recommended
- **Visual Studio Code**: With Python and Azure extensions
- **Azure CLI**: For command-line interactions with Azure
- **Docker**: For containerized deployments (optional)
- **Postman or similar**: For API testing

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
git clone https://github.com/your-repo/ai-foundry-workshop.git
cd ai-foundry-workshop
```

### 3. Environment Configuration
- Follow the language-specific setup instructions in your chosen language folder
- Configure Azure credentials and permissions
- Verify access to Azure AI Foundry

## 📖 Workshop Structure

### Module 1: Introduction to Azure AI Foundry
- Platform overview and architecture
- Creating your first project
- Understanding workspaces and resources

### Module 2: Data Management
- Data ingestion and preparation
- Working with Azure Data Lake and databases
- Data versioning and lineage

### Module 3: Model Development
- Building models with Azure AI Foundry
- Using pre-built models and APIs
- Custom model training and fine-tuning

### Module 4: Model Evaluation & Testing
- Performance metrics and evaluation
- A/B testing strategies
- Responsible AI practices

### Module 5: Deployment & Integration
- Model deployment options
- API endpoints and integration
- Scaling and performance optimization

### Module 6: MLOps & Monitoring
- CI/CD pipelines for AI
- Model monitoring and drift detection
- Automated retraining workflows

### Module 7: Advanced Scenarios
- Multi-modal AI applications
- RAG (Retrieval-Augmented Generation) patterns
- Agent-based architectures

## 🔒 Security & Best Practices

This workshop follows Azure security best practices:

- **Managed Identity**: All examples use managed identity for authentication
- **Key Vault Integration**: Secure storage of secrets and connection strings
- **RBAC**: Proper role-based access control configuration
- **Network Security**: Virtual network integration where applicable
- **Compliance**: Following responsible AI and governance guidelines

## 🆘 Troubleshooting

### Common Issues
- **Access denied errors**: Verify Azure subscription permissions and AI Foundry access
- **Resource quota limits**: Check Azure quotas for AI services in your region
- **Network connectivity**: Ensure proper firewall and network configuration

### Getting Help
- Check the troubleshooting guide in your language-specific folder
- Review Azure AI Foundry documentation
- Open an issue in this repository for workshop-specific problems

## 📋 Prerequisites Checklist

Before starting, ensure you have completed:

- [ ] Azure subscription with AI services access
- [ ] Azure AI Foundry access (preview sign-up if required)
- [ ] Development environment setup (VS Code, Python/CLI tools)
- [ ] Workshop materials cloned locally
- [ ] Azure CLI configured with your subscription
- [ ] Required Azure resources provisioned

## 🌟 Workshop Outcomes

By the end of this workshop, you will be able to:

- ✅ Navigate and use Azure AI Foundry effectively
- ✅ Build end-to-end AI solutions using the platform
- ✅ Implement proper MLOps practices
- ✅ Deploy and monitor AI models in production
- ✅ Apply security and governance best practices
- ✅ Integrate AI capabilities into existing applications

## 📚 Additional Resources

- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-foundry)
- [Azure AI Services Documentation](https://docs.microsoft.com/azure/cognitive-services)
- [Azure Machine Learning Documentation](https://docs.microsoft.com/azure/machine-learning)
- [Responsible AI Guidelines](https://www.microsoft.com/ai/responsible-ai)
- [Azure Architecture Center - AI Solutions](https://docs.microsoft.com/azure/architecture/browse/?terms=ai)

## 🤝 Contributing

We welcome contributions to improve this workshop! Please:

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request with a clear description

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors & Acknowledgments

This workshop was created by the Azure AI team and community contributors. Special thanks to all who have contributed to making this resource available.

---

**Ready to start?** Choose your preferred language folder and begin your Azure AI Foundry journey!

🇺🇸 [English Workshop Materials](./english/)  
🇧🇷 [Materiais em Português](./portuguese/)