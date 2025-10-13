import customtkinter as ctk
from tkinter import filedialog
import os
import threading
from api_handler import analyze_with_gemini

class App(ctk.CTk):
   
    def __init__(self):
        super().__init__()

        # --- Configurações da Janela Principal ---
        self.title("Analisador de Processos PJE com Gemini")
        self.geometry("700x400")
        self.center_window(700, 400)

        # Define o tema de cores
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.selected_file_path = None

        # --- Widgets da Interface ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.instruction_label = ctk.CTkLabel(
            self.main_frame,
            text="Selecione o arquivo do processo (PDF ou TXT) para iniciar a análise.",
            font=ctk.CTkFont(size=14),
            wraplength=600
        )
        self.instruction_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10))

        self.select_file_button = ctk.CTkButton(
            self.main_frame,
            text="Selecionar Arquivo",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.select_file_callback
        )
        self.select_file_button.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        self.selected_file_label = ctk.CTkLabel(
            self.main_frame,
            text="Nenhum arquivo selecionado.",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.selected_file_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(5, 10))

        self.start_button = ctk.CTkButton(
            self.main_frame,
            text="Iniciar Análise e Salvar",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.start_analysis_thread,
            state="disabled"
        )
        self.start_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20, ipadx=10, ipady=10)

        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="Status: Aguardando arquivo...",
            font=ctk.CTkFont(size=12),
            wraplength=650
        )
        self.status_label.grid(row=4, column=0, columnspan=2, padx=20, pady=(10, 20))

    def select_file_callback(self):
        """
        Abre a janela para seleção de arquivo e atualiza a interface.
        """
        self.selected_file_path = filedialog.askopenfilename(
            title="Selecione o processo",
            filetypes=(("Arquivos PDF", "*.pdf"), ("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*"))
        )
        if self.selected_file_path:
            self.selected_file_label.configure(text=os.path.basename(self.selected_file_path), text_color="white")
            self.status_label.configure(text="Status: Arquivo pronto para análise.", text_color="gray")
            self.start_button.configure(state="normal")
        else:
            self.selected_file_label.configure(text="Nenhum arquivo selecionado.", text_color="gray")
            self.status_label.configure(text="Status: Aguardando arquivo...", text_color="gray")
            self.start_button.configure(state="disabled")

    def start_analysis_thread(self):
        """
        Inicia a análise em uma thread separada para não travar a UI.
        """
        self.start_button.configure(state="disabled", text="Analisando...")
        self.status_label.configure(text="Status: Iniciando análise com Gemini... Isso pode levar um momento.", text_color="cyan")
        
        # Cria e inicia a thread
        analysis_thread = threading.Thread(target=self.run_analysis)
        analysis_thread.daemon = True
        analysis_thread.start()

    def run_analysis(self):
        """
        Função que executa a análise e lida com o resultado.
        """
        try:
            print("Iniciando análise com Gemini...")
            csv_data = analyze_with_gemini(self.selected_file_path)
            print("Análise concluída. Solicitando local para salvar...")
            
            # Pede ao thread principal para abrir o diálogo de salvar
            self.after(0, self.save_result, csv_data)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            self.after(0, self.update_status_error, str(e))

    def save_result(self, csv_data):
        """
        Abre a janela "Salvar como" e salva o arquivo com a codificação correta.
        """
        if not csv_data:
            self.update_status_error("A análise não retornou dados.")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile=f"analisado_{os.path.basename(self.selected_file_path).split('.')[0]}.csv"
        )
        
        if save_path:
            try:

                with open(save_path, 'w', newline='', encoding='utf-8-sig') as f:
                    f.write(csv_data)
                
                self.status_label.configure(text=f"Status: Análise salva com sucesso em:\n{save_path}", text_color="green")
            except Exception as e:
                self.update_status_error(f"Erro ao salvar arquivo: {e}")
        else:
            self.status_label.configure(text="Status: Salvamento cancelado pelo usuário.", text_color="yellow")

        self.start_button.configure(state="normal", text="Iniciar Análise e Salvar")

    def update_status_error(self, error_message):
        """
        Atualiza a label de status com uma mensagem de erro.
        """
        self.status_label.configure(text=f"Status: Erro! {error_message}", text_color="red")
        self.start_button.configure(state="normal", text="Iniciar Análise e Salvar")

    def center_window(self, width, height):
        """
        Função para centralizar a janela no ecrã.
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

