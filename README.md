# Projeto ASCII Art 🎨

Este projeto converte imagens em arte ASCII utilizando Python. Ele é composto por dois módulos principais:

- **image_processor.py**: Processa a imagem de entrada (redimensiona e converte para escala de cinza).
- **ascii_converter.py**: Converte a imagem processada em arte ASCII.

---

## 📂 Estrutura do Repositório

ascii-art-project/

├── src/ # Diretório principal do código-fonte

│ ├── ascii_converter.py # Conversão para arte ASCII

│ ├── image_processor.py # Processamento de imagens

│ └── main.py # Script principal 

├── .gitignore # Arquivos ignorados pelo Git

├── README.md # Documentação do projeto

├── requirements.txt # Dependências do projeto


## 🚀 Como Executar

### 1. Instale as Dependências
Certifique-se de ter o Python 3.13.2-amd64 instalado. Em seguida, instale as dependências:
pip install -r requirements.txt


### 2. Execute o Teste de Integração
Use o script `main.py` para testar os módulos:
python main.py


### 3. Resultados Gerados:
- A imagem processada será salva como `processed.output`.
- A arte ASCII será salva como `output_ascii`.


## 🛠️ Tecnologias Utilizadas

- **Python 3.13.2**
- **Pillow**: Biblioteca para manipulação de imagens.
- **NumPy**: Biblioteca para cálculos numéricos.

## Melhorias:
- Adicionar estilos nas artes geradas
- Modificação no ascii_converter.py nas suas opções de salvamento da arte
- Nessa opção, colocar a alternativa para o usuario de escolher esse save em .txt ou image
- Makefile

 (FUTURAMENTE) 
- adicionar IA a fim de desenhar com diferentes estilos, redes neurais convulacionais
- testes unitarios
- GIF
