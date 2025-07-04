#!/usr/bin/env python3
"""
Environment verification script for Azure AI Foundry Workshop
Checks if all dependencies are installed and configurations are correct
"""

import sys
import os
import importlib
from dotenv import load_dotenv

def check_python_version():
    """Check Python version"""
    print("🔍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.8+")
        return False

def check_package(package_name, description=""):
    """Check if a package is installed"""
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name} {description}")
        return True
    except ImportError:
        print(f"❌ {package_name} {description} - NOT INSTALLED")
        return False

def check_packages():
    """Check all required packages"""
    print("\n🔍 Checking dependencies...")
    
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
    
    print(f"\n📊 Result: {success_count}/{len(packages)} packages installed")
    return success_count == len(packages)

def check_env_variables():
    """Check if environment variables are configured"""
    print("\n🔍 Checking environment configuration...")
    
    # Try to load .env file
    if os.path.exists('.env'):
        load_dotenv()
        print("✅ .env file found")
    else:
        print("⚠️  .env file not found - using system variables")
    
    # Required variables
    required_vars = [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY", 
        "AZURE_OPENAI_DEPLOYMENT",
        "API_VERSION"
    ]
    
    # Optional variables by lab
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
    
    # Check required variables
    missing_required = []
    for var in required_vars:
        value = os.getenv(var)
        if value and value.strip():
            print(f"✅ {var}")
        else:
            print(f"❌ {var} - NOT CONFIGURED")
            missing_required.append(var)
    
    # Check optional variables
    for lab, vars_list in optional_vars.items():
        print(f"\n{lab} (optional):")
        for var in vars_list:
            value = os.getenv(var)
            if value and value.strip():
                print(f"  ✅ {var}")
            else:
                print(f"  ⚠️  {var} - not configured")
    
    if missing_required:
        print(f"\n❌ Required variables not configured: {', '.join(missing_required)}")
        return False
    else:
        print("\n✅ All required variables are configured")
        return True

def check_sample_files():
    """Check if sample files exist"""
    print("\n🔍 Checking sample files...")
    
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
            print(f"❌ {file_path} - not found")
    
    print(f"\n📊 Files found: {found_files}/{len(sample_files)}")
    return found_files == len(sample_files)

def test_azure_openai_connection():
    """Test Azure OpenAI connection"""
    print("\n🔍 Testing Azure OpenAI connection...")
    
    try:
        from openai import AzureOpenAI
        
        client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("API_VERSION")
        )
        
        # Simple test
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {"role": "user", "content": "Just say 'Connection OK'"}
            ],
            max_tokens=10
        )
        
        if response.choices[0].message.content:
            print("✅ Azure OpenAI connection - OK")
            return True
        else:
            print("❌ Azure OpenAI connection - Failed")
            return False
            
    except Exception as e:
        print(f"❌ Azure OpenAI connection error: {str(e)}")
        return False

def main():
    """Main function"""
    print("🚀 Azure AI Foundry Workshop - Environment Check")
    print("="*60)
    
    checks = [
        check_python_version(),
        check_packages(),
        check_env_variables(),
        check_sample_files(),
        test_azure_openai_connection()
    ]
    
    print("\n" + "="*60)
    print("📋 FINAL SUMMARY")
    print("="*60)
    
    if all(checks):
        print("🎉 SUCCESS! The environment is configured correctly.")
        print("✅ You can run all laboratories.")
        print("\n📚 Next steps:")
        print("1. Open Lab 1 to get started")
        print("2. Execute cells in order")
        print("3. Proceed with the remaining labs")
    else:
        print("⚠️  WARNING! Some issues were found.")
        print("📋 Recommended actions:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Configure .env file with your credentials")
        print("3. Run this script again")
        print("4. Consult SETUP.md file for more details")
    
    print("\n💡 For additional support, consult the SETUP.md file")

if __name__ == "__main__":
    main()
