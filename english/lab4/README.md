# Lab 4: LLM Frameworks - Developing with Semantic Kernel, AutoGen and LangChain

> **⚠️ Note**: This laboratory is under development. The `lab4.ipynb` notebook will be available soon with practical exercises.

This laboratory presents an overview of the main frameworks for developing applications with Large Language Models (LLMs), such as Semantic Kernel, AutoGen and LangChain. These frameworks provide tools and abstractions to facilitate the integration and orchestration of LLMs in applications.

## Learning Objectives

- Understand the purpose and use cases of each framework
- Explore basic implementation examples with each technology
- Compare the approaches of different frameworks
- Develop a mini-project using one of the frameworks

## Prerequisites

- Basic Python knowledge
- Familiarity with LLM concepts
- Configured Python development environment
- API keys for Azure OpenAI Service

## LLM Frameworks

### Semantic Kernel

Semantic Kernel is an open-source framework developed by Microsoft that allows integrating LLMs into applications in a modular and structured way.

#### Basic Example with Semantic Kernel

```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion

# Initialize the kernel
kernel = sk.Kernel()

# Configure AI service
deployment_name = "text-davinci-003"
endpoint = "https://your-endpoint.openai.azure.com/"
api_key = "your-api-key"

# Add the AI service to the kernel
kernel.add_text_completion_service("demoservice", 
                                  AzureTextCompletion(deployment_name, endpoint, api_key))

# Create a semantic function
prompt_config = sk.PromptTemplateConfig.from_completion_parameters(
    max_tokens=2000,
    temperature=0.7,
    top_p=0.8
)

prompt_template = """
Summarize the following text in 3 main points:
{{$input}}
"""

summary_function = kernel.create_semantic_function(
    prompt_template, 
    prompt_config, 
    "summarize", 
    "summary"
)

# Execute the function
text = "..."  # Long text here
summary = summary_function(text)
print(summary)
```

### AutoGen

AutoGen is a framework that allows creating, using and optimizing AI agents that can converse with each other to solve tasks. Developed by Microsoft, it facilitates the creation of multi-agent flows.

#### Basic Example with AutoGen

```python
import autogen

# Configure the models
config_list = [
    {
        "model": "gpt-4",
        "api_key": "your-api-key",
    }
]

# Create agents
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
)

# Start conversation between agents
user_proxy.initiate_chat(
    assistant,
    message="Create a Python function that calculates Fibonacci numbers up to n."
)
```

### LangChain

LangChain is a popular framework for developing LLM-based applications, offering components to handle documents, memory, agents and processing chains.

#### Basic Example with LangChain

```python
from langchain.llms import AzureOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Configure the LLM
llm = AzureOpenAI(
    deployment_name="text-davinci-003",
    model_name="text-davinci-003",
    openai_api_key="your-api-key",
    openai_api_base="https://your-endpoint.openai.azure.com/",
    openai_api_version="2022-12-01"
)

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["product"],
    template="Write an attractive description for the product: {product}"
)

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Execute the chain
result = chain.run("Programmable coffee maker")
print(result)
```

## Framework Comparison

| Framework | Strengths | Ideal Use Cases |
|-----------|-----------|----------------|
| Semantic Kernel | .NET ecosystem integration, plugin architecture, semantic memory | Enterprise applications, Microsoft solutions, complex integrations |
| AutoGen | Conversational agents, multi-agent flows, flexibility | Task automation, collaborative systems, rapid prototype development |
| LangChain | Large community, various ready-made components, robust documentation | Data retrieval (RAG), chatbots, task-specific agents |

## Practical Exercise

Choose one of the presented frameworks and implement a simple application that:

1. Loads a text document
2. Extracts relevant information
3. Generates a summary based on the extracted information
4. Answers questions about the content

## Next Steps

- Explore open-source projects that use these frameworks
- Experiment with combining different frameworks in a single project
- Implement a specialized agent for your business domain
- Explore production deployment options with Azure

## Additional Resources

- [Semantic Kernel Documentation](https://github.com/microsoft/semantic-kernel)
- [AutoGen Documentation](https://github.com/microsoft/autogen)
- [LangChain Documentation](https://langchain.readthedocs.io/)
- [Azure AI Studio](https://azure.microsoft.com/services/ai-studio/)
- [Advanced RAG Building Course](https://learn.microsoft.com/training/)
