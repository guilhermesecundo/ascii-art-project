# Projeto ASCII Art 🎨

Este projeto converte imagens em arte ASCII utilizando Python. Ele é composto por dois módulos principais:
- **image_processor.py**: Processa a imagem de entrada (redimensiona e converte para escala de cinza).
- **ascii_converter.py**: Converte a imagem processada em arte ASCII.

---

## 📂 Estrutura do Repositório

ascii-art-project/
├── pycache/ # Arquivos de cache do Python

├── ascii_converter.cpython-312.pyc # Cache compilado do ascii_converter.py

├── image_processor.cpython-312.pyc # Cache compilado do image_processor.py

├── src/ # Diretório principal do código-fonte

│ ├── ascii_converter.py # Conversão para arte ASCII

│ ├── image_processor.py # Processamento de imagens

│ └── main.py # Script principal (a ser planejado)

├── .gitignore # Arquivos ignorados pelo Git

├── README.md # Documentação do projeto

├── requirements.txt # Dependências do projeto

└── test_integration.py # Script para testar a integração dos módulos

## 🚀 Como Executar

### 1. Instale as Dependências
Certifique-se de ter o Python 3.13.2-amd64 instalado. Em seguida, instale as dependências:
pip install -r requirements.txt


### 2. Execute o Teste de Integração
Use o script `test_integration.py` para testar os módulos:
python test_integration.py


### 3. Resultados Gerados:
- A imagem processada será salva como `pendente`.
- A arte ASCII será salva como `pendente`.


## 🛠️ Tecnologias Utilizadas

- **Python 3.13.2**
- **Pillow**: Biblioteca para manipulação de imagens.
- **NumPy**: Biblioteca para cálculos numéricos.
