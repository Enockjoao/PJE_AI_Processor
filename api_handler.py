import os
import google.generativeai as genai
from dotenv import load_dotenv
import PyPDF2

load_dotenv()

# --- Configuração da API do Gemini ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("AVISO: Chave da API Gemini não encontrada no arquivo .env")

def analyze_with_gemini(file_path):
    """
    Lê o conteúdo de um arquivo (TXT ou PDF), envia para a API do Gemini com instruções específicas Sobre o Tema "Juridico" 
    e retorna os dados da planilha gerada.
    """
    if not GEMINI_API_KEY:
        raise ConnectionError("A chave da API Gemini não foi configurada.")

    file_content = ""
    try:
        # Verifica se o arquivo é um PDF
        if file_path.lower().endswith('.pdf'):
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                # Extrai o texto de todas as páginas
                for page in pdf_reader.pages:
                    file_content += page.extract_text() or ""
        # Caso contrário, trata como arquivo de texto
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado em: {file_path}")
    except Exception as e:
        raise IOError(f"Não foi possível ler o arquivo: {e}")

    # --- INSTRUÇÕES PARA TRIAGEM PROCESSUAL ESPECIALIZADA ---
    prompt = f"""
    ### INSTRUÇÃO MESTRA ###
    Você atuará como um especialista jurídico multidisciplinar na análise e triagem inicial de um documento processual (Apelação Cível ou Recurso Inominado). Sua tarefa é ler o documento, identificar os principais elementos técnicos e jurídicos, e formatar a análise completa como um arquivo CSV.

    ### REGRAS DE EXTRAÇÃO E CLASSIFICAÇÃO ###
    1.  **Processo:** Identifique com precisão o número do Processo/Apelação Cível. Não confunda com o número do processo de origem.
    2.  **Classe:** Identifique a classe processual (ex: APELAÇÃO CÍVEL, RECURSO INOMINADO).
    3.  **Ramo do Direito:** Classifique a matéria jurídica principal em um dos seguintes ramos: TRIBUTÁRIO, PROCESSUAL CIVIL, ADMINISTRATIVO, AMBIENTAL, PREVIDENCIÁRIO, CONSELHOS PROFISSIONAIS, ou uma combinação (ex: TRIBUTÁRIO / PROCESSUAL CIVIL).
    4.  **Assunto:** Defina o assunto principal de forma sucinta (ex: Retido na fonte, Excesso de Peso).
    5.  **Palavras-Chaves:** Extraia as palavras-chave (keywords) técnicas mais relevantes que representem os temas de mérito. Use vírgulas para separar os termos.
    6.  **Questão Controvertida:** Descreva o ponto central do debate jurídico de forma clara, objetiva e juridicamente fundamentada, em uma ou duas frases.
    7.  **Legislação Citada:** Identifique e liste TODA a legislação mencionada, citando conforme o padrão oficial (ex: Lei n. 9.873/1999, art. 1º, §1º; CPC/2015, art. 485 V e VI). Use ponto e vírgula para separar as diferentes leis.
    8.  **Data de distribuição:** Encontre a data de distribuição ou a data de autuação do recurso. Se não for encontrada, deixe o campo em branco.

    ### REGRAS DE FORMATAÇÃO DA SAÍDA ###
    1.  **Formato:** O resultado deve ser um CSV válido.
    2.  **Separador:** Utilize ponto e vírgula (;) como separador de colunas.
    3.  **Cabeçalho Obrigatório:** A primeira linha da sua resposta DEVE SER EXATAMENTE:
        Processo;Classe;Ramo do Direito;Assunto;Palavras-Chaves;Questão Controvertida;Legislação Citada;Data de distribuição
    4.  **Linha de Dados:** A segunda linha deve conter os dados extraídos, seguindo a ordem do cabeçalho.
    5.  **Saída Limpa:** Não inclua NENHUM texto, explicação, comentários ou formatação (como ` ```csv `) antes ou depois do conteúdo CSV. A resposta deve ser apenas o cabeçalho e a linha de dados.

    ### TEXTO DO PROCESSO PARA ANÁLISE ###
    ---
    {file_content}
    ---

    ### CONTEÚDO CSV GERADO ###
    """
    
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(prompt)
    
    # Limpa a resposta para garantir que seja apenas o CSV
    cleaned_response = response.text.strip().replace("`", "")
    if cleaned_response.startswith("csv"):
        cleaned_response = cleaned_response[3:].strip()
        
    return cleaned_response

