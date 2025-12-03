import os
import google.generativeai as genai
from dotenv import load_dotenv
import PyPDF2

load_dotenv()


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
        if file_path.lower().endswith('.pdf'):
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    file_content += page.extract_text() or ""
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado em: {file_path}")
    except Exception as e:
        raise IOError(f"Não foi possível ler o arquivo: {e}")


    prompt = f"""
    ### INSTRUÇÃO MESTRA ###
    Você atuará como um especialista jurídico multidisciplinar na análise e triagem inicial de um documento processual (Apelação Cível ou Recurso Inominado). Sua tarefa é ler o documento, identificar os principais elementos técnicos e jurídicos, e formatar a análise completa como um arquivo TSV (separado por tabulação).

    ### REGRAS DE EXTRAÇÃO E CLASSIFICAÇÃO ###
    1.  **Processo:** Identifique com precisão o número do Processo/Apelação Cível. Não confunda com o número do processo de origem.
    2.  **Classe:** Identifique a classe processual (ex: Apelação Cível, Recurso Inominado).
    3.  **Ramo do Direito:** Classifique a matéria jurídica principal em um dos seguintes ramos: TRIBUTÁRIO, PROCESSUAL CIVIL, ADMINISTRATIVO, AMBIENTAL, PREVIDENCIÁRIO, CONSELHOS PROFISSIONAIS, ou uma combinação (ex: TRIBUTÁRIO / PROCESSUAL CIVIL).
    4.  **Assunto:** Defina o assunto principal de forma sucinta (ex: Retido na fonte, Excesso de Peso).
    5.  **Palavras-Chaves:** Extraia as palavras-chave (keywords) técnicas mais relevantes que representem os temas de mérito. Use ponto e vírgula para separar os termos DENTRO das aspas.
    6.  **Questão Controvertida:** Descreva o ponto central do debate jurídico de forma clara, objetiva e juridicamente fundamentada, em uma ou duas frases.
    7.  **Legislação Citada:** Identifique e liste TODA a legislação mencionada, citando conforme o padrão oficial (ex: Lei n. 9.873/1999, art. 1º, §1º; CPC/2015, art. 485 V e VI). Use ponto e vírgula para separar as diferentes leis DENTRO das aspas.
    8.  **Data de distribuição:** Encontre a data de distribuição ou a data de autuação do recurso no formato DD/MM/AAAA. Se não for encontrada, deixe o campo em branco.

    ### REGRAS DE FORMATAÇÃO DA SAÍDA ###
    1.  **Formato:** O resultado deve ser um arquivo TSV (Tab-Separated Values).
    2.  **Separador de colunas:** Use TABULAÇÃO (Tab) como separador entre as colunas. NÃO use ponto e vírgula como separador de colunas.
    3.  **Cabeçalho:** A primeira linha deve ser exatamente (com TAB entre cada coluna):
        Processo[TAB]Classe[TAB]Ramo do Direito[TAB]Assunto[TAB]Palavras-Chaves[TAB]Questão Controvertida[TAB]Legislação Citada[TAB]Data de distribuição
    4.  **Linha de Dados:** A segunda linha contém os dados extraídos, separados por TAB.
    5.  **IMPORTANTE - Campos entre aspas:** Os campos "Palavras-Chaves" e "Legislação Citada" DEVEM estar envolvidos por aspas duplas ("). Exemplo: "execução fiscal; prescrição ordinária; interrupção da prescrição"
    6.  **Saída Limpa:** Responda APENAS com o cabeçalho e a linha de dados. Não inclua texto explicativo, comentários, ou formatação como ```tsv ou ```csv.

    ### EXEMPLO DE SAÍDA ESPERADA ###
    Processo	Classe	Ramo do Direito	Assunto	Palavras-Chaves	Questão Controvertida	Legislação Citada	Data de distribuição
    0000072-16.2019.4.01.3311	Apelação Cível	TRIBUTÁRIO	Simples Nacional / Prescrição	"execução fiscal; prescrição ordinária; interrupção da prescrição"	Discute-se a ocorrência de prescrição ordinária dos créditos tributários.	"Lei n. 6.830/1980, art. 8º; CTN, art. 174"	13/08/2024

    ### TEXTO DO PROCESSO PARA ANÁLISE ###
    ---
    {file_content}
    ---

    ### CONTEÚDO TSV GERADO ###
    """
    
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(prompt)
    

    cleaned_response = response.text.strip()

    if cleaned_response.startswith("```"):
        lines = cleaned_response.split("\n")

        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        cleaned_response = "\n".join(lines)
    
    cleaned_response = cleaned_response.replace("`", "").strip()
    if cleaned_response.lower().startswith("tsv"):
        cleaned_response = cleaned_response[3:].strip()
    if cleaned_response.lower().startswith("csv"):
        cleaned_response = cleaned_response[3:].strip()
        
    return cleaned_response
