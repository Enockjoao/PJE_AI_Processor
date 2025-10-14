# Analisador de Processos Jurídicos com Gemini AI
📖 Sobre o Projeto
O Analisador de Processos Jurídicos é uma aplicação de desktop desenvolvida em Python que utiliza o poder da Inteligência Artificial generativa do Google Gemini para automatizar a análise e extração de dados de documentos processuais. A ferramenta lê arquivos .pdf e .txt contendo peças jurídicas, como petições ou apelações, e gera uma planilha .csv estruturada com as informações mais relevantes, otimizando o tempo e a eficiência na triagem de processos.

Este projeto foi criado como uma demonstração prática de habilidades em desenvolvimento de software, integração de APIs de IA e criação de interfaces gráficas, sendo uma peça central do meu portfólio profissional.

# ✨ Funcionalidades Principais
Interface Gráfica Intuitiva: Interface limpa e moderna construída com a biblioteca CustomTkinter.

Suporte a Múltiplos Formatos: Capacidade de processar tanto arquivos de texto (.txt) quanto documentos PDF (.pdf).

Análise com IA: Integração direta com a API do Google Gemini (2.0 Pro) para realizar a extração e classificação inteligente dos dados.

Exportação de Dados: Salva os resultados em um arquivo .csv formatado, pronto para ser utilizado em planilhas ou sistemas de banco de dados.

Processamento Assíncrono: A análise dos documentos é executada em uma thread separada para garantir que a interface do usuário permaneça responsiva durante o processamento.

# Planejamento

--
<img width="1014" height="789" alt="image" src="https://github.com/user-attachments/assets/dd33e4b4-e0d5-4782-b6a5-699342577aad" />
--

# 📸 Demonstração

## Tela Inicial do Programa.
<img width="866" height="532" alt="1" src="https://github.com/user-attachments/assets/eb563b77-9589-4ede-8670-c7c9e9f5995e" />

## Escolha do Processo a ser Analisado.
<img width="1392" height="747" alt="2" src="https://github.com/user-attachments/assets/f03ada06-01c8-4dac-b3c1-1c47fb2b6336" />

## PDF em Processo de Analise.
<img width="884" height="538" alt="3" src="https://github.com/user-attachments/assets/47b1a48f-4375-44b3-9f65-ba933fd0411a" />

## Processo Baixado em CSV.
<img width="1864" height="286" alt="4" src="https://github.com/user-attachments/assets/88eb6b2b-ffc9-42b9-b581-a25168822b97" />


# 🛠️ Tecnologias Utilizadas
 Python 3.8+

 CustomTkinter: Para a criação da interface gráfica.

 Google Generative AI: Biblioteca oficial para interagir com a API do Gemini.

 PyPDF2: Para a extração de texto de arquivos PDF.

 python-dotenv: Para o gerenciamento seguro de chaves de API.

# 🚀 Instalação e Execução
Siga os passos abaixo para executar o projeto em seu ambiente local.

### 1. Pré-requisitos
Python 3.8 ou superior instalado.

Uma chave de API do Google Gemini. Você pode obter uma gratuitamente no Google AI Studio.

## 2. Clonar o Repositório

```
git clone [https://github.com/Enockjoao/PJE_AI_Processor.git](https://github.com/Enockjoao/PJE_AI_Processor.git)
cd PJE_Gemini_Processor
```


## 3. Instalar as Dependências
É altamente recomendável criar um ambiente virtual para isolar as dependências do projeto.

## Criar um ambiente virtual (opcional, mas recomendado)

```
python -m venv venv
```

# Ativar o ambiente virtual
### No Windows:

.venv\Scripts\activate.bat

### No macOS/Linux:

```
source .venv/bin/activate
```


## Instalar as bibliotecas necessárias

```
pip install -r requirements.txt
```


## 4. Configurar as Variáveis de Ambiente
Crie um arquivo chamado .env na raiz do projeto, copiando o conteúdo do arquivo .env.example. Em seguida, insira sua chave da API do Gemini.

Arquivo .env:

```
GEMINI_API_KEY="SUA_CHAVE_DE_API_AQUI"
```

## 5. Executar a Aplicação
Com tudo configurado, execute o script principal para iniciar a interface.

```
python main.py
```

## ⚙️ Como Usar
Com a aplicação aberta, clique no botão "Selecionar Arquivo".

Escolha um arquivo de processo no formato .pdf ou .txt.

O nome do arquivo aparecerá na tela. Clique no botão "Iniciar Análise e Salvar".

Aguarde o processamento. O status será atualizado na parte inferior da janela.

Ao final, uma janela de "Salvar como..." será aberta. Escolha o local e o nome para o seu arquivo .csv.

Pronto! Seu processo foi analisado e os dados foram salvos.

## 🔧 Como Customizar a Análise (Prompt)
A inteligência da extração reside no "prompt" enviado à API. Você pode customizar completamente o que a IA deve extrair e como ela deve formatar a saída.

Abra o arquivo api_handler.py.

Localize a variável prompt dentro da função analyze_with_gemini.

Altere as instruções, o cabeçalho do CSV e as regras de extração para atender às suas necessidades específicas.

--
## ⚖️ Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
--


## 👨‍💻 Autor
Feito por Enock
Linkedin: [link](www.linkedin.com/in/joao-victor-enock-972b682b9)





