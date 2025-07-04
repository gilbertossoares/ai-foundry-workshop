# Configuração do Ambiente - Azure AI Foundry Workshop

Este arquivo contém as instruções para configurar o ambiente Python necessário para executar todos os laboratórios do Azure AI Foundry Workshop.

## Pré-requisitos

- Python 3.8 ou superior
- Conta Azure com acesso aos serviços de IA
- Azure OpenAI Service configurado
- Azure AI Search configurado (para Lab 5)

## Instalação das Dependências

### Opção 1: Instalação Completa (Recomendada)
```bash
pip install -r requirements.txt
```

### Opção 2: Instalação por Laboratório

#### Lab 1 - Conexão e Primeiros Passos
```bash
pip install openai azure-ai-inference python-dotenv numpy
```

#### Lab 2 - Serviços de IA
```bash
pip install azure-cognitiveservices-speech azure-ai-textanalytics azure-ai-vision-imageanalysis azure-ai-formrecognizer azure-ai-contentsafety azure-core python-dotenv
```

#### Lab 3 - Prompt Engineering
```bash
pip install openai python-dotenv
```

#### Lab 4 - Semantic Kernel e AutoGen
```bash
pip install semantic-kernel autogen-agentchat autogen-ext[openai,azure] python-dotenv asyncio typing-extensions
```

#### Lab 5 - RAG (Retrieval-Augmented Generation)
```bash
pip install openai azure-search-documents azure-core python-dotenv numpy
```

## Configuração das Variáveis de Ambiente

### ⚠️ IMPORTANTE - Segurança

**NUNCA** commite arquivos contendo chaves de API ou secrets reais no GitHub ou outros repositórios públicos. Sempre use o arquivo `.env.example` como template e configure suas próprias credenciais em um arquivo `.env` local.

### Passos para Configuração Segura

1. **Copie o arquivo de exemplo:**
   ```bash
   cp .env.example .env
   ```

2. **Edite o arquivo `.env` com suas credenciais reais:**
   - Substitua todos os valores `your-*` pelos valores reais dos seus recursos Azure
   - Mantenha este arquivo sempre local (ele já está no .gitignore)

3. **Para desenvolvimento em equipe:**
   - Compartilhe apenas o arquivo `.env.example`
   - Cada desenvolvedor deve criar seu próprio arquivo `.env`
   - Documente onde obter as credenciais (ex: Azure Portal, Key Vault)

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_EMBEDDING_MODEL=text-embedding-3-small
API_VERSION=2024-02-01

# Azure AI Services (Lab 2)
AZURE_LANGUAGE_ENDPOINT=https://your-language-resource.cognitiveservices.azure.com/
AZURE_LANGUAGE_KEY=your-language-key
AZURE_VISION_ENDPOINT=https://your-vision-resource.cognitiveservices.azure.com/
AZURE_VISION_KEY=your-vision-key
SPEECH_ENDPOINT=https://your-speech-resource.cognitiveservices.azure.com/
SPEECH_KEY=your-speech-key
SPEECH_REGION=your-region
DOC_INTELLIGENCE_ENDPOINT=https://your-doc-intelligence.cognitiveservices.azure.com/
DOC_INTELLIGENCE_KEY=your-doc-intelligence-key
CONTENT_SAFETY_ENDPOINT=https://your-content-safety.cognitiveservices.azure.com/
CONTENT_SAFETY_KEY=your-content-safety-key

# Azure AI Foundry Model Catalog (Lab 1)
AZURE_PHI4_ENDPOINT=https://your-phi4-endpoint.region.models.ai.azure.com/
AZURE_PHI4_API_KEY=your-phi4-api-key
AZURE_PHI4_DEPLOYMENT=phi-4
AZURE_PHI4_API_VERSION=2024-04-01-preview

# Azure AI Search (Lab 5)
AZURE_SEARCH_ENDPOINT=https://your-search-service.search.windows.net
AZURE_SEARCH_KEY=your-search-key
AZURE_SEARCH_INDEX=rag-index
```

## Verificação da Instalação

Para verificar se tudo está instalado corretamente, execute:

```python
import openai
import azure.cognitiveservices.speech as speechsdk
import azure.ai.textanalytics
import azure.ai.vision.imageanalysis
import azure.ai.formrecognizer
import azure.ai.contentsafety
import azure.search.documents
import semantic_kernel
import autogen_agentchat
import numpy as np
import pandas as pd
from dotenv import load_dotenv

print("✅ Todas as dependências estão instaladas corretamente!")
```

## Solução de Problemas

### Erro de Instalação do AutoGen
Se houver problemas com autogen, tente:
```bash
pip install --upgrade pip
pip install autogen-agentchat[openai] autogen-ext[openai,azure]
```

### Erro de Versão do Python
Alguns pacotes requerem Python 3.8+. Verifique sua versão:
```bash
python --version
```

### Conflitos de Dependências
Se houver conflitos, use um ambiente virtual:
```bash
python -m venv azure-ai-env
source azure-ai-env/bin/activate  # Linux/Mac
azure-ai-env\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Arquivos de Exemplo

Os laboratórios utilizam arquivos de exemplo localizados em:
- `samples/234039841.jpg` - Imagem para análise de visão
- `samples/audio001.wav` - Áudio para reconhecimento de fala
- `samples/car-accident.png` - Imagem para análise avançada
- `samples/placa.jpg` - Documento para análise de texto

## Suporte

Se você encontrar problemas:
1. Verifique se todas as variáveis de ambiente estão configuradas
2. Confirme que os recursos Azure estão provisionados
3. Verifique se as chaves de API estão corretas e não expiraram
4. Confirme que a versão do Python é compatível

## Próximos Passos

1. Configure o arquivo `.env` com suas credenciais
2. Execute `pip install -r requirements.txt`
3. Teste a configuração executando o Lab 1
4. Prossiga com os laboratórios em ordem sequencial

---

**Nota**: Este workshop foi projetado para funcionar com Azure AI Foundry e os serviços Azure AI mais recentes. Algumas funcionalidades podem estar em preview.
