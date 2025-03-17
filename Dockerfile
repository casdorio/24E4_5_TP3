# Escolhe uma imagem base com Python
FROM fedora:latest

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Atualiza o sistema e instala pacotes necessários
RUN dnf update -y && dnf install -y \
    python3 \
    python3-pip \
    gcc \
    python3-devel \
    && dnf clean all

# Instala as bibliotecas Python necessárias
RUN pip install --no-cache-dir \
    numpy \
    asyncio \
    multiprocess

# Expõe a porta (caso necessário para futuras extensões ou APIs)
EXPOSE 8000

# Define o comando padrão para iniciar um terminal Python interativo
CMD ["python3"]
