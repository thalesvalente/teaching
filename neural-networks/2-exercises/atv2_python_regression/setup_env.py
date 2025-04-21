from pathlib import Path

# Código Python corrigido com boas práticas
import os
import subprocess
import sys
from pathlib import Path


def create_venv(env_name="regressao-linear-ex1"):
    """
    Cria um ambiente virtual com o nome especificado.
    """
    import venv

    print(f"🔧 Criando ambiente virtual '{env_name}'...")
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(env_name)
    print(f"✅ Ambiente virtual '{env_name}' criado com sucesso.")


def install_requirements(env_name="regressao-linear-ex1", req_file="REQUIREMENTS.txt"):
    """
    Instala os pacotes do arquivo REQUIREMENTS.txt dentro do ambiente virtual.
    """
    if os.name == "nt":
        pip_path = os.path.join(env_name, "Scripts", "pip.exe")
        activate_cmd = f".\\{env_name}\\Scripts\\activate && python ex1.py"
    else:
        pip_path = os.path.join(env_name, "bin", "pip")
        activate_cmd = f"source ./{env_name}/bin/activate && python ex1.py"

    print(f"📦 Instalando dependências do arquivo '{req_file}'...")
    subprocess.check_call([pip_path, "install", "-r", req_file])
    print("✅ Instalação concluída com sucesso.\n")
    print("🚀 Para ativar o ambiente e executar o projeto, use:")
    print(f"  {activate_cmd}")


if __name__ == "__main__":
    create_venv()
    if Path("REQUIREMENTS.txt").exists():
        install_requirements()
    else:
        print("⚠️ Arquivo 'REQUIREMENTS.txt' não encontrado. Crie um e liste suas dependências.")