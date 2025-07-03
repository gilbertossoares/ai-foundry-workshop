#!/usr/bin/env python3
"""
Script de verificação do ambiente para Azure AI Foundry Workshop
Verifica se todas as dependências estão instaladas e as configurações estão corretas
"""

import sys
import os
import importlib
from dotenv import load_dotenv

def check_python_version():
    """Verifica a versão do Python"""
    print("🔍 Verificando versão do Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Requer Python 3.8+")
        return False

def check_package(package_name, description=""):
    """Verifica se um pacote está instalado"""
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name} {description}")
        return True
    except ImportError:
        print(f"❌ {package_name} {description} - NÃO INSTALADO")
        return False

def check_packages():
    """Verifica todos os pacotes necessários"""
    print("\n🔍 Verificando dependências...")
    
    packages = [
        ("openai", "- Azure OpenAI SDK"),
        ("azure.ai.inference", "- Azure AI Inference"),
        ("azure.cognitiveservices.speech", "- Speech Services"),
        ("azure.ai.textanalytics", "- Text Analytics"),
        ("azure.ai.vision.imageanalysis", "- Vision Analysis"),
        ("azure.ai.formrecognizer", "- Form Recognizer"),
        ("azure.ai.contentsafety", "- Content Safety"),
        ("azure.search.documents", "- Azure Search"),
        ("semantic_kernel", "- Semantic Kernel"),
        ("autogen_agentchat", "- AutoGen"),
        ("numpy", "- NumPy"),
        ("pandas", "- Pandas"),
        ("dotenv", "- Python Dotenv"),
    ]
    
    success_count = 0
    for package, description in packages:
        if check_package(package, description):
            success_count += 1
    
    print(f"\n📊 Resultado: {success_count}/{len(packages)} pacotes instalados")
    return success_count == len(packages)

def check_env_variables():
    """Verifica se as variáveis de ambiente estão configuradas"""
    print("\n🔍 Verificando configurações de ambiente...")
    
    # Tentar carregar o arquivo .env
    if os.path.exists('.env'):
        load_dotenv()
        print("✅ Arquivo .env encontrado")
    else:
        print("⚠️  Arquivo .env não encontrado - usando variáveis do sistema")
    
    # Variáveis obrigatórias
    required_vars = [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY", 
        "AZURE_OPENAI_DEPLOYMENT",
        "API_VERSION"
    ]
    
    # Variáveis opcionais por lab
    optional_vars = {
        "Lab 2": [
            "AZURE_LANGUAGE_ENDPOINT",
            "AZURE_LANGUAGE_KEY",
            "AZURE_VISION_ENDPOINT", 
            "AZURE_VISION_KEY",
            "SPEECH_KEY",
            "SPEECH_REGION"
        ],
        "Lab 5": [
            "AZURE_SEARCH_ENDPOINT",
            "AZURE_SEARCH_KEY"
        ]
    }
    
    # Verificar variáveis obrigatórias
    missing_required = []
    for var in required_vars:
        value = os.getenv(var)
        if value and value.strip():
            print(f"✅ {var}")
        else:
            print(f"❌ {var} - NÃO CONFIGURADO")
            missing_required.append(var)
    
    # Verificar variáveis opcionais
    for lab, vars_list in optional_vars.items():
        print(f"\n{lab} (opcional):")
        for var in vars_list:
            value = os.getenv(var)
            if value and value.strip():
                print(f"  ✅ {var}")
            else:
                print(f"  ⚠️  {var} - não configurado")
    
    if missing_required:
        print(f"\n❌ Variáveis obrigatórias não configuradas: {', '.join(missing_required)}")
        return False
    else:
        print("\n✅ Todas as variáveis obrigatórias estão configuradas")
        return True

def check_sample_files():
    """Verifica se os arquivos de exemplo existem"""
    print("\n🔍 Verificando arquivos de exemplo...")
    
    sample_files = [
        "samples/234039841.jpg",
        "samples/audio001.wav", 
        "samples/car-accident.png",
        "samples/placa.jpg"
    ]
    
    found_files = 0
    for file_path in sample_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
            found_files += 1
        else:
            print(f"❌ {file_path} - não encontrado")
    
    print(f"\n📊 Arquivos encontrados: {found_files}/{len(sample_files)}")
    return found_files == len(sample_files)

def test_azure_openai_connection():
    """Testa a conexão com Azure OpenAI"""
    print("\n🔍 Testando conexão com Azure OpenAI...")
    
    try:
        from openai import AzureOpenAI
        
        client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("API_VERSION")
        )
        
        # Teste simples
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {"role": "user", "content": "Diga apenas 'Conexão OK'"}
            ],
            max_tokens=10
        )
        
        if response.choices[0].message.content:
            print("✅ Conexão com Azure OpenAI - OK")
            return True
        else:
            print("❌ Conexão com Azure OpenAI - Falhou")
            return False
            
    except Exception as e:
        print(f"❌ Erro na conexão com Azure OpenAI: {str(e)}")
        return False

def main():
    """Função principal"""
    print("🚀 Azure AI Foundry Workshop - Verificação de Ambiente")
    print("="*60)
    
    checks = [
        check_python_version(),
        check_packages(),
        check_env_variables(),
        check_sample_files(),
        test_azure_openai_connection()
    ]
    
    print("\n" + "="*60)
    print("📋 RESUMO FINAL")
    print("="*60)
    
    if all(checks):
        print("🎉 SUCESSO! O ambiente está configurado corretamente.")
        print("✅ Você pode executar todos os laboratórios.")
        print("\n📚 Próximos passos:")
        print("1. Abra o Lab 1 para começar")
        print("2. Execute as células em ordem")
        print("3. Prossiga com os demais labs")
    else:
        print("⚠️  ATENÇÃO! Alguns problemas foram encontrados.")
        print("📋 Ações recomendadas:")
        print("1. Instale as dependências: pip install -r requirements.txt")
        print("2. Configure o arquivo .env com suas credenciais")
        print("3. Execute novamente este script")
        print("4. Consulte o arquivo SETUP.md para mais detalhes")
    
    print("\n💡 Para suporte adicional, consulte o arquivo SETUP.md")

if __name__ == "__main__":
    main()
